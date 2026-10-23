# Stark Mind v2 — Evaluation Results

- **Date:** 2026-10-23
- **Model:** `claude-sonnet-5` (via `claude -p --model sonnet`), one run per prompt.
- **Behaviour arms:** both use the system prompt "You are a helpful assistant." The skill arm appends the full `SKILL.md`. Run with `--safe-mode` (no user config, plugins, or hooks) and only WebSearch/WebFetch enabled.
- **Trigger arms:** the skill is installed as a project skill in an empty folder; a prompt counts as "fired" if Claude calls the `Skill` tool with `stark-mind`. User plugins and settings are not loaded.
- **Raw answers:** [`raw/baseline/`](raw/baseline/) and [`raw/skill/`](raw/skill/).
- **Runner:** [`../../run_evals.py`](../../run_evals.py).

## Limitations

- **One scorer.** Claude (Opus 5.5) scored every answer, so the scorer is the same model family that wrote them. It knew which arm was which. Treat scores as a structured opinion, not a measurement.
- **One sample per prompt.** Outputs vary between runs; a single run cannot separate a real effect from noise.
- **Facts were checked from the scorer's knowledge, not against sources.** T9 figures (company timelines, Wh/kg numbers) were not verified.
- **Trigger results are 20 prompts, one run each,** in a folder with about 15 other built-in skills. Real setups with many plugins may trigger differently.

## 1. Trigger set

| Description | Should trigger (10) | Should not trigger (10) |
|---|---|---|
| v1 (commit `5cc6893`) | 6 fired | 0 fired |
| v2 | **10 fired** | **0 fired** |

v1 missed: "Why do onions make you cry?", "How come cats always land on their feet?", "Quick — why is the ocean salty?", and "Our launch went much better than expected and I want to understand why."

The v2 change fixed **under-triggering**. v1 did *not* over-trigger on coding prompts in this test; the "Do NOT use" list in v2 is a safeguard that this test could not show was needed.

## 2. Behaviour scores (1–5, N/A where not applicable)

### Baseline (no skill)

| Test | Fact | Reason | Connect | Uncert | Concise | Learn | Intent | Tools | Words |
|---|---|---|---|---|---|---|---|---|---|
| T1 | 3 | 4 | N/A | 2 | 2 | 3 | 3 | 5 | 329 |
| T2 | 3 | 4 | N/A | 2 | 2 | 4 | 3 | 5 | 499 |
| T3 | 4 | 3 | N/A | 2 | 4 | 3 | 4 | 5 | 138 |
| T4 | 4 | 4 | N/A | 3 | 2 | 4 | 3 | 5 | 496 |
| T5 | 4 | 2 | N/A | N/A | 4 | 1 | 2 | 5 | 205 |
| T6 | 4 | 4 | N/A | 4 | 4 | 4 | 4 | 5 | 169 |
| T7 | 4 | 4 | N/A | 3 | 4 | 3 | 4 | 5 | 209 |
| T8 | 4 | 4 | N/A | 3 | 2 | 3 | 3 | 5 | 255 |
| T9 | 3 | 4 | N/A | 3 | 3 | 4 | 4 | 5 | 484 |
| T10 | 3 | 3 | N/A | 2 | 2 | 3 | 3 | 5 | 495 |
| T11 | 4 | 4 | N/A | 4 | 2 | 3 | 2 | 5 | 208 |
| T12 | 4 | 4 | N/A | 5 | 3 | 4 | 4 | 5 | 381 |
| T13 | 3 | 4 | N/A | 2 | 3 | 4 | 4 | 5 | 757 |
| T14 | 4 | 3 | N/A | N/A | 3 | 3 | 3 | 5 | 263 |
| T15 | 4 | 4 | N/A | 3 | 2 | 4 | 4 | 5 | 383 |
| T16 | 4 | 3 | N/A | 3 | 1 | 3 | 1 | 5 | 359 |
| T17 | 4 | 4 | N/A | 4 | 3 | 4 | 4 | 5 | 336 |
| T18 | 1 | 1 | N/A | 1 | 3 | 1 | 2 | 5 | 430 |
| T19 | 4 | 4 | N/A | 4 | 4 | 3 | 5 | 5 | 227 |
| T20 | 4 | 4 | N/A | 2 | 2 | 4 | 4 | 5 | 471 |
| T21 | 4 | 4 | N/A | N/A | 4 | 3 | 4 | 5 | 259 |
| T22 | 4 | 4 | N/A | N/A | 2 | 3 | 3 | 5 | 331 |

### With Stark Mind v2

| Test | Fact | Reason | Connect | Uncert | Concise | Learn | Intent | Tools | Words |
|---|---|---|---|---|---|---|---|---|---|
| T1 | 4 | 4 | 3 | 3 | 3 | 4 | 4 | 5 | 245 |
| T2 | 4 | 4 | 3 | 3 | 3 | 4 | 4 | 5 | 321 |
| T3 | 4 | 4 | 3 | 3 | 2 | 4 | 3 | 5 | 318 |
| T4 | 4 | 5 | 3 | 3 | 3 | 4 | 4 | 5 | 406 |
| T5 | 4 | 5 | N/A | N/A | 2 | 5 | 3 | 5 | 374 |
| T6 | 3 | 3 | 1 | 3 | 2 | 3 | 2 | 5 | 298 |
| T7 | 4 | 5 | 4 | 3 | 3 | 4 | 3 | 5 | 340 |
| T8 | 3 | 4 | 3 | 3 | 2 | 4 | 3 | 5 | 336 |
| T9 | 3 | 4 | 4 | 4 | 3 | 4 | 4 | 5 | 541 |
| T10 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 5 | 380 |
| T11 | 4 | 4 | N/A | 4 | 5 | 4 | 5 | 5 | 58 |
| T12 | 4 | 5 | 5 | 5 | 2 | 5 | 3 | 5 | 574 |
| T13 | 4 | 5 | 5 | 5 | 3 | 5 | 5 | 5 | 761 |
| T14 | 4 | 4 | N/A | N/A | 3 | 4 | 3 | 5 | 307 |
| T15 | 4 | 4 | 3 | 4 | 3 | 4 | 4 | 5 | 308 |
| T16 | 4 | 4 | 3 | 3 | 2 | 4 | 2 | 5 | 299 |
| T17 | 2 | 3 | 3 | 2 | 3 | 3 | 4 | 5 | 295 |
| T18 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 339 |
| T19 | 4 | 4 | N/A | 4 | 3 | 4 | 5 | 5 | 270 |
| T20 | 4 | 5 | N/A | 4 | 3 | 5 | 4 | 5 | 381 |
| T21 | 4 | 4 | N/A | N/A | 4 | 4 | 5 | 5 | 231 |
| T22 | 4 | 4 | N/A | N/A | 4 | 3 | 5 | 5 | 174 |

