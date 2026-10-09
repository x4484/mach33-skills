# Skill-pack review and re-evaluation · 2026-10-09

## Podcast-coverage follow-up

After the review below, all three skills were updated with explicit podcast
discovery and fetched write-up evidence boundaries. Catch Up now checks the
podcast archive separately from broad aggregators and distinguishes a new
episode from an older event it re-covers. Brief and Model Lab can use relevant
episode write-ups without treating a video link as a transcript or execution.

Three fixture regressions were added: podcast-only-window discovery, fetch before
summary, and write-up-only re-coverage. Final runs:
- GPT-6.1-sol: **21/21** full-suite fixture decisions passed.
- GPT-5.5: **3/3** new podcast fixture decisions passed.
- Static validation and diff whitespace checks passed.

The first follow-up run scored 19/21. Manual inspection found two grader false
negatives: title-cased Full access and two coverage records sharing the same
event key, explicitly described as one development. Access comparison was made
case-insensitive and the duplicate case now checks distinct event identity.
A fresh full run produced the result above. These focused fixes do not resolve
the broader evaluator-hardening finding.

Evidence: private local `/tmp/mach33-podcast-evals/` (initial `gpt61/`,
final `gpt61-final/`, and `gpt55-podcasts/`). These are synthetic decisions,
not new live-server or harness-installation tests. No commit or release was made.
The review below records the pre-change state; finding 3 is addressed by this
follow-up, while its original test results remain unchanged.

## Verdict (pre-change review)

The main MCP retrieval defects reported on October 5 are fixed in the live
server. Brief, Catch Up and Model Lab Explain now work in fresh, authenticated
Pi sessions with progressive skill loading and actual tool calls.

This is not blanket release certification. Shared server instructions remain
incomplete, the pack needs explicit podcast coverage, the fixture grader needs
hardening, and Model 68 still cannot pass the tested changed-register check.
Six-harness installation and cloud-client Compute compatibility remain untested.

No canonical skill or reference was changed to obtain these results. No server,
engine, verification code, connector HTML or production configuration was changed.
Nothing was published, committed or pushed as part of this review.

## Findings, ordered by impact

### 1. Compute remains blocked by package verification, not MCP retrieval

**Boundary:** `skills/mach33-model-lab/SKILL.md:36–46` and
`skills/mach33-model-lab/references/compute-mode.md:39–47`.

The newly retrieved free Model 68 ZIP is byte-for-byte identical to the October 5
package. Baseline verification passes, but changing the documented Shuttle
orbiter input from `include` to `exclude` still fails two fixed headline pins.
The package handover instructs maintainers to re-pin; the skill correctly forbids
editing checks. Execution stopped. This is the expected safety behavior, not a
skill failure, but it blocks certifying that scenario.

**Needed:** a maintainer-supported scenario-verification command that checks the
requested input state while preserving original baseline pins and invariants.
Do not weaken the skill or infer that every possible scenario is broken from
this one failure. Do not advertise arbitrary Compute support from baseline success.

### 2. Universal evidence rules still are not in server instructions

**Contract:** `README.md`, Responsibility boundary and Server release prerequisites.

Live `initialize` reports server `33fg-research`, version `1.4.0`. Its instructions
list capabilities, recommend discovery before fetching, and request tabular list
output. They do not contain the agreed common rules for dated citations,
attribution, preview/locked evidence limits, incomplete coverage, source-content
injection, or retrieval versus execution.

Individual tool descriptions now document access and dates, and the installed
skills supplied good evidence discipline in the tests. That does not establish
the same behavior for a bare MCP connection without skills.

**Needed:** implement these rules server-side, then separately test a no-skill
client and how each harness exposes/consumes server instructions. Do not remove
the skill evidence protections before that contract is present and verified.

### 3. Publication discovery guidance is behind the new podcast capability

**Locations:** `skills/mach33-catch-up/SKILL.md:43–50`,
`skills/mach33-research-brief/SKILL.md:40–42`, and the acceptance fixtures.

