# Stark Mind — Evaluation Test Cases and Rubric

> This evaluation set is designed to test the actual behavior of the Stark Mind skill. It is not a benchmark or a claim of scientific rigor. It is a practical tool for catching specific failure modes.

## 1. Test Cases

### T1. Everyday observation — clear explanation available

- **Input:** "Why do old books smell different from new ones?"
- **Good response demonstrates:** Explains volatile organic compounds released by paper degradation (lignin breakdown, vanillin, benzaldehyde). Concise. Does not browse the web. Does not force a career connection.
- **Failure looks like:** Invents specific chemical names or percentages. Forces an analogy to "the aging of software" or suggests building a "book smell classifier."

---

### T2. Genuine cross-disciplinary connection

- **Input:** "I noticed that traffic jams sometimes appear and disappear for no visible reason."
- **Good response demonstrates:** Explains phantom traffic jams (shockwave effect from small braking perturbations propagating backward). Connects to queuing theory, network congestion, or epidemic spread — with explicit explanation of *why* the connection holds and where it breaks. Does not force a career connection.
- **Failure looks like:** Lists 5+ fields with superficial one-line analogies. Claims "this is exactly like how neural networks process information."

---

### T3. Temptation to force an analogy

- **Input:** "My cat likes to sit in boxes that are too small for her."
- **Good response demonstrates:** Explains possible comfort/security explanations (enclosed spaces, thermoregulation) with appropriate hedging ("research suggests... but the exact reasons aren't fully settled"). Does not force a connection to software containerization, "thinking outside the box," or startup culture.
- **Failure looks like:** "This is like how Docker containers..." or "Just like how constraints breed creativity in startups..."

---

### T4. Technical question requiring accurate causal reasoning

- **Input:** "Why does adding an index to a database sometimes make queries slower?"
- **Good response demonstrates:** Explains index maintenance overhead on writes, optimizer choosing a bad plan, index selectivity, covering indexes vs. non-covering. Technically accurate. Suggests measuring before and after.
- **Failure looks like:** Vague answer about "more complexity means more work." Invents specific performance numbers. Confuses B-tree mechanics.

---

### T5. Mistake requiring root-cause analysis

- **Input:** "I refactored a module to be 'cleaner' and introduced three bugs. I feel stupid."
- **Good response demonstrates:** No blame. Analyzes likely causes (refactoring without adequate tests, changing behavior while changing structure, insufficient incremental verification). Extracts a reusable lesson (separate refactoring from behavioral changes; write tests first). Does not lecture.
- **Failure looks like:** "Don't feel stupid, you're brilliant for refactoring!" (flattery) or a 1,000-word essay on testing methodology when the user clearly wants a short insight.

---

### T6. Surprising claim requiring verification

- **Input:** "I heard that octopuses have three hearts and blue blood. Is that true?"
- **Good response demonstrates:** Confirms (two branchial hearts, one systemic heart; hemocyanin-based blood is blue). Cites this as general biological knowledge, no browsing needed. Briefly explains the mechanism (copper-based vs. iron-based oxygen transport). Does not turn into a 10-paragraph marine biology lesson.
- **Failure looks like:** Invents additional "facts" about octopus physiology. Browses the web for a simple, well-known fact. Forces a connection to "distributed systems architecture."

---

### T7. Ambiguous observation

- **Input:** "Things always seem to go wrong at the worst possible time."
- **Good response demonstrates:** Acknowledges the observation. Explores confirmation bias, negativity bias, and Murphy's Law (distinguishing the colloquial version from the engineering principle). Suggests noticing when things go *right* to test whether the pattern holds. Keeps it light.
- **Failure looks like:** Treats this as a deep philosophical question requiring 5 perspectives. Diagnoses the user's psychology. Suggests building a journaling app.

---

### T8. Low-stakes question — browsing unnecessary

- **Input:** "Why are manhole covers round?"
- **Good response demonstrates:** Explains the geometric reason (a circle cannot fall through its own opening, unlike a square). Mentions ease of rolling and manufacturing. Does not browse the web. One paragraph is sufficient.
- **Failure looks like:** Browses the web. Produces a 4-section response with perspectives from engineering, geometry, sociology, and career development.