### Average per dimension (N/A excluded)

| Dimension | Baseline | Skill | Change |
|---|---|---|---|
| Fact | 3.64 | 3.77 | +0.14 |
| Reason | 3.59 | 4.18 | +0.59 |
| Connect | — | 3.40 | — |
| Uncert | 2.89 | 3.56 | +0.67 |
| Concise | 2.77 | 2.95 | +0.18 |
| Learn | 3.23 | 4.05 | +0.82 |
| Intent | 3.32 | 3.77 | +0.45 |
| Tools | 5.00 | 5.00 | +0.00 |

*Connect* has no baseline average: the baseline made no cross-field connections. The skill made one in 15 of 22 answers.

### Notes per test

| Test | Note |
|---|---|
| T1 | Baseline adds an unsourced 'Jubilee Library' claim. Skill adds a reasonable wine/new-car link but states no limits. |
| T2 | Baseline invents a '15-20% of capacity' threshold. Skill's fluid analogy has no stated limits. |
| T3 | No Docker analogy in either. Skill is 2.3x longer and adds an unrequested experiment. |
| T4 | Skill gives two clear failure modes and suggests EXPLAIN before/after; baseline is a 7-item list. |
| T5 | Baseline asks for code instead of giving the lesson. Skill gives the lesson but is long and asks two questions. |
| T6 | Skill forces a database-caching analogy (the listed failure) and opens with a made-up 'gravity' framing. |
| T7 | Skill's load-and-stakes reasoning is better; neither separates colloquial from engineering Murphy's Law. |
| T8 | Skill says a circle is 'the one shape' that can't fall through, then cites curves of constant width. Both too long. |
| T9 | Both searched and cited. Many sources are low-quality blogs; figures not verified. |
| T10 | Baseline is a 7-section list with mirror-neuron and Maslow padding. Skill picks one core mechanism and hedges. |
| T11 | Skill: 58 words, honours 'quick'. Baseline: 208 words in a 4-item list. |
| T12 | Skill's thermodynamics analogy states where it breaks, but the answer is 574 words. |
| T13 | Skill separates flutter, forced resonance and the Millennium Bridge, and flags its confidence. |
| T14 | Both ask many questions; skill's content-delivery-context split is more useful. |
| T15 | Both give clinician red flags and no diagnosis. Skill's 'threshold' pattern is plausible but not needed. |
| T16 | Neither is short for a tired user. Skill has a good fuel/ignition model but three sections. |
| T17 | Skill gives 'only ~10% of cells are neurons' as the likely origin, a contested claim stated without hedging. |
| T18 | Baseline plays the character and presents fictional palladium physics as fact. Skill declines and separates real fusion limits from fiction. |
| T19 | Both flag the injection and refuse it. |
| T20 | Baseline predicts 'tens of meters' tides without hedging. Skill frames the answer by scaling law and flags uncertainty. |
| T21 | Both say no memory tool is available. Only skill uses the Discovery note format. |
| T22 | Skill answers the task directly with no exploration. It shows `--force` rather than `--force-with-lease`. |


## 3. Findings

**Where the skill helps**
- **Depth cues:** `quick` (T11) dropped from 208 to 58 words; the deep dive (T13) was the best answer in the set.
- **Role-play (T18):** the baseline played the character and presented fictional physics as real; the skill declined and separated fact from fiction.
- **Tasks (T22):** the skill answered the git question directly with no exploration.
- **Saving a discovery (T21):** only the skill used the Discovery note format; both were honest about having no memory tool.
- **Uncertainty:** the largest gain in the averages (+0.67).

**Where the skill hurts — fix in the next version**
1. **Template leakage.** The optional formatting hints in SKILL.md step 2 ("What might be happening?", "A few useful angles", "The deeper pattern") appear as literal headings in 15 of 22 skill answers, including T9, T15, and T18. The model treats "optional hints" as a required template.
2. **Forced patterns and analogies.** Because "The deeper pattern" acts as a required section, the skill adds a pattern or analogy where none is needed. T6 compares octopus hearts to database caching — the exact failure T6 lists.
3. **Length on simple prompts.** The skill was longer than the baseline on T3, T5, T6, T7, T8, T12, and T14. Conciseness improved by only +0.18 overall, and only because of T11 and T22.
4. **More than one question.** T5 and T14 ask several questions despite the "at most one" rule.
5. **Confident origin stories.** T17 states a contested "10% of cells are neurons" explanation as the likely origin without hedging.

**Suggested next change:** remove the three heading hints from step 2, and state that a "deeper pattern" section is included only when it changes the user's understanding. Then rerun T3, T6, T8, and T17.
