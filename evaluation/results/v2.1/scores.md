# Stark Mind v2.1 — Targeted Rerun

- **Date:** 2026-10-23
- **Change tested:** removed the three formatting hints from step 2 ("What might be happening?", "A few useful angles", "The deeper pattern"). A deeper pattern is now named only when it changes the user's understanding, and short answers use plain prose.
- **Tests rerun:** T3, T6, T8, T17, skill arm only. Same model (`claude-sonnet-5`), settings, and runner as [v2](../v2/scores.md): `python evaluation/run_evals.py . evaluation/results/v2.1 T3 T6 T8 T17`.
- **Raw answers:** [`raw/skill/`](raw/skill/).

Same limitations as v2: one sample per prompt, one scorer (Claude Opus 5.5) who knew which version was which. Four prompts cannot show that the change generalizes.

## Template leakage

| | v2 | v2.1 |
|---|---|---|
| Answers using a hint as a heading | 4 of 4 | **0 of 4** |
| Answers with a "deeper pattern" section | 4 of 4 | **0 of 4** |

## Scores (Fact, Reason, Connect, Uncert, Concise, Learn, Intent, Tools)

| Test | Baseline | v2 | v2.1 | Words (base / v2 / v2.1) |
|---|---|---|---|---|
| T3 | 4,3,N/A,2,4,3,4,5 | 4,4,3,3,2,4,3,5 | 3,4,3,3,3,4,3,5 | 138 / 318 / 267 |
| T6 | 4,4,N/A,4,4,4,4,5 | 3,3,1,3,2,3,2,5 | 4,4,N/A,3,4,4,4,5 | 169 / 298 / 197 |
| T8 | 4,4,N/A,3,2,3,3,5 | 3,4,3,3,2,4,3,5 | 3,4,4,3,2,4,3,5 | 255 / 336 / 325 |
| T17 | 4,4,N/A,4,3,4,4,5 | 2,3,3,2,3,3,4,5 | 3,4,N/A,4,3,4,4,3 | 336 / 295 / 266 |

## Notes

- **T6 — fixed.** The database-caching analogy is gone. In its place is a plain cause-and-effect chain (copper chemistry → less efficient oxygen transport → extra hearts). It is 34% shorter and now matches the baseline on every dimension.
- **T17 — better, with a new problem.** The "10% of cells are neurons" claim is now one hedged possibility among several, not the likely origin. But the model ran a web search for a well-established myth, which the skill says not to do (Tools 5 → 3).
- **T3 — slightly better.** No forced "deeper pattern" section. Still about twice the baseline's length, still adds an experiment, and calls the 2014 shelter study a "hospital shelter" study.
- **T8 — no real change.** It still opens with "a circle is the only shape" and corrects that in a side note about Reuleaux triangles. Still long for a one-paragraph question.

## What is still open

1. **Length on simple prompts.** Removing the template cut length by 3–34%, but T3 and T8 are still longer than the baseline. The skill has no length target for default answers beyond "two to four paragraphs".
2. **Unneeded browsing (T17).** One instance; rerun to see whether it repeats before changing the research rules.
3. **Rerun all 22 tests** to check that the change did not hurt the tests where v2 headings were useful (T13 deep dive).
