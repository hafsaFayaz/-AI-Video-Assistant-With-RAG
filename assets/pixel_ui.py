"""
pixel_ui.py — Reusable pixel-RPG UI components for Streamlit.

Every function here returns/renders HTML that relies on classes defined
in assets/style.css. Nothing in this file touches backend logic —
it only presents whatever data it's handed.
"""

from pathlib import Path
import streamlit as st

ASSETS_DIR = Path(__file__).parent


def inject_css():
    """Load style.css once per session."""
    css_path = ASSETS_DIR / "style.css"
    st.markdown(f"<style>{css_path.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)


def hero_banner(title: str, subtitle: str, cat_emoji: str = "🐱"):
    st.markdown(f"""
    <div class="hero-banner">
        <div class="hero-title">{title}</div>
        <div class="hero-sub">{subtitle}</div>
        <div class="hero-cat">{cat_emoji}</div>
    </div>""", unsafe_allow_html=True)


def quest_card(title: str, content: str, icon: str = "📖"):
    st.markdown(f"""
    <div class="quest-card">
        <div class="quest-card-title">{icon} {title}</div>
        <div class="quest-card-content">{content}</div>
    </div>""", unsafe_allow_html=True)


def badge(text: str, color: str = "purple"):
    """color: purple | orange | pink | mint"""
    return f'<span class="pixel-badge badge-{color}">{text}</span>'

def badge_row(*badges_html: str):
    st.markdown(" ".join(badges_html), unsafe_allow_html=True)


def pixel_bar(label: str, value: int, max_value: int = 100, segments: int = 10, color: str = "mint"):
    """8-bit style segmented bar, e.g. an HP/XP bar."""
    filled = round((value / max_value) * segments) if max_value else 0
    filled = max(0, min(segments, filled))
    seg_html = "".join(
        f'<div class="pixel-bar-seg{" filled" if i < filled else ""}" style="--seg-color: var(--{color});"></div>'
        for i in range(segments)
    )
    st.markdown(f"""
    <div class="pixel-bar-wrap">
        <div class="pixel-bar-label">{label}</div>
        <div class="pixel-bar-track">{seg_html}</div>
    </div>""", unsafe_allow_html=True)


def scroll_box(text: str):
    """Ancient-scroll styled scrolling text panel (used for transcripts)."""
    st.markdown(f'<div class="scroll-box">{text}</div>', unsafe_allow_html=True)


def dialogue_history(messages: list[dict]):
    """
    messages: list of {"role": "user"|"assistant", "content": str}
    Renders an Undertale-style dialogue log.
    """
    html = '<div class="dialogue-box">'
    for msg in messages:
        if msg["role"] == "user":
            html += f"""
            <div class="d-msg">
                <span class="d-label you">You</span>
                <div class="d-bubble you">{msg['content']}</div>
            </div>"""
        else:
            html += f"""
            <div class="d-msg">
                <span class="d-label milo">🐱 Milo</span>
                <div class="d-bubble milo">{msg['content']}</div>
            </div>"""
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)


def status_hud(mood_emoji: str, energy_pct: int, xp: int, crystals: int):
    st.markdown(f"""
    <div class="status-hud">
        <span class="hud-item">{mood_emoji} Milo</span>
        <span class="hud-item hud-hp">❤️ Energy {energy_pct}%</span>
        <span class="hud-item hud-xp">⭐ XP {xp}</span>
        <span class="hud-item hud-gem">💎 Crystals {crystals}</span>
    </div>""", unsafe_allow_html=True)


def empty_state(icon: str, title: str, desc: str, badges: list[tuple[str, str]] | None = None):
    badges_html = ""
    if badges:
        badges_html = '<div style="margin-top:1.5rem">' + " ".join(
            badge(text, color) for text, color in badges
        ) + "</div>"
    st.markdown(f"""
    <div class="empty-state">
        <div class="icon">{icon}</div>
        <div class="title">{title}</div>
        <div class="desc">{desc}</div>
        {badges_html}
    </div>""", unsafe_allow_html=True)


def sidebar_header(text: str):
    st.markdown(f'<div class="sidebar-header">{text}</div>', unsafe_allow_html=True)


def sidebar_rule():
    st.markdown('<div class="nav-rule">══════════</div>', unsafe_allow_html=True)
