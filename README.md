# AIGP Exam Coach

A Claude skill that helps you prepare for the **IAPP AIGP (Artificial Intelligence Governance Professional)** exam, based on Body of Knowledge v2.1.

## What it does

| Mode | What you get |
|---|---|
| **Explain** | Plain-language explanation of any AIGP topic, with an example and the exam angle |
| **Quiz** | Original scenario-based questions (A to D), one at a time, with feedback on every option and the BoK domain |
| **Study plan** | A week-by-week plan based on your exam date, time and background |
| **Weak area review** | Focused review and practice on the domains where you score lowest |

## Structure

```
aigp-exam-coach/
├── SKILL.md
└── references/
    ├── domains.md          # The 4 domains, question ranges and topics
    ├── key-frameworks.md   # EU AI Act, NIST AI RMF, ISO/IEC 42001 and 42005, OECD, GDPR automated decisions
    └── exam-tips.md        # Exam format, answering strategy, study tips
```

## Install

**Claude apps:** Download this repo as a zip, then upload the `aigp-exam-coach` folder (zipped) under Settings > Capabilities > Skills.

**Claude Code:** Copy the `aigp-exam-coach` folder into `~/.claude/skills/`.

Then try: *"Quiz me on AIGP Domain II"* or *"Make me an AIGP study plan."*

## Disclaimer

- This is an independent study aid. It is not affiliated with or endorsed by the IAPP.
- All content is original. It does not contain official IAPP exam or practice questions.
- Laws and standards change. Always check the official AIGP Body of Knowledge at [iapp.org](https://iapp.org/certify/aigp/).
- Not legal advice.

## License

MIT
