"""
loading.py — Turns each backend pipeline step into an RPG quest line.

This module is presentation-only: it renders quest state, it never calls
transcriber.py / summarizer.py / rag_engine.py / extractor.py /
vector_store.py / audio_processor.py itself. app.py still drives the
actual pipeline and simply tells this module what state each step is in.
"""

import streamlit as st

# key -> (quest name, icon)
QUEST_STEPS = [
    ("audio",      "Uploading Video",             "📤"),
    ("transcript", "Listening Carefully",         "👂"),
    ("title",      "Naming the Legend",           "🏷️"),
    ("summary",    "Reading Ancient Scrolls",     "📜"),
    ("extract",    "Mining Knowledge Crystals",   "💎"),
    ("rag",        "Opening the Memory Vault",    "🧠"),
]

STATUS_TAG = {
    "pending": "WAITING",
    "active":  "IN PROGRESS",
    "done":    "COMPLETE",
}


def render_quest_log(steps: dict, placeholder=None):
    """
    steps: dict like {"audio": "done", "transcript": "active", ...}
    Missing keys default to "pending". Renders into `placeholder` if given,
    otherwise renders inline.
    """
    target = placeholder if placeholder is not None else st

    html = '<div class="quest-log-title">🎮 QUEST LOG</div>'
    for key, name, icon in QUEST_STEPS:
        state = steps.get(key, "pending")
        css_class = {"pending": "q-pending", "active": "q-active", "done": "q-done"}[state]
        check = "✅ " if state == "done" else ""
        html += f"""
        <div class="quest-line {css_class}">
            <span class="quest-icon">{icon}</span>
            <span class="quest-name">{check}{name}</span>
            <span class="quest-tag">{STATUS_TAG[state]}</span>
        </div>"""

    target.markdown(html, unsafe_allow_html=True)


def quest_complete_banner(placeholder=None):
    target = placeholder if placeholder is not None else st
    target.markdown(
        '<div class="quest-line q-done" style="justify-content:center;font-size:1.2rem;">'
        '🎉 QUEST COMPLETE</div>',
        unsafe_allow_html=True,
    )


def quest_failed_banner(error_text: str, placeholder=None):
    target = placeholder if placeholder is not None else st
    target.markdown(
        f'<div class="quest-line q-active" style="border-color:var(--pink);">'
        f'💀 Quest failed: {error_text}</div>',
        unsafe_allow_html=True,
    )
