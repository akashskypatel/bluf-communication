---
name: bluf-communication
description: Draft, rewrite, summarize, or review professional and technical communications using Bottom Line Up Front (BLUF). Lead with the answer, recommendation, decision, current status, impact, or specific ask, then provide only supporting evidence and context. Use for engineering updates, incident notices, investigation reports, decision requests, code reviews, pull requests, handoffs, emails, and stakeholder briefs. Do not impose BLUF formatting on ordinary coding, exploratory analysis, or user-requested formats that require a different order.
---

# BLUF Communication

Put the **decision-relevant bottom line first** so a reader can understand the result or requested action without reading the background. Follow it with the essential support, caveats, and next step.

## Scope

Use this skill when the user wants to create, edit, compress, or evaluate a communication artifact, including a technical update, incident notice, issue summary, PR description, review finding, decision memo, handoff, or status report.

Do not apply a canned format to routine programming, debugging, research, or questions that are not requests for a communication artifact. Follow explicit audience, tone, medium, length, and format requirements. BLUF is an **ordering principle**, not a mandatory heading scheme.

## Procedure

1. **Determine audience and purpose.** Identify what the reader must *know*, *decide*, or *do*. Choose a bottom-line type: answer, result, recommendation, status/impact, decision, blocker, or request.
2. **Establish the verified conclusion.** Extract facts, sources, observed results, constraints, unknowns, and the intended action. Do not infer a successful build, test, deployment, root cause, decision, deadline, owner, or severity without evidence.
3. **Lead with the bottom line.** In the first sentence or short paragraph, state the outcome and its practical meaning. For an ask, name the specific action; for a status, name the current state and impact; for a recommendation, name the preferred option and main reason. Prefer one sentence; use two if needed for accuracy.
4. **Support in descending importance.** Follow with the decisive evidence, impact/rationale, major tradeoffs or uncertainties, and next action. Include dates, owners, dependencies, validation status, or links when supplied and relevant—not as boilerplate.
5. **Match the medium.** In chat, use one short lead plus a few sentences or bullets. In a decision request, make the choice and required approval unmistakable. In an incident update, lead with observed impact and current mitigation. In a technical handoff, lead with outcome/blocker and next executable responsibility. For longer reports, keep detailed reasoning, data, and chronology under the lead.
6. **Audit before delivery.** Confirm the lead answers the reader's primary question, its certainty matches the evidence, the body actually supports it, and unresolved risks/failures remain visible. Delete duplicated setup and nonessential chronology.

## Output rules

- **Do not bury the conclusion.** Avoid openings such as “This document discusses…”, “Some background…”, or long chronology before the point.
- **Do not overclaim.** Distinguish *verified*, *inferred*, *proposed*, and *unknown*. If the cause or answer is unresolved, lead with that state and the important next step instead of inventing certainty.
- **Be concrete.** Prefer “Release blocked: integration tests fail in the payment service” over “There are some release concerns,” when the evidence supports it.
- **Keep necessary nuance.** BLUF is not permission to omit counterevidence, limitations, safety constraints, or materially qualifying details.
- **Do not require the word `BLUF`.** Use a natural lead or a `Bottom line:` label if helpful. Preserve the user's requested document headings where possible.
- **No unsupported logistics.** Never invent owner, deadline, severity, metrics, actions already taken, test results, or promises of future work.
- **Produce the requested artifact.** If asked to draft or rewrite, return the complete usable message. If asked to assess, identify missing or misplaced bottom-line content and suggest an improved version when useful.

## Reusable resources

- [Usage and composition guidance](references/usage-guidance.md): choice of lead, exceptions, uncertainty, and interoperability with SBAR.
- [Before/after examples](references/examples.md): technical communications that demonstrate the transformation.
- Templates in `templates/`: `quick-update.md`, `decision-request.md`, `incident-update.md`, `engineering-handoff.md`, `review-finding.md`. Use only the template matching the requested artifact; do not inject empty or irrelevant sections.

## Quality gate

Before finalizing, ask: **If the reader stops after the first sentence, will they know the most important fact, result, or action—and will that statement still be accurate?** Then verify the body provides enough evidence to trust or act on it.
