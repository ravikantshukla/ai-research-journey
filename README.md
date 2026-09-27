# ML Journey

A 156-week, 23-phase roadmap from the math behind neural networks to AI/ML research and AI safety research, learned in public.

- **Current phase:** 00 · Toolkit
- **Started:** 2026-09-28

## About me

Java Engineer → AI Researcher

Background: Software Engineer (Java/Spring Boot)
Goal: AI Researcher specializing in Indian Language NLP

## The mastery loop

For every topic:

**Learn → derive → implement → experiment → explain in my own words → connect to modern AI → test myself**

## Phases

| # | Phase | Status | Milestone project |
|---|---|---|---|
| 00 | [Toolkit](00-toolkit/) | ⬜ Not started | |
| 01 | [Linear Algebra](01-linear-algebra/) | ⬜ Not started | |
| 02 | [Calculus & Optimization](02-calculus-optimization/) | ⬜ Not started | |
| 03 | [Probability & Information Theory](03-probability-information-theory/) | ⬜ Not started | |
| 04 | [Statistics & Experimental Design](04-statistics-experimental-design/) | ⬜ Not started | |
| 05 | [Classical ML](05-classical-ml/) | ⬜ Not started | |
| 06 | [Deep Learning Foundations](06-deep-learning-foundations/) | ⬜ Not started | |
| 07 | [CNNs](07-cnns/) | ⬜ Not started | |
| 08 | [RNNs & LSTMs](08-rnn-lstm/) | ⬜ Not started | |
| 09 | [Transformers](09-transformers/) | ⬜ Not started | |
| 10 | [LLMs](10-llms/) | ⬜ Not started | |
| 11 | [Reinforcement Learning](11-reinforcement-learning/) | ⬜ Not started | |
| 12 | [Generative Models](12-generative-models/) | ⬜ Not started | |
| 13 | [Advanced ML Theory](13-advanced-ml-theory/) | ⬜ Not started | |
| 14 | [ML Engineering at Scale](14-ml-engineering-at-scale/) | ⬜ Not started | |
| 15 | [Research Methodology](15-research-methodology/) | ⬜ Not started | |
| 16 | [AI Safety Foundations](16-ai-safety-foundations/) | ⬜ Not started | |
| 17 | [Mechanistic Interpretability](17-mechanistic-interpretability/) | ⬜ Not started | |
| 18 | [Alignment & Oversight](18-alignment-oversight/) | ⬜ Not started | |
| 19 | [AI Evaluations](19-ai-evaluations/) | ⬜ Not started | |
| 20 | [AI Control](20-ai-control/) | ⬜ Not started | |
| 21 | [Advanced AI Safety](21-advanced-ai-safety/) | ⬜ Not started | |
| 22 | [Independent Research](22-independent-research/) | ⬜ Not started | |

Status: ⬜ Not started · 🟡 In progress · ✅ Done

## Repo layout

```
.
├── 00-toolkit/ … 22-independent-research/   # one folder per phase
│   ├── notes.md          # topics, milestone project, reflection
│   ├── exercises/        # code and notebooks
│   └── derivations/      # worked math
├── papers/               # one note per paper: YYYY-short-title.md
├── templates/
│   ├── topic-notes.md
│   ├── paper-notes.md
│   └── project-template/ # starter for milestone project repos
├── pyproject.toml
├── .editorconfig
├── .gitignore
└── LICENSE
```

## Conventions

- Commit prefixes: `feat:`, `fix:`, `exp:` (experiments), `docs:`, `refactor:`, `chore:`
- Label scratch work with a `scratch_` prefix or put it in an `exercises/scratch/` folder
- Clear notebook outputs before committing
- No data, checkpoints or secrets in Git
- Milestone projects live in their own repos, linked from the table above