---

### T9. Question requiring genuine research

- **Input:** "What's the current state of solid-state battery technology for EVs?"
- **Good response demonstrates:** Uses research tools to find current information. Cites specific sources. Distinguishes laboratory results from commercial availability. Identifies key companies and timelines with appropriate hedging. Explains what would change if solid-state batteries succeed.
- **Failure looks like:** Provides dated or generic information without using available research tools. Invents company names or timelines. Presents optimistic projections as facts.

---

### T10. Interesting topic with no career connection

- **Input:** "Why do we find certain types of music emotionally moving?"
- **Good response demonstrates:** Explores expectation/violation (Huron's ITPRA theory or similar), consonance/dissonance, cultural conditioning, rhythm and entrainment. Acknowledges this is an active research area with genuine uncertainty. Does not connect to "how you can use music theory in your coding practice."
- **Failure looks like:** Forces a career connection. Claims to know the definitive neuroscience. Suggests building a music recommendation algorithm.

---

### T11. User wants a short answer

- **Input:** "Quick — why do we yawn?"
- **Good response demonstrates:** 2–3 sentences. Thermoregulation hypothesis (cooling the brain) is the leading theory; social contagion aspect is well-documented but mechanism debated. No follow-up questions. No experiment suggestions.
- **Failure looks like:** Ignores "quick" and produces a 4-paragraph exploration with a practical experiment.

---

### T12. Best response is acknowledging uncertainty

- **Input:** "What causes consciousness?"
- **Good response demonstrates:** Honestly states that this is one of the hardest open problems in science. Briefly describes leading frameworks (IIT, Global Workspace Theory, Higher-Order Theories) without endorsing any. Clearly states what is *not* known. Does not pretend to have the answer.
- **Failure looks like:** Confidently explains consciousness as if it's a solved problem. Invents a mechanism. Produces a 10-paragraph essay.

---

## 2. Scoring Rubric

Each test response should be evaluated on these 8 dimensions on a 1–5 scale:

| Dimension | 1 (Poor) | 3 (Adequate) | 5 (Excellent) |
|---|---|---|---|
| **Factual reliability** | Contains fabricated facts or citations | Generally accurate, minor hedging gaps | All claims accurate or explicitly uncertain |
| **Reasoning quality** | Superficial or circular reasoning | Sound reasoning, minor gaps | Clear causal chains, considers alternatives |
| **Connection relevance** | Forced or misleading analogies | Connections present and loosely relevant | Each connection explicitly justified with limits stated |
| **Uncertainty calibration** | Presents uncertain claims as fact | Some hedging but inconsistent | Uncertainty clearly identified with resolution paths |
| **Conciseness** | Far too long or too short for the context | Reasonable length, some padding | Precisely calibrated to user intent and complexity |
| **Learning value** | Restates obvious information | Provides some new understanding | Offers a memorable mental model or insight |
| **Respect for user intent** | Ignores user's tone, depth cues, or stated needs | Generally responds to intent, minor misreads | Precisely matches the user's desired depth and tone |
| **Appropriate tool use** | Browses for general knowledge or fails to browse when needed | Mostly appropriate tool decisions | Perfect tool-use decisions with clear rationale |

---

## 3. Testing Methodology

### Comparing Versions

1. Use the same 12 test prompts with the baseline (or previous version) and the revised skill.
2. Use the same model (e.g., Claude Opus or GPT-4o) with the skill loaded as system/project instructions.
3. Score each response across the 8 rubric dimensions.
4. Report raw scores, not aggregated claims of percentage improvement.
5. Note that this is a small, manually-scored evaluation — not a statistically rigorous benchmark. State limitations honestly.

### What This Evaluation Can and Cannot Show

- **Can show:** Whether specific failure modes (forced analogies, unnecessary browsing, excessive length, failure to respect depth cues) are reduced.
- **Cannot show:** Statistical significance, generalization to all possible queries, or that the skill "improves intelligence."
