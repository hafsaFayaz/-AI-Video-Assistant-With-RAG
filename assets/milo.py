"""
milo.py — Milo the pixel cat: official mascot of Video Quest AI.

Milo is a fixed, bottom-right widget. It renders the real pixel-art sprite
from assets/milo/<state>.png when one exists (generated to match the
official reference art), and falls back to an emoji if a sprite is ever
missing — so the app never breaks on a missing asset.
"""

import base64
from functools import lru_cache
from pathlib import Path
import random
import streamlit as st

MILO_DIR = Path(__file__).parent / "milo"
SPRITE_EXTENSIONS = (".png", ".gif")

# state -> (emoji fallback sprite, animation class, sample lines)
MILO_STATES = {
    "idle": ("🐱", "", [
        "Waiting for a new quest...",
        "Ready when you are, adventurer.",
    ]),
    "thinking": ("🐱", "thinking", [
        "Hmm... let me think...",
        "Consulting the Memory Vault...",
    ]),
    "reading": ("🐱", "thinking", [
        "Reading the ancient scrolls...",
        "So many words in this one!",
    ]),
    "detective": ("🐱", "thinking", [
        "Searching for clues...",
        "Something's hidden in here...",
    ]),
    "happy": ("😻", "", [
        "Quest complete! Nice work!",
        "We make a great team!",
    ]),
    "sad": ("🙀", "", [
        "Uh oh, that quest failed...",
        "Let's try that again.",
    ]),
}


@lru_cache(maxsize=None)
def _sprite_data_uri(state: str) -> str | None:
    """Base64-encode a real sprite file for a state, if one exists on disk."""
    for ext in SPRITE_EXTENSIONS:
        candidate = MILO_DIR / f"{state}{ext}"
        if candidate.exists():
            mime = "image/gif" if ext == ".gif" else "image/png"
            data = base64.b64encode(candidate.read_bytes()).decode("ascii")
            return f"data:{mime};base64,{data}"
    return None


def render_milo(state: str = "idle", message: str | None = None):
    """Render Milo fixed at bottom-right of the viewport with a speech bubble."""
    if state not in MILO_STATES:
        state = "idle"
    emoji, anim_class, lines = MILO_STATES[state]
    bubble_text = message or random.choice(lines)

    sprite_uri = _sprite_data_uri(state)
    if sprite_uri:
        sprite_html = f'<img src="{sprite_uri}" class="milo-sprite {anim_class}" alt="Milo" />'
    else:
        sprite_html = f'<div class="milo-sprite {anim_class}">{emoji}</div>'

    st.markdown(f"""
    <div class="milo-wrap">
        <div class="milo-bubble">{bubble_text}</div>
        {sprite_html}
    </div>""", unsafe_allow_html=True)


def milo_says(message: str) -> str:
    """Return a chat-log-friendly Milo line (used in dialogue_history)."""
    return message
