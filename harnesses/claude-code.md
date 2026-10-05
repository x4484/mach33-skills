# Claude Code — easy setup

Paste this into Claude Code. Approve the required local file changes and complete
Mach33 sign-in when prompted. No manual configuration editing should be necessary
if the agent has the needed tools.

```text
Install the three Mach33 research skills from the public GitHub repository URL I provide below.

Repository: https://github.com/x4484/mach33-skills

Read the repository README and your harness-specific guide first. Inspect the files before installing. Install all three directories under skills/, including their references, using this harness's supported skill location. Do not overwrite existing skills or configuration without asking me. Do not execute repository scripts, install model dependencies, download models, or run model code during setup.

Check whether the Mach33 MCP is already connected. If not, help me add https://research.33fg.com/mcp using your supported connection mechanism. Preserve my existing configuration and let me complete sign-in through the normal authentication flow; never ask me to paste passwords or tokens.

Verify that the three skills are discoverable and the authenticated MCP tools are available. Use a small read-only discovery call; do not claim setup succeeded if any step is blocked. Tell me if I need to reload or start a new session.

Finish with a short status for skills and MCP, plus one example question.

Harness: Claude Code
Skill destination: ~/.claude/skills/
Harness note: Use /mach33-research-brief to invoke Brief explicitly. Start a new session if newly installed skills are not visible.
```

## Try it

"Brief me on what Mach33 thinks about orbital compute."

For Catch Up: "What did Mach33 publish in the last seven days?"
For Model Lab: "Explain the Global Launch Manifest definitions without running code."

## If setup is blocked

Ask the assistant to name the blocked step and the minimum action needed.
If skill discovery fails, reload/start a new session as supported and check again.
If it cannot write files, download the repository ZIP from GitHub and put the
three complete skill directories in the location above. Confirm the location
against your installed version/profile before copying.
If MCP setup is unavailable, use the [Mach33 connection guide](https://research.33fg.com/mcp-guide).
Skill installation and MCP authentication are separate checks.

Compute remains unverified; setup must not download or run model packages.

## Documentation basis

[Official skills documentation](https://code.claude.com/docs/en/skills).

These instructions are drafts pending a clean-install smoke test.
