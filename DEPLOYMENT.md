# Deployment plan — 3 days max

## Recommended stack

- GitHub repository: `antoine-dop-site`
- Coding assistant: Codex connected to the GitHub repo
- Hosting: Vercel, connected to GitHub
- Video: Vimeo embed, not GitHub

## Day 1 — Today

1. Create a new GitHub repository: `antoine-dop-site`.
2. Push this folder to GitHub.
3. Connect the repository to Codex.
4. Give Codex the task in `CODEX_BRIEF.md`.
5. Import the same repository in Vercel.
6. First deployment online with the temporary Vercel URL.

## Day 2

1. Review the site on desktop and mobile.
2. Ask Codex to correct spacing, image rhythm, broken links and mobile layout.
3. Add exact Sœurs / Houme stills only if supplied.
4. Run a second Vercel deployment by pushing to `main`.

## Day 3

1. Final text correction.
2. Add custom domain if available.
3. Check contact links, Vimeo modal, mobile display.
4. Publish final URL.

## Git commands

If GitHub CLI is installed:

```bash
cd antoine-dop-site-ready
gh repo create antoine-dop-site --private --source=. --remote=origin --push
```

If you create the repo manually on GitHub:

```bash
cd antoine-dop-site-ready
git init
git add .
git commit -m "Initial premium DP portfolio site"
git branch -M main
git remote add origin https://github.com/antoinegueugneaudop-alt/antoine-dop-site.git
git push -u origin main
```
