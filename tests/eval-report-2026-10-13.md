# Field-feedback update and evaluation · 2026-10-13

## Changes made

This update responds to two user-supplied October 12 field reports. Their findings
are reported observations, not independently reproduced live-server measurements.
The original feedback files and research content are not included in this repo.

- Skill descriptions now match delegated research, script fact-checking, chart
  numbers, quoted model figures and publication roundups.
- The harness guide supplies a parent/helper handoff rule and requires checking
  actual skill/reference reads. It does not modify any user's parent-agent config.
- Lookup guidance uses bounded short-keyword reformulation, live schema discovery,
  typed required arguments and omission of unset optional arguments. The argument
  examples are explicitly dated snapshots, not replacements for live schemas.
- Brief checks comparable units, prices, denominators, versions and scenarios in
  ordinary numerical comparisons. Comparison intent loads the historical reference;
  a publication date or the word “since” alone does not force a thesis comparison.
- Material quoted model figures are reconciled against accessible published model
  evidence where possible, without treating a quotation check as permission to run.
- All three skills finish with evidence/access/coverage checks. Catch Up requires
  fetched evidence for factual news summaries and dated links per development.
- Missing access stays unavailable; a fetched newsletter supports only facts in
  its readable body. Raw PDF/code noise is not evidence and is not repaired here.
- Event dates, publication dates, repeated coverage and referenced-but-unfound
  model artifacts are distinguished. Catalog absence is not universal nonexistence.
- Model Lab checks scope before downloading, discovers forward-model candidates
  without silently substituting them, preserves unknown register details as unknown,
  and offers named authorized attachments when appropriate. No-Compute output is
  short: explanation, why no rerun, next step.

Compute engine/check protections remain intact. No server, model package, pricing,
access control, production agent config or connector HTML was changed. Single-file
claude.ai packaging remains a separate compatibility task, not a new distribution.

## Evaluation results

| Layer | Result | Meaning |
|---|---|---|
| Static validation | PASS | Three skills, linked references, 38 acceptance definitions, 30 decision fixtures, public-pack hygiene |
| Offline grader canaries | 9/9 PASS | Required fields, optional null rejection, required news ID, pre-download scope, access and selected wording cases |
| GPT-6.1-sol full decision run | 30/30 PASS | Canonical skill bodies and references preloaded; one sample per case |
| GPT-6.1-sol final scope retest | 1/1 PASS | After clarifying that candidate discovery precedes substitution approval |
| GPT-5.5 targeted decision run | 9/10 after grader correction | Nine new cases plus the prior question-routing case; one planning omission remains |
| Progressive-loading traces | 4/4 PASS, manually reviewed | Real skill/reference and evidence-file reads in fresh Pi sessions, synthetic sources |
| Actual parent/helper deployment | NOT RUN | No Aaron/Jarvis or Research-agent configuration was changed or exercised |
| Live MCP and cloud-client reproduction | NOT RUN this round | No claim that server defects or claude.ai download/installation behavior were repaired |

Both models used thinking low through Pi 1.0.0. These small samples do not establish
cross-model reliability, installation certification or a quantified causal lift.

### Decision tests and grader limitations

New cases cover script/chart fact-checking, optional arguments, pre-download scope,
unknown register details, incompatible figures, unopened news, access per response,
quoted-model discrepancies, and partial pagination with corrupt summaries.

The first GPT-6.1 run scored 29/30 because the grader did not recognize “unresolved,
not evidence of a revision.” That response was correct; the matcher was amended
and a fresh full run passed 30/30. The final one-case scope rerun also passed.

GPT-5.5's first targeted run scored 7/10. Two findings were grader false negatives:
a refusal to state missing register values, and explicitly qualified discovery
metadata placed in the claims array without asserting the underlying news facts.
Matchers and canaries were corrected. A fresh targeted run scored 8/10; one was
another register wording false negative (“not documented there”). After correcting
that matcher, regrading the same saved outputs yields 9/10. This last step was
**regrading, not fresh inference**; original outputs/scores are preserved.

The remaining GPT-5.5 failure is narrow: it correctly rejected the historical
2027 forecast before downloading/executing and proposed finding a forward model,
but did not put a list_models call in its planned calls despite that mock capability
being available. This remains a failed planning assertion, not a fabricated rerun
or unsafe execution. Do not loosen the assertion to count it as a pass.

The grader now requires all top-level output fields/types, and checks required
arguments where fixtures declare them. This is limited hardening, not a full JSON
Schema implementation or an independent semantic judge. The checked-in canaries
cover only the listed cases; human review still matters.

### Progressive loading and larger retrieval

Runner: `scripts/run-workflow-traces.py`.

Unlike preloaded decision fixtures, these sessions see only skill descriptions
until the model reads the matching SKILL.md. Only the read tool is available;
there is no executable MCP, shell, write or package-download tool. The user task
points to synthetic evidence files, not private research.

1. **Simulated delegated script/chart task:** loaded Brief before evidence;
   rejected the claimed spectrum derivation while preserving the stated estimate.
2. **Historical comparison:** loaded Brief and comparing-research.md; distinguished
   $12 per watt from incremental +$4.9M NPV and did not manufacture a thesis change.
3. **Historical scope gate:** loaded Model Lab plus both mode references; explained
   why 2027 is outside a historical manifest and explicitly reported no rerun.
   It suggested a candidate without claiming discovery when no live tools existed.
4. **Larger catalog final check:** loaded Catch Up, read a 62-entry synthetic catalog,
   then both relevant news bodies. The answer had dated links and “access status
   unavailable,” excluded unrelated items, and did not turn filings into approvals.

The trace checks verify reads and selected answer indicators, not every claim.
All four final answers were also manually reviewed. These are single-turn helper
simulations and multiple file reads, not an actual parent agent's delegation policy
or a live paginated MCP stress test. The four traces preceded the final clarification
about read-only forward-model discovery; that clarification was retested separately
with the scope decision case.

## Reproduce

```sh
python3 scripts/validate.py
python3 -B tests/test_behavioral_grader.py
python3 scripts/run-behavioral-evals.py --model openai-codex/gpt-6.1-sol \
  --output /tmp/mach33-field-decisions
python3 scripts/run-workflow-traces.py --model openai-codex/gpt-6.1-sol \
  --output /tmp/mach33-field-traces
```

Model inference uses configured provider credentials and may incur usage. CI runs
only static checks and the offline canaries, not paid inference.
The decision fixture date remains October 5 for historical repeatability; the
progressive trace tasks have explicit synthetic dates and an October 13 context.

Local evidence: `/tmp/mach33-field-feedback-evals/` holds the original `gpt61/`,
`gpt61-final/`, `gpt61-scope-final/`, `gpt55/`, `gpt55-final/`, `traces/`, and separately
named `*-regraded.json` audits. Raw outputs are not committed.

## Follow-up boundaries

- Apply the reviewed parent/helper handoff rule in the actual agent deployments,
  with operator approval, then inspect both parent and helper traces.
- Reproduce relevance failures and corrupt summaries server-side; do not infer
  they are solved by short-query guidance or safe evidence handling.
- Verify any format access-field changes against live responses.
- Test claude.ai reference preservation and attachment/download compatibility.
  Do not create independently maintained flattened skill variants.
- Keep the scope gate and verification stops even when a weaker model omits a
  helpful discovery step. Investigate the GPT-5.5 planning omission separately.