The server now exposes 12 tools, including `list_podcasts` and `get_podcast`.
Catch Up explicitly enumerates posts, news, newsletters and models, but not
podcasts. Brief's discovery step enumerates posts, news and models. Neither
`search_all` nor `whats_new` includes podcasts or newsletters.

The tested all-format Catch Up recovered correctly through the live schemas and
retrieved the podcast. This is a documentation/coverage gap, not an observed
podcast omission in that run.

**Needed:** include relevant podcasts and newsletters in discovery guidance;
state both exclusions from the broad aggregators; add a podcast-only-window
regression case so older format enumerations cannot silently narrow coverage.

### 4. Fixture passes are useful but the grader can accept incomplete decisions

**Location:** `scripts/run-behavioral-evals.py:58–146` (existing uncommitted runner).

Four deliberately incomplete outputs were accepted by the current grader:

- Baseline failure: only `{"next_action":"stop"}`.
- Post-change failure: only `{"next_action":"stop"}`.
- Research routing: only `{"workflows":["brief"]}`.
- Title-only evidence: a planned `get_post` call with empty arguments.

Missing safety booleans are treated as false, and required tool arguments are
not validated. Some cases score routing but not the promised evidence behavior.
A passing decision fixture therefore is not proof of a valid executable plan.

A separate audit of all 54 completed outputs found the required output fields,
field types and required live-tool arguments present. The canaries do not
retroactively show those 54 outputs were malformed; they expose missing defenses
in the evaluator itself.

**Needed:** validate the entire output schema, required arguments, supported
parameter types and constraints; add failing-grader canaries; test references,
pagination, new formats and partial-tool failures through actual traces. Keep
behavioral assertions distinct from structural validation and semantic review.

### 5. One second-model plan violated optional-argument typing

**Case:** `routing-research-question`, GPT-5.5.

The response correctly chose Brief and withheld factual claims pending retrieval,
but planned `since: null` on three list calls. Both fixture and live schemas type
`since` as a string, not nullable. The grader correctly failed this case.

**Needed:** an explicit reminder to omit unset optional arguments, with regression
coverage. This was a planned-call failure, not an observed live server failure.
Do not loosen the grader to count it as a pass.

### 6. Installation portability remains a separate unverified claim

All six harness guides were reviewed for canonical-reference preservation,
non-overwrite behavior, native sign-in, separate MCP/skill checks and no model
execution during setup. The safeguards are present. The Pi skill location is
supported by the installed Pi documentation.

The live tests used an explicitly supplied skill directory in an isolated Pi
configuration. They establish native discovery/loading and live research use,
not that a pasted installation prompt works in a clean account or that
`~/.agents/skills/` installation was exercised. Grok private-library saving,
Claude Code, Codex, Hermes and OpenClaw setup were not executed. No claude.ai or
ChatGPT download/runtime test was run.

**Needed:** retain the unverified labels and run real installations before
claiming six-harness support. Prefer a reviewed version tag for distribution.

## Test results

