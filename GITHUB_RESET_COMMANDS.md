# Reset GitHub from this clean folder

Use this only if the current GitHub repo has taken the wrong direction and must be replaced by this clean version.

Repository:

```text
antoinegueugneaudop-alt/antoine-dop-site
```

From Terminal, after unzipping this folder:

```bash
cd ~/Downloads/antoine-dop-site-ready
rm -rf .git
git init
git branch -M main
git add .
git commit -m "Reset site from validated Safari V4"
git remote add origin https://github.com/antoinegueugneaudop-alt/antoine-dop-site.git
git push -u origin main --force
```

Then connect / redeploy from Vercel.
