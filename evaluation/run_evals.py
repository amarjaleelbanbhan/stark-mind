"""Run Stark Mind evals via `claude -p`. Usage: python run_evals.py <repo_dir> <out_dir> [trigger | T3 T6 ...]
Pass `trigger` to rerun only the trigger set, or test IDs to rerun only those tests (skill arm)."""
import json, os, re, shutil, subprocess, sys, tempfile
from concurrent.futures import ThreadPoolExecutor

repo, out = sys.argv[1], sys.argv[2]
MODEL = "sonnet"
skill = open(os.path.join(repo, "SKILL.md"), encoding="utf-8").read()
cases = open(os.path.join(repo, "evaluation", "test_cases.md"), encoding="utf-8").read()
BASE = "You are a helpful assistant."

# Behaviour prompts: the first quoted string on each "- **Input...:**" line.
tests = re.findall(r'### (T\d+)\..*?\n- \*\*Input[^*]*:\*\* "(.*?)"\n', cases, re.S)
assert len(tests) == 22, len(tests)
T21_CONTEXT = ("[Earlier in this conversation you explained phantom traffic jams: small braking "
               "perturbations propagate backward as shockwaves, like congestion in queues.]\n\n")

trig = cases.split("## 4. Trigger Set")[1]
should, should_not = trig.split("### Should not trigger")
trig_cases = [(q, True) for q in re.findall(r'^\d+\. "(.*)"$', should, re.M)] + \
             [(q, False) for q in re.findall(r'^\d+\. "(.*)"$', should_not, re.M)]
assert len(trig_cases) == 20, len(trig_cases)


def claude(args, prompt, cwd):
    r = subprocess.run(["claude", "-p", "--no-session-persistence", "--model", MODEL, *args, prompt],
                       cwd=cwd, capture_output=True, text=True, encoding="utf-8", timeout=600)
    return r.stdout


def behaviour(job):
    tid, prompt, arm = job
    sys_prompt = BASE if arm == "baseline" else BASE + "\n\n" + skill
    full = T21_CONTEXT + prompt if tid == "T21" else prompt
    with tempfile.TemporaryDirectory() as d:
        raw = claude(["--safe-mode", "--tools", "WebSearch,WebFetch", "--allowedTools", "WebSearch,WebFetch",
                      "--system-prompt", sys_prompt, "--output-format", "json"], full, d)
    d = json.loads(raw)
    path = os.path.join(out, "raw", arm, f"{tid}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"**Prompt:** {full}\n\n---\n\n{d.get('result', '')}\n")
    return tid, arm, d.get("total_cost_usd", 0), d.get("num_turns"), list(d.get("modelUsage", {}))


def trigger(job):
    q, expected = job
    with tempfile.TemporaryDirectory() as d:
        os.makedirs(os.path.join(d, ".claude", "skills", "stark-mind"))
        shutil.copy(os.path.join(repo, "SKILL.md"), os.path.join(d, ".claude", "skills", "stark-mind"))
        # Project settings only: skips the user's plugins and hooks, keeps the project skill.
        raw = claude(["--setting-sources", "project", "--strict-mcp-config", "--max-turns", "2",
                      "--output-format", "stream-json", "--verbose"], q, d)
    fired = False
    for line in raw.splitlines():
        try:
            ev = json.loads(line)
        except ValueError:
            continue
        msg = ev.get("message") if isinstance(ev, dict) else None
        for c in (msg.get("content") or [] if isinstance(msg, dict) else []):
            if isinstance(c, dict) and c.get("type") == "tool_use" and c.get("name") == "Skill" \
                    and "stark-mind" in json.dumps(c.get("input")):
                fired = True
    return q, expected, fired


for arm in ("baseline", "skill"):
    os.makedirs(os.path.join(out, "raw", arm), exist_ok=True)
only_trigger = sys.argv[3:] == ["trigger"]
only_tests = [] if only_trigger else sys.argv[3:]
jobs = [(t, p, "skill") for t, p in tests if t in only_tests] if only_tests else        [(t, p, a) for t, p in tests for a in ("baseline", "skill")]
with ThreadPoolExecutor(6) as ex:
    b = [] if only_trigger else list(ex.map(behaviour, jobs))
    t = [] if only_tests else list(ex.map(trigger, trig_cases))
json.dump({"behaviour": b, "trigger": t}, open(os.path.join(out, "run.json"), "w"), indent=1)
print("cost", round(sum(x[2] or 0 for x in b), 3), "models", {m for x in b for m in x[4]})
for q, e, f in t:
    print("OK " if e == f else "BAD", "expected" if e else "not-exp ", "fired" if f else "quiet", q)
