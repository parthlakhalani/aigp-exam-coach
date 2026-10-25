# AIGP Exam Coach

A Claude skill that helps you prepare for the **IAPP AIGP (Artificial Intelligence Governance Professional)** exam, based on Body of Knowledge v2.1.

## What it does

| Mode | What you get |
|---|---|
| **Explain** | Plain-language explanation of any AIGP topic, with an example and the exam angle |
| **Quiz** | Original scenario-based questions (A to D), one at a time, with feedback on every option and the BoK domain |
| **Study plan** | A week-by-week plan based on your exam date, time and background |
| **Weak area review** | Focused review and practice on the domains where you score lowest |

## Practice exam

A browser-based mock exam that works like the real test: 100 questions, a 180-minute timer, an optional 15-minute break after question 50, flag for review, and a review screen.

At the end you get a score report against an 80% readiness target, a breakdown by BoK domain, and a list of the topics to study next, with links to the questions you missed.

**Open it:** [practice-exam/index.html](practice-exam/index.html). Download the file and open it in any browser, or use GitHub Pages (see below).

## Structure

```
aigp-exam-coach/
├── SKILL.md
└── references/
    ├── domains.md          # The 4 domains, question ranges and topics
    ├── key-frameworks.md   # EU AI Act, NIST AI RMF, ISO/IEC 42001 and 42005, OECD, GDPR automated decisions
    └── exam-tips.md        # Exam format, answering strategy, study tips
practice-exam/
└── index.html              # Self-contained mock exam (no install needed)
```

## Install

**Claude apps:** Download this repo as a zip, then upload the `aigp-exam-coach` folder (zipped) under Settings > Capabilities > Skills.

**Claude Code:** Copy the `aigp-exam-coach` folder into `~/.claude/skills/`.

Then try: *"Quiz me on AIGP Domain II"* or *"Make me an AIGP study plan."*

**Practice exam online:** in this repo go to Settings > Pages, set the source to the `main` branch and `/ (root)`, then open `https://<your-username>.github.io/aigp-exam-coach/practice-exam/`.

## Disclaimer

- This is an independent study aid. It is not affiliated with or endorsed by the IAPP.
- The skill files are original content. The practice exam questions come from a third-party practice set (Set 1). They are not official IAPP exam or practice questions.
- Domain tags on practice exam questions are mapped by hand to BoK v2.1 and are estimates.
- A few practice questions may be outdated (for example, references to US Executive Order 14110, which was revoked in January 2025). Check anything doubtful against current sources.
- Laws and standards change. Always check the official AIGP Body of Knowledge at [iapp.org](https://iapp.org/certify/aigp/).
- Not legal advice.

## License

MIT
