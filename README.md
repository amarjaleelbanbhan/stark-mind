# Stark Mind

A reusable AI skill for turning observations into understanding.

## The Problem

When presented with casual observations, questions, or random curiosities, general-purpose large language models tend toward predictable failure modes:
- **Excessive verbosity**: Generating multi-paragraph essays or unprompted action plans when a simple, direct explanation was all that was needed.
- **Superficial breadth**: Listing half a dozen shallow analogies across random fields without explaining why the analogies hold or where they break down.
- **Flattery and praise**: Labeling ordinary questions "brilliant" or "profound" instead of engaging directly with the substance.
- **Premature project-ification**: Turning every observation into a business idea, software tool, or productivity task.

Stark Mind guides models toward concise, evidence-aware, cross-disciplinary exploration that prioritizes clarity, intellectual honesty, and accurate mental models.

## What the Skill Does

Stark Mind structures interactions around a 6-step exploration process:

1. **Understand**: Clarify the core observation and separate observed facts from interpretations.
2. **Explain, then look wider**: Start with the simplest accurate mechanism before exploring relevant alternative angles.
3. **Ask better questions**: Uncover hidden constraints, trade-offs, feedback loops, and edge cases (with a ceiling of at most one follow-up question).
4. **Connect ideas**: Identify cross-disciplinary connections only when they genuinely illuminate the subject, explicitly stating where analogies stop being useful.
5. **Find a useful takeaway**: Provide a memorable mental model or principle without forcing unneeded action items or projects.
6. **Connect to goals**: Relate insights to the user's stated goals only when a genuine, non-trivial connection exists.

### Depth Calibration

The skill supports user-controlled depth:
- **Quick (`quick`, `tldr`, `in a sentence`)**: 1–3 sentences focusing strictly on the core mechanism, omitting follow-up questions and practical exercises.
- **Default (unspecified)**: A focused 2–4 paragraph exploration with at most one targeted follow-up question.
- **Deep dive (`deep dive`, `go deeper`, `explain fully`)**: Detailed breakdown exploring multiple angles, underlying evidence, and practical experiments.

## Quick Example

**User input:**
> "A restaurant owner remembers what regular customers usually order."

**Stark Mind response summary:**
- **Mechanism:** Explains how recognition makes people feel understood and reduces cognitive friction during ordering.
- **Cross-disciplinary bridge:** Draws a connection to personalization in software systems and user preferences in AI agents.
- **Trade-offs and limits:** Highlights the boundary between helpful memory and intrusive tracking, noting where the analogy diverges (social reciprocity versus algorithmic profiling).
- **Takeaway:** Good personalization reduces friction while leaving people in control of what is remembered.
- **No forced agenda:** Explores the idea on its merits without telling the user to build a restaurant CRM or launch a startup.

## Installation

Stark Mind follows the open skill standard (`SKILL.md` with YAML frontmatter) and can be used across multiple AI coding assistants, chat interfaces, and agent environments.

### Claude Code / Codex CLI / AGY
Copy the skill folder into your agent's skill directory:
- **Claude Code:** `.claude/skills/stark-mind/`
- **Codex CLI:** `.codex/skills/stark-mind/`
- **AGY:** `.agents/skills/stark-mind/`

The environment will detect the skill definition and activate it via progressive disclosure when relevant questions or observations arise.

### Claude.ai Projects
1. Open your Claude.ai Project.
2. Under **Project Knowledge**, upload [`SKILL.md`](file:///d:/skill/Stark%20Mind%20skill/SKILL.md).
3. The skill rules will apply across conversations within that project.

### ChatGPT Custom GPTs
1. Go to the **GPT Builder** and navigate to the **Configure** tab.
2. Paste the contents of [`SKILL.md`](file:///d:/skill/Stark%20Mind%20skill/SKILL.md) into the **Instructions** field (condensing if nearing the 8,000-character limit), or upload [`SKILL.md`](file:///d:/skill/Stark%20Mind%20skill/SKILL.md) under **Knowledge**.

### ChatGPT Custom Instructions
ChatGPT Custom Instructions enforce strict character limits (1,500 characters on Free/Go; 5,000 characters on Plus/Pro/Team). The full skill file exceeds the standard limit. You can:
- Paste the **Purpose** and **Core process** sections into the "How would you like ChatGPT to respond?" field.
- A dedicated condensed version optimized for character-constrained fields is planned for a future release.

### Other Assistants and System Prompts
Copy the contents of [`SKILL.md`](file:///d:/skill/Stark%20Mind%20skill/SKILL.md) directly into your assistant's system prompt or custom instructions field.

## Evaluation

The repository includes an evaluation suite in [`evaluation/test_cases.md`](file:///d:/skill/Stark%20Mind%20skill/evaluation/test_cases.md). It contains:
- **12 test scenarios (T1–T12)** targeting specific failure modes such as forced analogies, unnecessary web research, failure to adhere to brevity constraints, and hallucinated mechanisms.
- **An 8-dimension scoring rubric** covering factual reliability, reasoning quality, connection relevance, uncertainty calibration, conciseness, learning value, respect for user intent, and appropriate tool use.
- **A comparative testing methodology** for evaluating baseline versus modified skill revisions.

## Limitations

- **Prompt-level instruction**: Stark Mind is a system prompt instruction, not a fine-tuned model or dedicated agent runtime. Output quality depends entirely on the reasoning and instruction-following capabilities of the underlying base model.
- **Platform dependency for memory**: Cumulative learning across sessions relies on external memory features (such as Claude Projects, ChatGPT memory, or agent artifacts). On stateless platforms, each conversation starts fresh.
- **Analogy guardrails are imperfect**: While the skill explicitly instructs models to limit analogies and state where comparisons break down, underlying LLMs may still occasionally suggest tenuous connections.
- **No scientific learning validation**: The skill has not been scientifically validated through formal educational outcome studies. It is designed to mitigate known behavioral failure modes in conversational LLMs.
- **Context token overhead**: The complete skill consumes approximately 3,100 tokens of context window space.

## License

Stark Mind is licensed under the [MIT License](LICENSE). See [`LICENSE`](file:///d:/skill/Stark%20Mind%20skill/LICENSE) for the full text.

## Contributing

Contributions, bug reports, and suggestions are welcome:
- When proposing modifications to prompt instructions, keep changes focused and minimal to conserve token overhead.
- Test proposed changes against the scenarios in [`evaluation/test_cases.md`](file:///d:/skill/Stark%20Mind%20skill/evaluation/test_cases.md) to ensure existing guardrails and calibration behaviors are preserved.
- Open an issue or pull request with your findings and rationale.
