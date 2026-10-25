# Key Frameworks for the AIGP Exam

Short study summaries. Laws and standards change, so check official sources for exact wording and dates.

---

## EU AI Act (Regulation (EU) 2024/1689)

**What it is:** The first broad, binding AI law. Uses a risk-based approach. Applies to anyone placing AI on the EU market or whose AI output is used in the EU.

**Risk tiers**
- **Prohibited:** practices seen as unacceptable, such as social scoring, manipulative techniques that cause harm, and certain uses of biometrics.
- **High risk:** AI that is a safety component of regulated products, or used in listed sensitive areas (for example employment, education, credit, essential services, law enforcement, migration, justice, critical infrastructure).
- **Limited risk:** transparency duties, such as telling people they are talking to a chatbot and labeling deepfakes or AI-generated content.
- **Minimal risk:** no specific duties; voluntary codes encouraged.

**Main roles:** provider, deployer, importer, distributor. Providers carry the heaviest duties. A deployer or other party can become a provider, for example by putting its own name on a system or making a substantial change.

**High-risk provider duties (main themes):** risk management system, data governance, technical documentation, logging, instructions for use, human oversight, accuracy and robustness and cybersecurity, quality management system, conformity assessment, registration, post-market monitoring, serious incident reporting.

**High-risk deployer duties (main themes):** use as instructed, assign trained human oversight, monitor and report problems, keep logs, inform affected people where required. Some deployers (such as public bodies and certain credit or insurance uses) must do a fundamental rights impact assessment.

**General-purpose AI (GPAI) models:** providers must keep technical documentation, share information with downstream providers, have a copyright policy, and publish a summary of training content. Models with systemic risk have extra duties such as evaluations, adversarial testing, incident reporting and cybersecurity.

**AI literacy:** providers and deployers must take steps to give staff enough AI knowledge.

**Enforcement:** national authorities plus the EU AI Office (especially for GPAI). Fines are tiered, with the highest tier for prohibited practices.

**Timeline:** applies in stages. Prohibitions and AI literacy came first, then GPAI rules, then most high-risk rules. The Digital Omnibus proposals (late 2025) aim to delay some high-risk dates. Check the current status before relying on any date.

---

## NIST AI Risk Management Framework (AI RMF 1.0)

**What it is:** Voluntary US framework for managing AI risk. Sector neutral and not a law. Comes with a Playbook of suggested actions.

**Trustworthy AI characteristics:** valid and reliable; safe; secure and resilient; accountable and transparent; explainable and interpretable; privacy-enhanced; fair with harmful bias managed.

**Four core functions**
- **Govern:** culture, policies, roles and accountability. Cross-cutting; supports the other three.
- **Map:** understand context, purpose, stakeholders and possible impacts.
- **Measure:** assess, test and track risks with methods and metrics.
- **Manage:** prioritize and treat risks, respond to incidents, monitor over time.

Each function splits into categories and subcategories. **Profiles** tailor the framework to a use case or sector. NIST has also published a Generative AI Profile.

**Exam angle:** know which function an activity belongs to. Example: setting up an AI risk committee is Govern; testing for bias is Measure.

---

## ISO/IEC 42001 (AI management system)

**What it is:** International standard for an AI Management System (AIMS). Certifiable, like ISO 27001 for security.

**Structure:** the common ISO management system clauses (context, leadership, planning, support, operation, performance evaluation, improvement) using Plan-Do-Check-Act.

**Key parts**
- AI policy and objectives
- AI risk assessment and risk treatment
- AI system impact assessment
- Annex A reference controls and Annex B implementation guidance
- Statement of Applicability
- Internal audit, management review, continual improvement

**Exam angle:** it is about the organization's management system, not one model. It fits well with ISO 27001 and ISO 27701.

---

## ISO/IEC 42005 (AI system impact assessment)

**What it is:** Guidance on how to assess the impact of an AI system on individuals, groups and society. Not a certifiable standard.

**Key ideas**
- When to do an assessment and when to repeat it (for example, after major changes)
- What to cover: intended use, foreseeable misuse, affected people, benefits and harms
- How to document results and link them to risk management
- Supports the impact assessment step in ISO/IEC 42001

**Related:** ISO/IEC 22989 gives AI concepts and terminology. ISO/IEC 23894 gives AI risk management guidance.

---

## OECD AI Principles

**What they are:** The first intergovernmental AI standard, adopted in 2019 and updated in 2024. Non-binding but very influential. The OECD AI system definition shaped later laws, including the EU AI Act.

**Five values-based principles**
1. Inclusive growth, sustainable development and well-being
2. Human rights and democratic values, including fairness and privacy
3. Transparency and explainability
4. Robustness, security and safety
5. Accountability

**Five recommendations for governments:** invest in AI research; build an inclusive AI ecosystem; create an enabling and interoperable policy environment; build human skills and support workers through change; cooperate internationally.

**Also useful:** the OECD framework for classifying AI systems, which looks at people and planet, economic context, data and input, the AI model, and task and output.

---

## GDPR and automated decision-making

**Core rule:** people have the right not to be subject to a decision based solely on automated processing (including profiling) that has legal or similarly significant effects on them.

**Allowed only when:** necessary for a contract, authorized by law with safeguards, or based on explicit consent.

**Safeguards:** right to human intervention, to express a view, and to contest the decision. Stricter limits apply when special category data is used.

**Transparency:** people must be told about such decisions and given meaningful information about the logic involved and the likely consequences.

**Related duties**
- Data protection impact assessment (DPIA) for high-risk processing, which is common with AI
- Lawful basis, purpose limitation, data minimization, privacy by design
- Data subject rights (access, correction, erasure, objection)

**Case law to know:** the CJEU SCHUFA ruling (2023) found that a credit score can itself count as an automated decision when a lender relies heavily on it.

**Exam angle:** "solely automated" is key. Real, meaningful human review can take a decision outside the rule. A rubber-stamp review does not.
