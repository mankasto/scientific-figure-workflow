# Scientific Figure Workflow

A collaborative Codex plugin for turning research content into:

1. an auditable scientific-figure prompt;
2. a reviewed high-resolution PNG master;
3. a hybrid editable PowerPoint;
4. an independent semantic, visual, package, and editability report.

The workflow is split into five cooperating skills:

| Skill | Responsibility |
|---|---|
| `figure-workflow` | Orchestration and handoff state |
| `figure-prompt-compiler` | Paper/reference → specification and prompt |
| `figure-png-renderer` | Prompt → reviewed PNG master |
| `figure-ppt-reconstructor` | PNG → native shapes/text plus replaceable raster assets |
| `figure-qa-reviewer` | Independent final gate |

## Install from this repository

Add this repository as a Codex plugin marketplace, then install `scientific-figure-workflow`. The marketplace manifest is at `.agents/plugins/marketplace.json`.

For direct skill use, copy `plugins/scientific-figure-workflow` into a Codex-compatible plugin directory.

## Start a job

```bash
python3 plugins/scientific-figure-workflow/scripts/init_figure_job.py work/my-figure --owner your-name
```

Put papers, captions, reference images, or notes in `work/my-figure/00_source/`, then invoke `$figure-workflow`.

Validate handoffs with:

```bash
python3 plugins/scientific-figure-workflow/scripts/validate_figure_job.py work/my-figure
```

## Adapter projects

This repository does not copy third-party skills. It can coordinate independently installed adapters:

- [Happy Figure Skill](https://github.com/BAIKEMARK/happy-figure-skill) or [CCF-Figure](https://github.com/Deepshare-Official/CCF-Figure) for prompt drafting;
- [PaperBanana](https://github.com/dwzhu-pku/PaperBanana) for image rendering and refinement;
- [img2pptx](https://github.com/Lancelot-Xie/img2pptx) for editable PowerPoint reconstruction.

See [THIRD_PARTY.md](THIRD_PARTY.md) for licensing notes.

## Collaboration

Every stage writes versioned artifacts and updates `status.json`. Contributors can work on different stages without sharing chat history or proprietary local skills. Pull requests can review prompts, selected renders, reconstruction manifests, and QA separately.

## License

This orchestration plugin is licensed under Apache-2.0. External adapters and image-generation models retain their own licenses and terms.
