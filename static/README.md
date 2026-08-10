# AdamXweb.github.io

My personal blog, live at <https://adam.kostarelas.com>.

[![Project status](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FAdamXweb%2F.github%2Fmain%2Fbadges%2FAdamXweb.github.io.json)](https://github.com/AdamXweb/.github/blob/main/STATUS.md#adamxwebgithubio)
[![github pages](https://github.com/AdamXweb/AdamXweb.github.io/actions/workflows/gh-pages.yml/badge.svg?branch=dev)](https://github.com/AdamXweb/AdamXweb.github.io/actions/workflows/gh-pages.yml)
[![Licence: MIT](https://img.shields.io/badge/licence-MIT-blue)](https://github.com/AdamXweb/AdamXweb.github.io/blob/dev/LICENSE)

<!-- disclosure:start -->
> [!NOTE]
> **Project status.** The badge above is generated from [my status list](https://github.com/AdamXweb/.github/blob/main/STATUS.md), which says what I promise for this project and every other one.
<!-- disclosure:end -->

---

A [Hugo](https://gohugo.io) site using the [Blowfish](https://github.com/nunocoracao/blowfish)
theme, which is vendored into this repository at `themes/blowfish` (version 2.89.1) rather than
pulled in as a submodule or Hugo module.

The repository has two branches that matter:

- `dev` holds the source — content, config, assets and the build workflow. This is the branch to
  edit.
- `master` holds the generated site. It is overwritten by the deploy workflow, so nothing should be
  committed to it by hand. That includes this file: it is `static/README.md` on `dev`, and the build
  copies it to the root of `master`, which is what GitHub shows on the repository page.

## Run it locally

Hugo **extended** 0.151.0 — the version pinned in
[`.github/workflows/gh-pages.yml`](https://github.com/AdamXweb/AdamXweb.github.io/blob/dev/.github/workflows/gh-pages.yml).
See the [Hugo install docs](https://gohugo.io/installation/). No submodule fetch is needed because
the theme is committed in the tree.

```sh
hugo server     # local server with live reload
hugo --minify   # build the production site into ./public
```

There is also a [`justfile`](https://github.com/AdamXweb/AdamXweb.github.io/blob/dev/justfile) with
the same commands as [just](https://just.systems) recipes: `just run`, `just build`, `just clean`,
plus `just default` and `just setup`.

Ignore `just setup`. It runs `git submodule update --init --recursive`, from when the theme was a
submodule — there is no `.gitmodules` any more and `themes/blowfish` is committed in the tree, so the
recipe does nothing. The `submodules: true` in the workflow's checkout step is stale for the same
reason.

## How it deploys

Pushing to `dev` runs the `github pages` workflow, which builds with `hugo --minify` and publishes
`./public` to `master` using `peaceiris/actions-gh-pages`, writing the `CNAME` for
`adam.kostarelas.com`. GitHub Pages then serves `master` at that domain.

The workflow also declares an hourly `schedule` trigger, but no scheduled runs appear in the Actions
history — GitHub only runs scheduled workflows from the default branch (`master`), which does not
contain the workflow file. In practice every deploy is triggered by a push to `dev`.

## Where things live

| Path | What is in it |
| --- | --- |
| `content/` | All pages. Sections: `blog`, `micro`, `projects`, `open`, `privacy`, `dashboard`, `resource`. |
| `archetypes/default.md` | Front matter template used by `hugo new`. |
| `hugo.toml` | `baseURL`, `languageCode` and site title. |
| `config/_default/` | The rest of the config — params, menus, languages, markup. |
| `assets/` | Custom CSS (`css/custom.css`, `css/syntax.css`) and site images such as the avatar. |
| `static/` | Favicons and `uploads/`, copied verbatim to the site root. |
| `layouts/` | Section templates that override the theme (`micro`, `open`, `privacy`, `projects`). |
| `themes/blowfish/` | The vendored theme. Changes here are overwritten on a theme upgrade — override in `layouts/` or `assets/` instead. |

Posts are page bundles: a folder under `content/blog/` containing `index.md` alongside its images,
so a post and its assets move together.
