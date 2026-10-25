# AIGP Exam Coach

A Claude skill that helps you prepare for the **IAPP AIGP (Artificial Intelligence Governance Professional)** exam, based on Body of Knowledge v2.1.

## What it does

| Mode | What you get |
|---|---|
| **Explain** | Plain-language explanation of any AIGP topic, with an example and the exam angle |
| **Quiz** | Original scenario-based questions (A to D), one at a time, with feedback on every option and the BoK domain |
| **Study plan** | A week-by-week plan based on your exam date, time and background |
| **Weak area review** | Focused review and practice on the domains where you score lowest |

## Practice exams

Browser-based mock exams that work like the real test: 100 questions, a 180-minute timer, an optional 15-minute break after question 50, flag for review, and a review screen. At the end you get a score report against an 80% readiness target, a breakdown by BoK domain, and the topics to study next.

| Level | Exams |
|---|---|
| Easy | [Easy Exam 1](practice-exams/easy-1/index.html) |
| Medium | Coming soon |
| Hard | [Hard Exam 1](practice-exams/hard-1/index.html) |

**Open them:** start at [practice-exams/index.html](practice-exams/index.html). Download the repo and open it in any browser, or use GitHub Pages (see below).

## Structure

```
aigp-exam-coach/
├── SKILL.md
└── references/
    ├── domains.md          # The 4 domains, question ranges and topics
    ├── key-frameworks.md   # EU AI Act, NIST AI RMF, ISO/IEC 42001 and 42005, OECD, GDPR automated decisions
    └── exam-tips.md        # Exam format, answering strategy, study tips
practice-exams/
├── index.html              # Landing page listing every exam by level
├── easy-1/index.html       # One self-contained exam per folder
└── _build/                 # Template, question data and build script
```

## Install

**Claude apps:** Download this repo as a zip, then upload the `aigp-exam-coach` folder (zipped) under Settings > Capabilities > Skills.

**Claude Code:** Copy the `aigp-exam-coach` folder into `~/.claude/skills/`.

Then try: *"Quiz me on AIGP Domain II"* or *"Make me an AIGP study plan."*

**Practice exam online:** in this repo go to Settings > Pages, set the source to the `main` branch and `/ (root)`, then open `https://<your-username>.github.io/aigp-exam-coach/practice-exams/`.

**Adding an exam:** save the questions as `practice-exams/_build/data/<level>-<n>.json`, add a line to `practice-exams/_build/exams.json`, then run `python3 practice-exams/_build/build.py`. Exams are named by level and number, for example Easy Exam 1, Medium Exam 1, Hard Exam 2.

## Disclaimer

- This is an independent study aid. It is not affiliated with or endorsed by the IAPP.
- The skill files are original content. The practice exam questions come from third-party practice sets. They are not official IAPP exam or practice questions.
- Domain tags on practice exam questions are mapped by hand to BoK v2.1 and are estimates.
- A few practice questions may be outdated (for example, references to US Executive Order 14110, which was revoked in January 2025). Check anything doubtful against current sources.
- Laws and standards change. Always check the official AIGP Body of Knowledge at [iapp.org](https://iapp.org/certify/aigp/).
- Not legal advice.

## License

MIT, for the skill files and the practice exam interface code. The practice exam questions are third-party content and are not covered by this license.
