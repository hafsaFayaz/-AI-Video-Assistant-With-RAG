# Video Quest AI — Pixel RPG UI

## What changed
Only presentation. `core/` and `utilities/` are untouched — `app.py` calls the exact
same functions (`process_input`, `transcribe_all`, `generate_title`, `summarize`,
`extract_action_items`, `extract_key_decisions`, `extract_questions`,
`build_rag_chain`, `ask_question`) in the same order as your original file.

## New files
```
assets/
├── style.css      # the entire pixel theme (palette, fonts, components)
├── pixel_ui.py     # reusable components: cards, badges, bars, dialogue box
├── milo.py         # Milo mascot states + floating widget
├── loading.py      # RPG quest log tied to your 6 pipeline steps
└── milo/           # optional: drop idle.gif, thinking.gif, happy.gif, etc.
                     # here later — milo.py already checks for them
app.py               # refactored to use the components above
```

## Run it
```bash
pip install streamlit python-dotenv
streamlit run app.py
```
(plus whatever your `core`/`utils` modules already require).

## Fonts
`Pixelify Sans` (headings/buttons) and `VT323` (body/dialogue) load from Google
Fonts inside `style.css` — no local font files needed. If you want to self-host
the .ttf files instead (e.g. for offline use), drop them in `assets/fonts/` and
swap the `@import` line in `style.css` for `@font-face` rules.

## Milo's sprite
`assets/milo/` now ships real pixel-art PNGs (idle, thinking/reading/detective,
happy, sad) generated to match your reference art — same maroon outline,
orange/amber fur, cream belly, pink ears/nose. `milo.py` base64-embeds
whichever PNG matches the current state directly into the widget, so there's
no extra network request. If a state's file is ever missing, it silently
falls back to an emoji so the app never breaks. Drop in hand-drawn `.gif`s
with the same filenames any time to replace these — no code changes needed.

## Extending
- Add a new quest step: add a row to `QUEST_STEPS` in `assets/loading.py` and
  call `update_step("your_key", "active"/"done")` in `app.py`.
- Add a new badge color: add a `.badge-<name>` rule in `style.css` next to the
  existing four (purple/orange/pink/mint).
- Achievements/Settings pages from your roadmap aren't wired yet (Phase 2+) —
  say the word and I'll scaffold multipage nav in the same pixel theme.
