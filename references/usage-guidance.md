# Composition guidance

## Pick the correct bottom line

| Reader's need | Lead with | Then provide |
| --- | --- | --- |
| Know what happened | Current outcome and practical impact | Decisive evidence, scope, gaps |
| Approve or decide | Specific option and decision sought | Reason, tradeoffs, alternatives, deadline if known |
| Act on a blocker | Blocker, impact, and needed action | Evidence, attempted workarounds, dependencies |
| Monitor an incident | Observed impact and mitigation state | Scope/timeline, current evidence, unknowns, next update if known |
| Review work | Verdict or highest-priority finding | Reproduction, impact, required change |
| Resume an investigation | Verified current state and next owner/action | What is ruled out, artifacts, remaining gaps |

## Bottom-line composition

Prefer this mental model (not required literal headings):

**Outcome / recommendation / action** + **relevant scope or consequence** + **important qualification (if needed)**.

A single sentence is a useful default but not a hard cap. When the truth needs a qualification, include it in the lead or immediately after it.

Weak: “We spent the day reviewing the service and are still discussing the release.”

Strong: “Release remains blocked by an unresolved startup failure; the investigation has not yet established a root cause.”

These are examples of wording, not claims about a live system.

## Evidence and uncertainty

- Separate observations from interpretations: “The health check failed” is not the same as “the database caused the failure.”
- Preserve failed tests and incomplete verification. Do not convert “not reproduced” to “fixed,” or “build passed” to “all tests passed.”
- Distinguish planned actions from completed actions. The requested approval is not an approved decision.
- Include evidence links when available; omit unverified identifiers and do not invent citations.
- Use chronology only when the sequence explains impact, causality, or what action is needed.

## BLUF and neighboring structures

BLUF specifies **where the main point appears**. It does not prescribe the rest of the message. SBAR specifies **which four categories to cover**. If both are requested, lead with a compact outcome or ask and then retain SBAR sections without repeating the same material unnecessarily.

An executive summary can be longer than the opening BLUF. A technical root-cause report can still retain evidence, trace detail, and methodology after its top-line finding. When the user expressly requests a chronological narrative, legal/academic structure, a structured schema, or raw diagnostic output, preserve that requirement instead of reordering material mechanically.

## Final review rubric

1. The first sentence states the most useful outcome, status, recommendation, or request.
2. It names the important scope/impact without unsupported certainty.
3. The following details directly support the opening assertion.
4. Uncertainty, failure, conditions, and significant counterevidence are visible.
5. Any action requested is specific enough for its intended reader.
6. A reader can skim without losing the central point; deeper technical readers can trace the evidence.
