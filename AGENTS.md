# AGENTS.md — instructions for Codex

You are working on the premium portfolio website for Antoine Gueugneau, Director of Photography.

## Operating mode

Work autonomously and keep moving. The goal is to make the site shippable quickly.

- Do not stop after one tiny fix if there are obvious next improvements in the same scope.
- Group safe visual/code polish into small but meaningful batches.
- Commit completed work and leave the worktree clean.
- Open PRs only when the platform requires it or when the change is substantial.
- If a PR is opened, continue with the next safe task unless blocked by a required user approval.
- Ask the user only for high-impact creative choices: changing image selections, changing project order, replacing copy, or changing the Visual Preparation hierarchy.
- For safe implementation work, proceed without asking: removing dead CSS, responsive fixes, spacing/rhythm polish, broken links, modal/player fixes, accessibility labels, HTML cleanup, and performance improvements.

## Absolute rules

- Site language: English only.
- Use only real stills / photograms already supplied in the repository.
- Do not invent images.
- Do not generate AI replacements for Work pages.
- Do not relight, smooth, reconstruct faces, sharpen aggressively, or make visible AI-style corrections.
- Allowed image treatment only: crop to 2.1, remove black bands, soft micro-contrast, very light harmonization.
- Keep images faithful to the source.

## Visual direction

- White, premium, editorial, international agent-roster feel.
- Quiet typography, strong image rhythm, generous breathing space.
- No technical/descriptive labels visible under work cards.
- Copy must be short, precise and premium.
- When an image is strong enough, let it breathe: do not add unnecessary text overlays.

## Home structure

1. Hero + under-hero
2. Selected Work
3. Showreel
4. Visual Preparation
5. About
6. Contact

## Validated content

Hero:
- Use the hotel / pool / sky / architecture image.
- Do not write Antoine Gueugneau inside the hero image.
- Keep the name only in the header / navigation and footer.
- The hero image should remain clean, quiet and image-led.

Under-hero:
- Left: “A cinematographer’s eye, extended into preparation.”
- Right: “Selected cinematography work across series and feature films.”

Selected Work order:
1. All Those Things We Never Said
2. Sœurs
3. Deutsch-les-Landes
4. Déter
5. Clem
6. Houme

Deutsch-les-Landes:
- Comedy / Amazon Prime Video direction.
- Use the scaphandre / costume image as the Home and Work lead image, not the poetic beach/profile image.

Sœurs:
- Home image: mother/child kiss.
- Work page main image: interior father scene.
- Text: Directed by Yamina Benguigui.

Houme:
- Home and Work lead: wide courtyard with soldiers / prisoners / architecture.
- Text: Directed by Rachid Bouchareb.
- Context: Part of the series of 10 short films against racism ‘Vivre Ensemble’.

Showreel:
- Large 2.1 visual block.
- Buttons: Play Main Reel / Second Reel / More on Vimeo.
- No “2019 Reel”.

Visual Preparation:
- Present as an operational preproduction tool, not an AI gallery.
- Start with 8 identical aligned thumbnails.
- Each case page must include Back to Visual Preparation.

Contact:
- Keep the validated white editorial Contact block.
- Email: antoinegueugneau.dop@gmail.com
- Links: Vimeo, IMDb, LinkedIn, Instagram.

## Autonomous backlog priority

1. Remove obsolete/dead hero overlay CSS and verify the hero has no overlay text.
2. Improve responsive behavior on desktop, tablet and mobile without changing image choices.
3. Check all internal links and page paths.
4. Harmonize spacing rhythm across Home, Work pages and Visual Preparation pages.
5. Improve accessibility labels and focus states.
6. Keep the site deployable as a static site from the repository root.