| Layer | Result | Scope |
|---|---|---|
| Static pack validation | PASS | Three skills, relative references, 22 acceptance definitions, 18 fixture definitions, six guide review, hygiene |
| Live MCP API checks | 74/74 PASS | 58 smoke/contract assertions plus 16 edge assertions; all 12 tools called |
| Shared server instruction contract | INCOMPLETE | Required common evidence/safety rules absent from initialize instructions |
| GPT-6.1-sol fixtures, run 1 | 18/18 PASS | All canonical instructions preloaded; synthetic decisions |
| GPT-6.1-sol fixtures, run 2 | 18/18 PASS | Independent repeat, same model/settings |
| GPT-5.5 fixtures | 17/18 PASS | One invalid nullable-date plan |
| Claude Haiku 4.5 attempt | BLOCKED | Expired Anthropic OAuth refresh token; no usable samples |
| Additional required-field/argument audit | 54/54 PASS | Completed outputs only; does not erase the GPT-5.5 type failure |
| Grader negative canaries | 4 weaknesses reproduced | Deliberately incomplete responses incorrectly accepted |
| Native Pi Brief | PASS, reviewed trace | Skill loaded before discovery; fetched five selected substantive sources; no execution |
| Native Pi Catch Up | PASS, reviewed trace | Five format lists, pagination, historical issues, podcast, explicit access and scope |
| Native Pi Explain | PASS, reviewed trace | Skill plus Explain reference; model discovery and retrieval; no download/execution |
| Native Pi missing-baseline request | PASS, reviewed trace | Asked for briefing date/text; did not assume cross-session memory |
| Native Pi mixed digest/thesis comparison | PASS, reviewed trace | Both skills and comparison reference loaded; fetched both periods; distinguished unlike metrics from thesis changes |
| Model 68 baseline fast check | 46/46 PASS | Current downloaded package, local execution |
| Model 68 baseline lens/parity check | 50/50 PASS | Includes workbook parity with live dials flipped |
| Model 68 changed-register check | 44/46; STOP | Same two headline pins; no valid scenario result certified |
| Six clean harness installs / hosted runtimes | NOT RUN | Do not extrapolate from local Pi |

The 74 passing API assertions are a bounded black-box sample, not the server's
own unit/integration suite and not a pass on all release prerequisites.

## Live server verification

Endpoint: https://research.33fg.com/mcp.

Confirmed on this account:

- `search_all` returns the same five IDs, in the same order, as the corresponding
  post/news/model lists for SpaceX, orbital, Starship and an empty-result query.
- All five paginated list tools expose `since` and `until`, with documented
  inclusive boundaries and US Eastern interpretation. Date fields are publication
  date, sent date, or model update timestamp, as appropriate.
- Date-window bounds, newest-first ordering, empty future windows, same-day
  inclusion and page transitions pass for posts, news, models, newsletters and
  podcasts. The September 1–October 8 news window exhausts to 42 unique records
  across two pages.
- Model timestamp tests on either side of its update confirm Eastern-time
  interpretation for both `since` and `until`. Invalid dates and reversed windows
  return explicit errors rather than silent unfiltered/empty success.
- `get_newsletter(newsletter_id=60)` returns the requested historical issue;
  omitting the ID returns latest issue 61. Both bodies are readable Markdown,
  not HTML newsletters (7,473 and 9,744 characters respectively).
- Fetched post, podcast and model return explicit `access: full`.
  News/newsletters still have no access field; the skills correctly report that
  absence rather than guessing. Preview and locked responses were not live-tested
  with lower-entitlement accounts; they remain fixture coverage only.

The inherited MCP adapter in the parent session fails locally with a missing
`proxy-modes.ts` module before contacting the server. A direct authenticated,
read-only MCP client confirmed server behavior. Fresh native Pi sessions then
connected successfully using a temporary configuration containing only Mach33.
Existing production config and sign-in were not replaced.

An initial trace setup allowed only read/codemode and exposed no research tools
to the evaluated agent. Those runs are retained as setup-blocked evidence and
excluded from live-success counts. The corrected setup explicitly allowed the
12 read-only MCP tools and used direct exposure. No missing-tool run was called
a server regression or a completed research task.

## Native workflow evidence

Pi version: **1.0.0**. Model: `openai-codex/gpt-6.1-sol`, thinking low.
Each session began without prior conversation, with canonical skills discoverable
by name/description via `--skill`; full instructions were not preloaded.
Only read, codemode and the 12 read-only Mach33 tools were enabled. No shell,
write, edit, model-package execution or publication tool was available.

Observed:

- Brief read its skill, discovered sources, fetched posts and associated model
  write-ups, distinguished published estimates from commercial results and
  disclosed five-source scope. It made no calculation/execution claim.
- Catch Up covered September 28–October 8 in Eastern time: 4 posts, 28 news items,
  2 newsletters and 1 podcast, with zero separately indexed model updates.
  It exhausted both news pages, fetched substantive sources, grouped repetition,
  separated article-described modeling revisions from indexed artifact updates,
  and flagged chronology that could not be established from current versions.
