# Initial or comprehensive documentation

Use only when the user authorizes comprehensive documentation or reorganization. Do not load or execute this workflow for routine local maintenance. Reuse known goals and project material instead of asking again for established information.

## Establish coverage

Read project entry points, existing documents, actual usage paths, and relevant code and tests to map capabilities to major parts. A README may be stale, and a directory tree does not prove functionality. Verify core user journeys first, then background and maintenance capabilities; investigate uncertainty rather than reading every file first.

Distinguish current capabilities, explicit plans, and unverified areas. Current pages describe the present; plans stay in existing requirements or tasks. If only part of the implementation can be inspected, state coverage and unknowns. Do not equate unseen features with nonexistent ones or implement missing features as a side effect.

## Establish reading entry points

Create or correct the overall architecture and feature index first, then add feature and implementation detail by importance. Reuse equivalent files. Do not move user documents or break links solely to match suggested names.

Defaults are `00-总览与分层.md` and `01-功能全貌.md`. Describe behavior before implementation. One page may cover closely related capabilities; large features may span pages if the index remains navigable. Explain shared mechanisms once.

Preserve the user's directory organization when it differs from defaults, applying the same three-layer responsibilities rather than redesigning folders.

## Verify and complete in batches

Work by independent topic: make the core picture readable before expanding mechanisms. Verify code and evidence for each batch and update affected diagrams, indexes, and cross-references. Complete the whole authorized scope without requesting permission after every batch; explain concrete limits from missing access or important unknowns.

Where historical evidence is absent, describe current structure and observable consequences without inventing motives. Distinguish plans and history; preserve valuable replaced decisions with links to their replacements.

Finally check the reader's route: can readers understand the whole, find important capabilities, and understand key mechanisms and tradeoffs without code? Check affected content and links. Do not create empty pages, uniformly refresh dates, or score the entire repository to demonstrate completion.
