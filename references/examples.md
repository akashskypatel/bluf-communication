# BLUF transformations

All scenarios below are **fictional illustrations**, not verified results from any actual repository or incident.

## Engineering status

**Before:** “We updated the build script, checked a few logs, and talked about the deployment. There are still two failures in the integration suite.”

**After:** “The release is blocked: two integration tests still fail. The build-script change is complete, but no deployment is authorized until the failing tests are resolved or explicitly dispositioned.”

Why it works: reader sees outcome and blocker before activity history; it does not claim a root cause.

## Decision request

**Before:** “There are several approaches for caching. We compared memory use, rollout complexity, and latency. I think option B makes sense. Can you review?”

**After:** “Recommendation: approve option B for the cache rollout because it limits migration risk. The main tradeoff is higher memory use; the decision is pending review.”

Why it works: proposes a concrete choice and names the key tradeoff without implying approval.

## Incident notification

**Before:** “At the start of the shift we noticed some alerts and began checking system graphs. Requests are failing in one zone, but we haven't verified the cause.”

**After:** “Requests in one zone are failing; root cause is not yet verified. The team is investigating the affected path, and no recovery has been confirmed.”

Why it works: observed impact and uncertainty come before investigative history.

## Handoff

**Before:** “We looked at the new parsing code and ran a few experiments. The failing input is attached. We need someone to look at the bounds check.”

**After:** “Next action: inspect the parser bounds check against the attached failing input. The defect is reproduced, but the cause and fix remain unverified.”

Why it works: the next operator knows what to do and which claims are actually established.

## Code-review finding

**Before:** “I reviewed `loadConfig()` and noticed that the path comes from a request field. There's a helper later that reads it.”

**After:** “Block merge until `loadConfig()` validates the request-controlled path before opening the file. The current code permits paths outside the intended configuration directory.”

Why it works: states the requested change and the security consequence first. The example presumes that this issue has been independently confirmed.

## Unknown result

**Before:** “We tried changing several settings, and the numbers look different. Maybe this fixed it.”

**After:** “The performance change is unverified; existing measurements are not comparable. Re-run the benchmark with a consistent workload before attributing any improvement to the setting.”

Why it works: it gives a useful bottom line without manufacturing a result.
