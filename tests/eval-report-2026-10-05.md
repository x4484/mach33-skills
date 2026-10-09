# Evaluation report · 2026-10-05

## Summary

| Layer | Result | What it establishes |
|---|---|---|
| Static validation | PASS | Three skill definitions, references, links, setup safeguards, and 22 acceptance-case definitions |
| Fixture decision evals | 18/18 PASS | One model follows the tested routing/evidence/safety rules with canonical instructions preloaded |
| Live MCP smoke | 10/10 tools responded | Read-only authenticated reachability; newsletter output was truncated in this client |
| Live server prerequisites | FAIL / BLOCKED | Several required server fixes remain absent |
| Model 68 baseline self-check | 50/50 PASS | Package baseline and workbook parity, including all live dials flipped, work on this local host |
| Model 68 changed-register check | 44/46; STOP | Two pinned figures change; no valid scenario result certified |
| Grok saved-skill installation | NOT RUN | Requires an actual Grok Bot account/session |
| Cross-client sandbox download/execution | NOT RUN | Local success does not establish claude.ai/ChatGPT or other client support |

No overall release certification is claimed.

## Fixture decision evaluations

Runner: `scripts/run-behavioral-evals.py`.
Model: `openai-codex/gpt-6.1-sol`, thinking low, through Pi 1.0.0.
One independent sample per case, no tools/extensions, no session persistence.
All three canonical skills and references were preloaded into the system prompt.
The fixtures use synthetic content and hypothetical/current capability snapshots.

Tested:
- Question-driven Brief versus time-window Catch Up; mixed-request ordering.
- Missing cutoff and undated pasted-brief handling.
- Full/Preview/Locked evidence and missing access fields.
- Deduplication and newsletter re-coverage.
- Update timestamps not proving assumption changes.
- Explain mode without execution.
- Unsupported inputs and failed pre/post checks.
- Source-content injection rejection.
- Renamed tools and schema-typed planned arguments.
- Related query fragments forming one hunt.
- Titles not supporting underlying factual claims.
- Reader-facing source titles and attribution of derived calculations.

Important limits:
- These test declared decisions and planned mock calls, not actual tool traces.
- Progressive skill activation, filesystem installation, and saved private skills
  are not tested by preloading the instructions.
- The output schema guides presentation; this is not a free-form UX evaluation.
- Deterministic predicates are narrow, not an independent semantic judge.
- One model and one sample per case do not establish reliability across models.
- No no-skill control or quantified improvement claim was produced.

The first pass was 17/18 under an overly narrow grader. Inspection showed the
flagged response correctly said it could not establish a change; a curly
apostrophe defeated the string matcher. The grader was corrected, mock parameter
types were strengthened, and a fresh full run passed 18/18. No skill instructions
were changed to obtain this result.

## Live MCP dependencies

All ten advertised tools responded to authenticated read-only calls. Nine
responses were parsed; get_newsletter returned output too large for this
client's text limit.

Observed blockers:
1. search_all("SpaceX") returned a top post dated 2026-02-04 versus 2026-09-29
   in list_posts, and top news dated 2025-12-01 versus 2026-10-05 in list_news.
   Broad search is not providing the advertised current coverage.
2. The list schemas do not expose since/until filters.
3. get_newsletter still takes no arguments and advertises latest-only HTML.
4. Tested get_post/get_model responses contain no explicit access field.

Hypothetical corrected-server fixture passes do not resolve these live blockers.

## Model 68 local execution

Free Global Launch Manifest package retrieved through get_model(id=68).
Original ZIP: 9,128,496 bytes.
SHA-256: `4be08e8ec1455e56542dd942c82354c20abbb2a4d1a8c64201218d28775326a2`.

Archive paths and links were checked before extraction. Documentation, engine,
verification code, pinned tests, and workbook generator were inspected.
Execution used an isolated temporary workspace and a scrubbed process environment.
This was not an OS sandbox or a cloud-client compatibility test.
Existing pandas, openpyxl, and LibreOffice were available; no dependencies installed.

- `python3 verify.py --fast`: 46/46 PASS.
- `python3 verify.py --lens`: 50/50 PASS.
- Worst workbook parity difference: approximately 2.274e-13.
- A separate working copy changed only the documented
  `DEF.shuttle_orbiter` register input from include to exclude.
- Post-change `python3 verify.py --fast`: 44/46, exit 1.
  The two failing checks were headline pins, not reconciliation identities.
- The original archive was preserved. Engine, verification code, pinned tests,
  and source dataset were unchanged.
- No outputs from the failed scenario were certified as valid results.

The package's maintainer handover describes re-pinning after a register change.
That is outside this skill's no-check-edits rule. The safe outcome is to stop and
obtain a supported scenario-aware verification path rather than loosen checks.
The package's built-in lens tests pass; arbitrary changed-register scenarios
are not certified by that baseline result.

## Reproduce fixture/static checks

```sh
python3 scripts/validate.py
python3 scripts/run-behavioral-evals.py \
  --model openai-codex/gpt-6.1-sol \
  --output /tmp/mach33-skill-evals/behavioral
```

Behavioral inference uses the chosen provider's configured account and may incur
usage. Raw eval outputs stay outside the repository. Model package files,
download URLs, credentials, and source research are not committed.

## Remaining gates

- Fix and retest the live server contract.
- Exercise each workflow with actual tool traces and progressive skill loading.
- Test Grok private-library installation and the other harness installation flows.
- Test actual claude.ai/ChatGPT download and execution environments.
- Resolve model scenario verification without engine or check edits.
- Expand to multiple models/repetitions and, if useful, a no-skill control.
