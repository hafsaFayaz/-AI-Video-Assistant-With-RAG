"""
state.py — single source of truth for session-state defaults.

Every page calls init_session_state() at the top so state exists no matter
which page the player lands on first. Nothing here touches the backend
pipeline — it's game/UI state only (XP, crystals, Milo's mood, nav flags).
"""

import streamlit as st

DEFAULTS = {
    # quest pipeline
    "result": None,
    "pipeline_steps": {},
    "pipeline_done": False,
    "last_source": "",

    # chat
    "chat_history": [],
    "questions_asked": 0,

    # Milo / RPG stats
    "milo_state": "idle",
    "xp": 0,
    "crystals": 0,
    "energy": 100,
    "quests_completed": 0,
    "transcript_viewed": False,

    # settings
    "default_language": "english",
    "milo_chatty": True,

    # achievements already shown as "unlocked" (for the pop-in feel later)
    "unlocked_achievements": set(),
}


def init_session_state():
    for key, default in DEFAULTS.items():
        if key not in st.session_state:
            st.session_state[key] = default() if callable(default) else (
                set() if isinstance(default, set) else
                (list(default) if isinstance(default, list) else
                 (dict(default) if isinstance(default, dict) else default))
            )


def reset_progress():
    """Used by the Settings page — wipes RPG progress, keeps the current quest result."""
    st.session_state.xp = 0
    st.session_state.crystals = 0
    st.session_state.energy = 100
    st.session_state.quests_completed = 0
    st.session_state.questions_asked = 0
    st.session_state.transcript_viewed = False
    st.session_state.unlocked_achievements = set()
    st.session_state.milo_state = "idle"


def reset_everything():
    """Full wipe — progress and the current quest/chat data."""
    reset_progress()
    st.session_state.result = None
    st.session_state.chat_history = []
    st.session_state.pipeline_steps = {}
    st.session_state.pipeline_done = False
    st.session_state.last_source = ""
