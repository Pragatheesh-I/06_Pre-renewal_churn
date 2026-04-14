import streamlit as st

# =============================================================================
# CONFIGURATION — PASTE YOUR POWER BI EMBED URL HERE
# =============================================================================

POWERBI_EMBED_URL = "https://app.powerbi.com/reportEmbed?reportId=d2e1c724-f342-48d0-8960-f8e0d90e9874&autoAuth=true&ctid=bc88ed7e-984d-4728-939e-6ab8bfeaba1d"

# =============================================================================
# PAGE CONFIG
# =============================================================================

st.set_page_config(
    page_title="Pre-Renewal Churn Dashboard",
    page_icon="📊",
    layout="wide"
)

# =============================================================================
# HEADER
# =============================================================================

st.markdown("""
<div style="
    background-color:#1B3A6B;
    color:white;
    padding:16px 24px;
    margin:-1rem -1rem 1rem -1rem;
">
    <h2 style="margin:0;">📊 Pre-Renewal Churn Risk Dashboard</h2>
    <p style="margin:0; font-size:12px; opacity:0.8;">
        Model-driven churn prediction and retention prioritisation
    </p>
</div>
""", unsafe_allow_html=True)

# =============================================================================
# INFO BOX
# =============================================================================

st.markdown("""
<div style="
    background:#EBF3FB;
    border-left:4px solid #1B3A6B;
    padding:10px;
    margin-bottom:15px;
    font-size:13px;
">
    ℹ️ This dashboard provides a complete view of churn risk, key drivers,
    customer behaviour signals, and retention priorities.
</div>
""", unsafe_allow_html=True)

# =============================================================================
# POWER BI EMBED
# =============================================================================

embed_html = f"""
<iframe
    src="{POWERBI_EMBED_URL}"
    width="100%"
    height="800"
    frameborder="0"
    allowFullScreen="true">
</iframe>
"""

st.markdown(embed_html, unsafe_allow_html=True)

# =============================================================================
# FOOTER
# =============================================================================

st.markdown("""
<p style="text-align:center; font-size:12px; color:gray;">
Pre-renewal Churn Analytics
</p>
""", unsafe_allow_html=True)