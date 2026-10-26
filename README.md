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

**Start here:** [https://parthlakhalani.github.io/aigp-exam-coach/practice-exams/](https://parthlakhalani.github.io/aigp-exam-coach/practice-exams/)

| Level | Exam | Direct link |
|---|---|---|
| Easy | Easy Exam | [Easy 1](https://parthlakhalani.github.io/aigp-exam-coach/practice-exams/easy-1/), [Easy 2](https://parthlakhalani.github.io/aigp-exam-coach/practice-exams/easy-2/), [Easy 3](https://parthlakhalani.github.io/aigp-exam-coach/practice-exams/easy-3/), [Easy 4](https://parthlakhalani.github.io/aigp-exam-coach/practice-exams/easy-4/), [Easy 5](https://parthlakhalani.github.io/aigp-exam-coach/practice-exams/easy-5/), [Easy 6](https://parthlakhalani.github.io/aigp-exam-coach/practice-exams/easy-6/) |
| Medium | Medium Exam | [Medium 1](https://parthlakhalani.github.io/aigp-exam-coach/practice-exams/medium-1/) |
| Hard | Hard Exam | [Hard 1](https://parthlakhalani.github.io/aigp-exam-coach/practice-exams/hard-1/) |

The links work once GitHub Pages is turned on for this repo (see below). You can also download the repo and open `practice-exams/index.html` in any browser.

## Structure

```
aigp-exam-coach/
├── SKILL.md
└── references/
    ├── domains.md          # The 4 domains, question ranges and topics
    ├── key-frameworks.md   # EU AI Act, NIST AI RMF, ISO/IEC 42001 and 42005, OECD, GDPR automated decisions
    └── exam-tips.md        # Exam format, answering strategy, study tips
aigp-exam-coach.zip         # Ready-to-upload skill package
practice-exams/
├── index.html              # Landing page listing every exam by level
├── easy-1/index.html       # One self-contained exam per folder
└── _build/                 # Template, question data and build script
```

## Install

**Claude apps (web, desktop):**
1. Download [aigp-exam-coach.zip](https://github.com/parthlakhalani/aigp-exam-coach/raw/main/aigp-exam-coach.zip). Do not unzip it.
2. Make sure **Settings > Capabilities > Create and edit files** is turned on.
3. Go to **Customize > Skills**, click **+**, then **Create skill > Upload a skill**, and choose the zip.
4. Turn the skill on in your skills list.

On Team and Enterprise plans, an owner may need to allow custom skills first.

**Claude Code:** Copy the `aigp-exam-coach` folder into `~/.claude/skills/`.

**Try it:** start a new chat and ask *"Quiz me on AIGP Domain II"*, *"Explain the EU AI Act risk tiers"* or *"Make me an AIGP study plan."*

**Practice exam online:** in this repo go to Settings > Pages, set the source to the `main` branch and `/ (root)`, then open `https://<your-username>.github.io/aigp-exam-coach/practice-exams/`.

**Adding an exam:** save the questions as `practice-exams/_build/data/<level>-<n>.json`, add a line to `practice-exams/_build/exams.json`, then run `python3 practice-exams/_build/build.py`. Exams are named by level and number, for example Easy Exam 1, Medium Exam 1, Hard Exam 2.

## Disclaimer

- This is an independent study aid. It is not affiliated with or endorsed by the IAPP.
- The skill files and Medium Exam 1 are original content. The Easy Exam 1 to 6 and Hard Exam 1 questions come from third-party practice sets. Some of their questions were reworded or corrected where the original answer was outdated or inaccurate. None are official IAPP exam or practice questions.
- Domain tags on practice exam questions are mapped by hand to BoK v2.1 and are estimates.
- A few practice questions may be outdated (for example, references to US Executive Order 14110, which was revoked in January 2025). Check anything doubtful against current sources.
- Laws and standards change. Always check the official AIGP Body of Knowledge at [iapp.org](https://iapp.org/certify/aigp/).
- Not legal advice.

## License

MIT, for the skill files, the practice exam interface code and the Medium Exam 1 questions. The Easy Exam 1 to 6 and Hard Exam 1 questions are third-party content and are not covered by this license.
