# CLAUDE.md

## TODO list workflow

Maintain `TODO.md` at the repo root as an ongoing record of requests. It has two sections: `## Pending` and `## Done`.

- **Whenever the user makes a request**, add it to the `## Pending` section as a checklist item before starting work.
- **When a request is completed**, move it from `## Pending` to `## Done`, rewriting it as a one-line description of the change that was made.
- Keep `## Pending` reading `_Nothing pending._` when it is empty.
- Update `TODO.md` as part of the same change so it stays in sync with the work.

## Deploy / versioning workflow

The repo-root `VERSION` file holds an integer build number that the UI shows at
the top of the page (`index.html` reads it).

- **Before every deploy to `main`, increment `VERSION`** — run
  `python3 scripts/bump_version.py` (prints the new number) and commit the bump
  along with the changes being deployed.
- Deploying = fast-forward `main` to the working branch and push; the GitHub
  Actions workflow then publishes to GitHub Pages. Pushing only to the working
  branch does **not** deploy.
- **After the deploy finishes, tell the user which version number they should
  see** (e.g. "you should see v3" — matching the badge at the top of the page).