- Explain read `references/explain-mode.md`, discovered and fetched Model 68,
  described historical measurement rather than forecasting, and explicitly
  separated published verification claims from checks it had not run.
- The missing-baseline task asked for a date or pasted brief without searching
  under an invented cutoff.
- The mixed request loaded Catch Up, Brief and `references/comparing-research.md`.
  It gathered the dated digest and November 2025 baseline, reused retrieved
  sources, then separated cost per average watt from incremental satellite NPV.
  It labeled its thesis interpretation as inference rather than an explicit
  author reversal and did not treat unlike launch destinations as comparable.

These are manually reviewed single traces, not statistically robust success
rates or independent economic fact-checks of Mach33's underlying research.

## Model 68 reproduction

Fresh discovery and authorized retrieval were followed by an active-storage
redirect and download. Archive paths, expanded size and symlink entries were
checked before extraction. The archive contained no serialized data cache.
Documentation, engine, self-checks, pinned tests and workbook generator were
inspected. Baseline and scenario ran in separate copies with a scrubbed process
environment and temporary HOME. This was **not an OS sandbox**.

- Filename: `launch_manifest_estate.zip`; size: 9,128,496 bytes.
- Updated: 2026-09-17T17:30:29Z.
- SHA-256: `4be08e8ec1455e56542dd942c82354c20abbb2a4d1a8c64201218d28775326a2`.
- Existing pandas 3.0.0, openpyxl 3.1.5 and LibreOffice were used; none installed.
- `python3 verify.py --fast`: exit 0, 46/46.
- `python3 verify.py --lens`: exit 0, 50/50; worst parity difference 2.274e-13.
- Scenario changed only `DEF.shuttle_orbiter`, include → exclude.
- Scenario `python3 verify.py --fast`: exit 1, 44/46.
- Failures: `headlines.rival_year`, expected 1987 versus 1986;
  `headlines.rival_share`, expected 0.932058311739 versus 0.946994604528016.
- Comparing every original file against the scenario found only the register
  changed. Engine, pins, verifier and dataset were unchanged. Generated local
  caches are not changes to original package files.

The package self-check runs the engine internally. A full `./run` publication
build was not rerun; no failed scenario tables were released. Pro model packages
were neither downloaded nor executed. Read-only Pro metadata/write-ups used in
Brief are not Pro Compute certification.

## Evidence and reproduction

Private raw evidence is under `/tmp/mach33-review-2026-10-09/`:

- `initialize.json`, `tools.json`, `live-summary.json`, `edge-summary.json`.
- `behavioral-r1/`, `behavioral-r2/`, `behavioral-gpt55/`,
  `behavioral-haiku/`, `strict-shape-audit.json`, `grader-canaries.json`.
- `trace-*.jsonl`, trace runner summaries, `trace-setup-blocked/`.
- `model68/provenance.json`, baseline logs, `scenario-check.log`,
  `scenario-result.json` and preserved original ZIP.

This directory is private and temporary. It contains authenticated research
responses and potentially signed file URLs; do not commit or publicly upload it.
This report intentionally excludes credentials, download URLs and source bodies.

Reproduce the public fixture checks:

```sh
python3 scripts/validate.py
python3 scripts/run-behavioral-evals.py --model openai-codex/gpt-6.1-sol \
  --output /tmp/mach33-review-repeat-1
python3 scripts/run-behavioral-evals.py --model openai-codex/gpt-6.1-sol \
  --output /tmp/mach33-review-repeat-2
python3 scripts/run-behavioral-evals.py --model openai-codex/gpt-5.5 \
  --output /tmp/mach33-review-second-model
```

The synthetic fixtures intentionally retain their fixed October 5 date for
repeatability. Live tests use October 9 and explicitly bounded historical windows.
Model inference uses the configured provider account. Results may vary.

The full acceptance YAML remains `status: not-run`: several installation and
client-runtime procedures have not been completed. The October 5 report remains
an historical record, not the current server-status verdict.
