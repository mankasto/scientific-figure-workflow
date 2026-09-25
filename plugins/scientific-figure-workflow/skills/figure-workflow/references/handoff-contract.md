# Handoff contract

Each job uses this structure:

```text
job/
  status.json
  00_source/
  01_prompt/
  02_render/candidates/
  03_reconstruct/assets/
  03_reconstruct/build/
  04_qa/
```

`status.json` contains `job_id`, `stage`, `state`, `owner`, `updated_at`, `inputs`, `outputs`, `hard_gates`, and `notes`.

Allowed stages are `source`, `prompt`, `render`, `reconstruct`, `qa`, and `complete`. A specialist may advance only its own stage. It must not silently rewrite approved upstream artifacts; revisions create versioned files and record the reason in `notes`.

The prompt handoff includes `structure_lock.yaml` and `structure_skeleton.png`. The render, reconstruction, and QA stages must cite the lock version they used. Any change to topology, visual center, relative region allocation, connector grammar, or density distribution invalidates downstream approval and returns the job to the prompt stage.

Paths in manifests are relative to the job root so another contributor can clone the repository and continue the work.
