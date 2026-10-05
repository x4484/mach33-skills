# Grok Bot — save the skills once

Paste this short setup prompt into your Bot. The Bot reads the repository and
saves the workflows; you do not need to read or paste their full instructions.

```text
Fetch https://github.com/x4484/mach33-skills. Read README.md, then the three directories under skills/, including every referenced file. Save them as three reusable private Grok Bot skills: mach33-research-brief, mach33-catch-up, and mach33-model-lab. Preserve their instructions, reference content, routing rules, and safety boundaries; do not replace them with lossy summaries. Use this Bot's supported skill-saving mechanism, not Grok Build filesystem paths.

Ask before overwriting existing skills. Do not execute repository scripts, install dependencies, download models, run model code, or create routines during setup.

Verify each skill is listed in my private skill library and can be invoked. Check whether the Mach33 MCP at https://research.33fg.com/mcp is connected and authenticated. If needed, help me connect it using your supported native connector and let me complete normal sign-in. Never ask for passwords or tokens in chat.

Report saved skills and authenticated MCP access separately. If fetching or saving is unavailable, explain the blocked step; do not claim installation succeeded. Finish with one example research question.
```

## Check it worked

Type `/` in the desktop composer to find the saved skills.
If absent, check **Marketplace → Your plugins → Manage plugins and skills →
Private skills**.

Ask: "Use mach33-research-brief to explain what Mach33 thinks about orbital compute."

Saved private skills are shared across your Bots. Each Bot still needs appropriate
Mach33 access. Saved procedures do not guarantee access to an earlier briefing:
provide its text or a cutoff date when comparison requires it.

## If setup is blocked

The documented product supports saving private skills, but this repository's
GitHub-to-private-skill flow has not been tested yet. There is no claim of a
native one-click GitHub importer.
If the Bot cannot fetch the repo, offer a GitHub ZIP download/upload where the
client supports attachments. If saving is unavailable, report the limitation;
do not pretend session instructions are installed skills.

Model Explain does not require code execution. Compute remains unverified and
requires a separately tested download/runtime/self-check path.

## Documentation basis

- [Grok Bot skills and routines](https://docs.x.ai/grok-bot/skills-routines-and-automations)
- [Grok Bot overview](https://docs.x.ai/grok-bot/overview)

Grok Bot and Grok Build are different products. Do not apply Build's local
skill-directory conventions to Bot without explicit product support.
