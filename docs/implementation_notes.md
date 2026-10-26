# GitHub profile implementation notes

## What is included

- `README.md` follows the requested eight-section order and keeps the essential profile text readable without images or animation.
- `assets/prince-banner.svg` is an original 3:1 vector banner. It uses charcoal, red, warm white, guitar gold, and a small purple accent; pinstripes, abstract strings, and a quiet waveform suggest a stage and guitar without depicting Prince.
- `assets/terminal-anim.gif` is a silent, self-hosted terminal illustration. It types a short learning session and loops in about 15 seconds. It does not run commands or report real repository state.
- `assets/auth-symbol.svg` is an original pick-and-waveform mark, not a copy of the Love Symbol.
- Projects remain placeholders until real repository links are supplied.

The attachment contained the written visual brief but no separate reference-photo file. The artwork therefore follows the written description and does not reproduce a photograph or a likeness.

## Profile bio options

All three options are under 160 characters:

1. **Minimal and professional** — `Learning programming and logic one project at a time. Building with intention.`
2. **Subtle music reference** — `Exploring code, music, and ideas with curiosity—one small experiment at a time.`
3. **Terminal identity** — `tiagx422@purple-dev:~$` learning JavaScript, Python, Git, GitHub, and MySQL.

These are suggestions only; the GitHub profile description field has not been changed.

## Install or publish

For the profile README to appear, use a public repository whose name exactly matches the GitHub username. Keep `README.md` at the repository root and preserve the `assets/` paths. The `docs/` folder is supporting documentation and is not required for GitHub to render the profile.

This deliverable is arranged for the public profile repository `tiagx422/tiagx422`. If using a different account, replace `tiagx422` in the README, banner, and terminal artwork, then rename the profile repository to that account's exact username. Replace `[PROJECT TITLE]`, `[one-line description]`, and `[LINK TO REPOSITORY]` only after choosing real projects to feature.

## GitHub and animation constraints

The README uses GitHub Flavored Markdown and simple supported HTML alignment only. It has no JavaScript, `<style>`, event handlers, canvas, iframe, audio, or video. The banner and signature are static, local SVGs. The terminal is a local GIF because GitHub README rendering does not provide a safe, dependable place for a custom live terminal program. GIFs loop automatically and cannot be paused in the README, so the animation is deliberately quiet and carries no essential information by color or motion. The alt text and nearby text provide a readable fallback.

The GIF is 244,768 bytes (72 frames, about 15.34 seconds per loop), under the requested 500 KB per-asset limit. Regenerating it requires Pillow and `python docs/create_terminal_gif.py` from the project root. The README itself contains no embedded payload and stays far under 2 MB. All graphic assets are stored in this repository; the stack is presented as grouped text rather than a remote badge wall.

## Accessibility and responsiveness

The banner keeps its typography within a wide safe area and uses a 3:1 viewBox. The terminal uses short lines and is rendered as a responsive image so it scales down on mobile without horizontal scrolling. Important learning-stack and project text remains in the README. Every image has descriptive alternative text. The dark assets retain high contrast in both GitHub themes; the README text itself follows the viewer's selected theme.

## Editing the vector assets

`assets/prince-banner.svg` and `assets/auth-symbol.svg` are the editable source definitions. They use inline vector shapes, paths, text, and restrained fills; neither depends on an external image or font download. `docs/create_terminal_gif.py` is the local generator used to rebuild the GIF.



