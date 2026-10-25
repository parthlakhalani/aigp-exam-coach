# AIGP Domains (Body of Knowledge v2.1)

The exam has 100 questions: 85 scored and 15 unscored. The ranges below are scored questions per domain and competency. Always confirm against the current BoK on iapp.org.

| Domain | Focus | Questions |
|---|---|---|
| I | Foundations of AI governance | 16 to 20 |
| II | How laws, standards and frameworks apply to AI | 19 to 23 |
| III | Governing AI development | 21 to 25 |
| IV | Governing AI deployment and use | 21 to 25 |

Domains III and IV together are about half the exam.

---

## Domain I: Foundations of AI governance (16 to 20)

What AI governance is and how to build a program, for any industry or company size.

**I.A What AI is and why it needs governance (4 to 6)**
- Common definitions and types of AI
- Risks and harms to individuals, groups, organizations and society (bias, misalignment, scale)
- What makes AI different: complexity, opacity, autonomy, speed and scale, data dependency, probabilistic outputs
- Responsible AI principles: fairness, safety, privacy, security, transparency, explainability, accountability, human focus

**I.B Setting expectations for AI governance (5 to 7)**
- Roles and responsibilities for governance stakeholders
- Cross-functional teams and diverse expertise
- Training and awareness for all staff
- Fitting governance to company size, maturity, sector, products and risk appetite
- How developers, providers, deployers and users differ in duties

**I.C Policies across the AI life cycle (6 to 8)**
- Oversight and accountability policies for every stage: use case review, risk management, ethics by design, data, development, testing, deployment, monitoring, documentation, incidents
- Updating existing policies (privacy, security, data governance, IP) for AI
- Third-party risk: procurement, supply chain, HR, acceptable use, contracts

---

## Domain II: Laws, standards and frameworks (19 to 23)

Existing laws that touch AI, plus AI-specific laws and standards.

**II.A Data privacy laws applied to AI (4 to 6)**
- Transparency, choice, lawful basis, purpose limitation
- Data minimization and privacy by design
- Controller duties: impact assessments, processors, cross-border transfers, data subject rights, automated decision-making, breaches, records
- Sensitive and special category data (for example, biometrics)

**II.B Other existing laws applied to AI (4 to 6)**
- Intellectual property (training data use, ownership of outputs)
- Non-discrimination (employment, credit, housing, insurance)
- Consumer protection (unfair or deceptive practices)
- Product liability (design and manufacturing defects)

**II.C AI-specific laws (5 to 7)**
- Risk tiers (prohibited, high, limited, minimal) and what falls in each
- Requirements: risk management, data governance, technical documentation, conformity and impact assessments, record keeping
- Human oversight, transparency, notification, quality management
- General-purpose AI model rules
- Enforcement and penalties
- Different duties for providers, deployers, importers and distributors
- Examples named in the BoK: EU AI Act, South Korea AI Basic Act, US federal and state AI laws for the private sector

**II.D Standards and tools (4 to 6)**
- OECD AI Principles and related guidance
- NIST AI RMF and Playbook (functions, categories, subcategories)
- Core ISO standards: ISO/IEC 22989, 42001, 42005

---

## Domain III: Governing AI development (21 to 25)

Duties when designing, building, training, testing and maintaining AI.

**III.A Design and build (6 to 8)**
- Define business context and use case
- Perform or review an impact assessment
- Apply policies and ethics to design choices (purpose, requirements, model choice, human oversight, metrics and thresholds, stakeholder input)
- Identify and manage risks (harm matrix, mitigation hierarchy, stakeholder mapping, benchmarking, pilots)
- Document the design and build process

**III.B Data for training and testing (6 to 8)**
- Data governance: lawful right to use data, quality, quantity, integrity, fit for purpose
- Data lineage and provenance
- Plan and run tests: unit, integration, validation, performance, security, bias, interpretability
- Manage issues found during training and testing
- Document the process

**III.C Release, monitoring and maintenance (8 to 10)**
- Release readiness (model cards, conformity requirements)
- Continuous monitoring and a schedule for updates and retraining
- Periodic checks: audits, red teaming, threat modeling, security testing
- Manage and document incidents
- Understand why incidents happen (brittleness, poor data, weak testing, drift)
- Public disclosures (technical documentation, instructions for deployers, post-market monitoring plans)

---

## Domain IV: Governing AI deployment and use (21 to 25)

Choosing a model, then deploying and using it responsibly. Applies to in-house and third-party models.

**IV.A Deciding to deploy (6 to 8)**
- Use case context: objectives, performance needs, data, ethics, workforce readiness
- Model types: classic vs generative, proprietary vs open source, small vs large, language vs multimodal
- Deployment options: cloud, on-premise, edge; as-is, fine-tuning, RAG, agentic setups

**IV.B Assessing the AI system (5 to 7)**
- Perform or review an impact assessment on the chosen system
- Key terms and risks in vendor and licensing agreements
- Extra duties and liability when deploying your own proprietary model

**IV.C Governing deployment and use (9 to 11)**
- Apply policies to deployment (data governance, risk, issues, user training)
- Continuous monitoring, maintenance, updates, retraining
- Periodic checks: audits, red teaming, threat modeling, security testing
- Document incidents, risks and post-market monitoring
- Prevent secondary uses and downstream harms
- External communication plans
- Policy and controls to switch off or localize a system when needed

---

## Quick mapping tips

- "Who must do this?" questions usually test role differences (I.B, II.C).
- "What should happen first?" questions usually test life cycle order (I.C, III, IV).
- IV.C is the largest single competency. Monitoring, incidents and shutdown controls matter.
