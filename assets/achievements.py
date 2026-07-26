import streamlit as st

ACHIEVEMENTS = [
    "First Video Uploaded",
    "First Summary Generated",
    "First Question Asked",
    "Knowledge Explorer"
]


def unlocked_count(state):
    return len(state.get("unlocked", []))


def render_achievement_grid():
    cols = st.columns(2)

    for i, item in enumerate(ACHIEVEMENTS):
        with cols[i % 2]:
            st.markdown(
                f"""
                <div class="achievement-card">
                    🏆 {item}
                </div>
                """,
                unsafe_allow_html=True
            )