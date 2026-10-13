# Choose your assistant

No terminal commands are required in these recommended setup flows: paste the
appropriate prompt into your assistant and approve only the necessary setup steps.
The assistant must have the tools/permissions needed to install files.

- [Grok Bot: save reusable skills](grok-bot.md)
- [Claude Code](claude-code.md)
- [Codex](codex.md)
- [Pi](pi.md)
- [Hermes](hermes.md)
- [OpenClaw](openclaw.md)

First connect Mach33 using the [MCP guide](https://research.33fg.com/mcp-guide).
A prompt cannot create a connector if your client or bot operator has not enabled
that capability. You may still need to complete normal account sign-in.

## Delegated research and activation

Installation does not guarantee that a parent or helper loads a skill. Put this
handoff rule in the parent agent's instructions using the operator-approved
configuration mechanism; this repository does not change those settings for you:

> Before Mach33 work, select and load the matching canonical skill: Brief for
> questions, fact-checks and chart/script numbers; Catch Up for publication
> windows; Model Lab for model assumptions or requested scenarios. When delegating,
> pass the skill's installed path or saved-skill name, the user's actual question,
> cutoff/baseline and execution limits. Require the helper to load the skill and
> applicable references before research, and return dated fetched evidence,
> per-source access and unresolved gaps. Do not replace the skill with a tool recipe.

Check that helpers can actually discover/read the skill and its references.
If unavailable, provide the reviewed canonical content through supported context
sharing (not a lossy summary), or report the loading block. Never count a handoff
instruction as proof of loading: inspect the helper's read/invocation trace.
A helper without the instructions can produce ordinary MCP research, but that
must not be labeled a with-skill evaluation.

After installation, test a natural task such as "Fact-check this video claim
using Mach33" as well as explicit invocation. Check both parent and helper traces.
For a multi-file skill, confirm references survived installation. Single-file
claude.ai packaging remains a separate compatibility task; do not claim a lone
SKILL.md copy contains references it only points to.

## Publication preparation (maintainers only)

This skills-only repository is https://github.com/x4484/mach33-skills.
Mach33 research stays in its separate private repository.
The pack uses Apache 2.0; it does not license research or model content.
Finish the release checks and verify installation before promoting the prompts
as supported. Prefer a reviewed version tag in installation instructions.

These are documentation-backed draft flows, not tested installations.
If the assistant cannot download or write files, use GitHub's ZIP download and
the documented manual location; do not claim the prompt installed anything.
