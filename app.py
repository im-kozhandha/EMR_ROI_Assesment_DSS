# =============================================================================
# IMPORTS
# =============================================================================
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import plotly.graph_objects as go

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="EMR ROI Assessment",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── EXTERNAL STYLES (FONTS + ICONS) Font Awesome ──────────────────────────────────────────────────────────────
st.markdown(
    '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" crossorigin="anonymous"/>',
    unsafe_allow_html=True,
)

# ── Global CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

/* ── Reset & base ── */
:root { color-scheme: light !important; }
html, body, [class*="css"], .stApp,
.main, section.main, [data-testid="stAppViewContainer"] {
    font-family: 'Inter', system-ui, -apple-system, sans-serif !important;
    background-color: #f5f7fc !important;
    color: #1a1a1a !important;
}

/* ── Centered content wrapper ── */
section.main > div {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2.4rem 2rem 4rem 2rem !important;
}

/* ═══════════════ SIDEBAR TOGGLE FIX ═══════════════ */
/* Force ALL sidebar toggle-related elements visible */
[data-testid="collapsedControl"],
[data-testid="stSidebarCollapseButton"],
[data-testid="stSidebarCollapseButton"] button,
button[kind="header"],
.st-emotion-cache-yzjhf7,
.st-emotion-cache-1rtdyuf {
    display: flex !important;
    visibility: visible !important;
    opacity: 1 !important;
    pointer-events: all !important;
}

[data-testid="collapsedControl"] {
    position: fixed !important;
    top: 50% !important;
    left: 0 !important;
    z-index: 999999 !important;
    background: #2c8c7a !important;
    border-radius: 0 8px 8px 0 !important;
    width: 28px !important;
    min-height: 48px !important;
    align-items: center !important;
    justify-content: center !important;
    box-shadow: 2px 0 8px rgba(0,0,0,0.18) !important;
    cursor: pointer !important;
    transform: translateY(-50%) !important;
}
[data-testid="collapsedControl"]:hover { background: #1a6b5c !important; }
[data-testid="collapsedControl"] * {
    color: #fff !important;
    fill: #fff !important;
    visibility: visible !important;
}

[data-testid="stSidebarCollapseButton"] button {
    background: #eaf5f3 !important;
    border-radius: 8px !important;
}
[data-testid="stSidebarCollapseButton"] svg { fill: #2c8c7a !important; }

/* ═══════════════ SIDEBAR ═══════════════ */
[data-testid="stSidebar"],
[data-testid="stSidebar"] > div {
    background-color: #ffffff !important;
    border-right: 1px solid #e6edf4 !important;
}
[data-testid="stSidebar"] * { color: #1a1a1a !important; }

[data-testid="stSidebar"] .stMarkdown h2,
[data-testid="stSidebar"] .stMarkdown strong {
    font-size: 0.72rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.09em !important;
    text-transform: uppercase !important;
    color: #64748b !important;
}
[data-testid="stSidebar"] .stMarkdown p,
[data-testid="stSidebar"] .stCaption {
    font-size: 0.74rem !important;
    color: #94a3b8 !important;
}
[data-testid="stSidebar"] label {
    font-size: 0.79rem !important;
    font-weight: 500 !important;
    color: #374151 !important;
}

/* number input field */
[data-testid="stSidebar"] input[type="number"],
[data-testid="stSidebar"] input {
    background-color: #f8fafc !important;
    color: #1a1a1a !important;
    border: 1px solid #dde5ef !important;
    border-radius: 8px 0 0 8px !important;
    font-size: 0.84rem !important;
    font-family: 'Inter', sans-serif !important;
}
/* +/- buttons */
[data-testid="stSidebar"] [data-testid="stNumberInput"] button {
    background-color: #f1f5f9 !important;
    color: #1e293b !important;
    border: 1px solid #dde5ef !important;
    font-weight: 700 !important;
    font-size: 0.95rem !important;
}
[data-testid="stSidebar"] [data-testid="stNumberInput"] button:hover {
    background-color: #e2edf6 !important;
    color: #2c8c7a !important;
}

/* slider filled track */
[data-testid="stSidebar"] [data-baseweb="slider"] [role="progressbar"] {
    background-color: #2c8c7a !important;
}
/* slider thumb */
[data-testid="stSidebar"] [data-baseweb="slider"] div[role="slider"] {
    background-color: #2c8c7a !important;
    border: 2px solid #ffffff !important;
    box-shadow: 0 0 0 3px rgba(44,140,122,0.25) !important;
}
/* slider value tooltip */
[data-testid="stSidebar"] [data-baseweb="slider"] [data-testid="stThumbValue"] {
    background: #2c8c7a !important;
    color: #fff !important;
    border-radius: 4px !important;
    font-size: 0.73rem !important;
    padding: 1px 6px !important;
}
/* slider tick labels */
[data-testid="stSidebar"] [data-testid="stTickBar"] {
    color: #94a3b8 !important;
    font-size: 0.71rem !important;
}

/* sidebar section spacing */
[data-testid="stSidebar"] .block-container { padding-top: 1.8rem !important; }
[data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div { margin-bottom: 0.15rem !important; }

/* ═══════════════ PAGE HEADER ═══════════════ */
.page-header {
    display: flex;
    align-items: flex-start;
    gap: 1rem;
    margin-bottom: 1.6rem;
    padding-bottom: 1.4rem;
    border-bottom: 1px solid #e6edf4;
}
.page-header-icon {
    width: 44px; height: 44px;
    background: #eaf5f3;
    border-radius: 12px;
    display: flex; align-items: center; justify-content: center;
    flex-shrink: 0;
    margin-top: 2px;
}
.page-header-icon i { color: #2c8c7a; font-size: 1.1rem; }
.page-h1 {
    font-size: 1.3rem;
    font-weight: 700;
    color: #0f2027;
    margin: 0 0 0.2rem 0;
    line-height: 1.25;
    letter-spacing: -0.02em;
}
.page-sub {
    font-size: 0.79rem;
    color: #94a3b8;
    margin: 0;
    font-weight: 400;
}

/* ═══════════════ INFO STRIP ═══════════════ */
.info-strip {
    border-left: 3px solid #2c8c7a;
    background: transparent;
    border-radius: 0;
    padding: 0.5rem 1rem;
    font-size: 0.79rem;
    color: #374151;
    margin-bottom: 2rem;
    line-height: 1.6;
}
.info-strip strong { color: #1a4d4a; }

/* ═══════════════ METRIC CARDS ═══════════════ */
.metric-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1rem;
    margin-bottom: 2rem;
}
.metric-card {
    background: #ffffff;
    border: 1px solid #e6edf4;
    border-radius: 18px;
    padding: 1.25rem 1.35rem 1.1rem;
    transition: border-color 0.18s ease;
    position: relative;
    overflow: hidden;
}
.metric-card:hover { border-color: #b2d8d2; }

/* Accent card — Annual ROI */
.metric-card.accent {
    border-color: #2c8c7a;
    background: linear-gradient(135deg, #ffffff 60%, #f0faf8 100%);
}
.metric-card.accent:hover { border-color: #1a6b5c; }
.metric-card.accent .card-value { color: #2c8c7a; }
.metric-card.accent .card-icon i { color: #2c8c7a; }

/* card top stripe for accent */
.metric-card.accent::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: #2c8c7a;
    border-radius: 18px 18px 0 0;
}

.card-icon { font-size: 0.8rem; color: #94a3b8; margin-bottom: 0.65rem; display: block; }
.card-icon i { font-size: 0.85rem; }
.card-label {
    font-size: 0.66rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #94a3b8;
    margin-bottom: 0.4rem;
}
.card-value {
    font-size: 1.8rem;
    font-weight: 700;
    color: #0f2027;
    line-height: 1.05;
    letter-spacing: -0.03em;
}
.card-sub {
    font-size: 0.68rem;
    color: #b0bec5;
    margin-top: 0.35rem;
    font-weight: 400;
}

/* ═══════════════ SECTION HEADERS ═══════════════ */
.section-hdr {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin: 0 0 0.9rem 0;
}
.section-hdr i {
    font-size: 0.78rem;
    color: #2c8c7a;
    width: 18px; text-align: center;
}
.section-hdr span {
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 0.09em;
    text-transform: uppercase;
    color: #94a3b8;
}

/* ═══════════════ CHART CONTAINER ═══════════════ */
.chart-card {
    background: #ffffff;
    border: 1px solid #e6edf4;
    border-radius: 18px;
    padding: 1.4rem 1.4rem 0.8rem;
    margin-bottom: 1.5rem;
}
/* strip plotly default padding */
[data-testid="stPlotlyChart"] { margin: 0 !important; }
[data-testid="stPlotlyChart"] > div {
    border: none !important;
    border-radius: 0 !important;
    background: transparent !important;
}

/* ═══════════════ TABLE ═══════════════ */
.table-card {
    background: #ffffff;
    border: 1px solid #e6edf4;
    border-radius: 18px;
    padding: 1.2rem 1.4rem;
    height: 100%;
}
table { font-size: 0.81rem !important; border-collapse: collapse; width: 100%; }
th {
    font-size: 0.66rem !important; font-weight: 700 !important;
    letter-spacing: 0.07em; text-transform: uppercase;
    color: #94a3b8 !important; padding: 6px 10px;
    border-bottom: 1px solid #e6edf4;
    text-align: left; background: transparent !important;
}
td {
    padding: 7px 10px !important; color: #334155 !important;
    border-bottom: 1px solid #f1f5f9;
    background: transparent !important;
}
tr:last-child td { border-bottom: none; }

/* ═══════════════ STRIP BOXES ═══════════════ */
.transition-strip {
    border-left: 3px solid #f59e0b;
    padding: 0.6rem 1rem;
    font-size: 0.79rem;
    color: #78350f;
    margin: 1.5rem 0;
    line-height: 1.7;
}
.summary-strip {
    border-left: 3px solid #2c8c7a;
    padding: 0.8rem 1.1rem;
    font-size: 0.82rem;
    color: #1a4d4a;
    line-height: 2.1;
    margin-bottom: 1rem;
}

/* ═══════════════ FOOTER ═══════════════ */
.footer-note {
    text-align: center;
    font-size: 0.7rem;
    color: #cbd5e1;
    margin-top: 2.5rem;
    padding-top: 1.5rem;
    border-top: 1px solid #e6edf4;
}

/* ═══════════════ MISC ═══════════════ */
#MainMenu, footer, header { visibility: hidden !important; }
[data-testid="stDecoration"] { display: none !important; }
.stCaption > div { color: #94a3b8 !important; font-size: 0.73rem !important; }
</style>
""", unsafe_allow_html=True)

# ── JS Sidebar Toggle (failsafe — works even when native button is hidden) ────────────────
components.html("""
<script>
(function() {
  function injectToggle() {
    var pd = window.parent.document;
    if (pd.getElementById('emr-sidebar-btn')) return;

    var btn = document.createElement('button');
    btn.id = 'emr-sidebar-btn';
    btn.innerHTML = '&#9776;';
    btn.title = 'Toggle Sidebar';
    btn.style.cssText = [
      'position:fixed','top:50%','left:0',
      'transform:translateY(-50%)',
      'z-index:2147483647',
      'background:#2c8c7a','color:#fff',
      'border:none','border-radius:0 8px 8px 0',
      'width:30px','height:54px',
      'font-size:18px','cursor:pointer',
      'box-shadow:2px 0 10px rgba(0,0,0,0.22)',
      'display:flex','align-items:center','justify-content:center'
    ].join(';');

    btn.onmouseenter = function(){ this.style.background='#1a6b5c'; };
    btn.onmouseleave = function(){ this.style.background='#2c8c7a'; };

    btn.onclick = function() {
      // 1. Try native Streamlit collapse button
      var native = pd.querySelector('[data-testid="collapsedControl"]') ||
                   pd.querySelector('[data-testid="stSidebarCollapseButton"] button');
      if (native) { native.click(); return; }

      // 2. Fallback: toggle sidebar element directly
      var sb = pd.querySelector('[data-testid="stSidebar"]');
      if (sb) {
        var collapsed = sb.getAttribute('aria-expanded') === 'false' || sb.offsetWidth < 20;
        sb.style.display = collapsed ? '' : 'none';
      }
    };

    pd.body.appendChild(btn);
  }

  injectToggle();
  [300, 800, 1800, 3500].forEach(function(t){ setTimeout(injectToggle, t); });
})();
</script>
""", height=0)

# ── Page Header+ Context ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="page-header">
  <div class="page-header-icon"><i class="fa-solid fa-hospital-user"></i></div>
  <div>
    <p class="page-h1">EMR ROI &amp; Paperless Assessment</p>
    <p class="page-sub">Decision tool for hospital owners &nbsp;·&nbsp; All values are adjustable estimates</p>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="info-strip">
  <strong>Default assumptions &nbsp;—</strong>&nbsp;
  Paper time: 12 min &nbsp;·&nbsp; EMR time: 8 min &nbsp;·&nbsp;
  Error rate: 4% &nbsp;·&nbsp; Learning period: 3 days &nbsp;·&nbsp; Efficiency drop: 10%
</div>
""", unsafe_allow_html=True)

# ── Sidebar => User inputs────────────────────────────────────────────────
with st.sidebar:
    st.markdown("**INPUTS**")
    st.caption("Adjust values to model your scenario")
    st.markdown("")
    patients      = st.number_input("Patients per day",                  min_value=1,   value=100,    step=10)
    paper_time    = st.number_input("Time per patient — paper (min)",    min_value=1,   value=12,     step=1)
    emr_time      = st.number_input("Time per patient — EMR (min)",      min_value=1,   value=8,      step=1)
    paper_cost_mo = st.number_input("Monthly paper cost (₹)",            min_value=0,   value=15000,  step=500)
    error_rate    = st.slider("Error rate (%)",  0.0, 20.0, 4.0, 0.5)
    cost_per_err  = st.number_input("Cost per error (₹)",                min_value=0,   value=2000,   step=100)
    setup_cost    = st.number_input("EMR setup cost (₹)",                min_value=0,   value=500000, step=10000)
    maint_cost_mo = st.number_input("Monthly maintenance cost (₹)",      min_value=0,   value=8000,   step=500)
    digit_level   = st.slider("Digitization level (%)", 0, 100, 70, 1)

# ── Core Calculations ──────────────────────────────────────────────────
WORKING_DAYS = 26

# --- Time savings ---
time_saved_per      = paper_time - emr_time
daily_time_saved    = time_saved_per * patients
monthly_time_hr     = daily_time_saved * WORKING_DAYS / 60

# --- Convert time to money ---
STAFF_COST_PER_HR   = 300
time_benefit_mo     = monthly_time_hr * STAFF_COST_PER_HR

# --- Error + paper savings ---
error_cost_month    = (error_rate / 100) * patients * WORKING_DAYS * cost_per_err
error_saving_mo     = error_cost_month * (digit_level / 100)
paper_saving_mo     = paper_cost_mo * (digit_level / 100)

# --- Total benefit ---
time_benefit_scaled = time_benefit_mo * (digit_level / 100)
total_benefit_mo    = time_benefit_scaled + error_saving_mo + paper_saving_mo

# --- Costs ---
total_cost_mo       = maint_cost_mo
total_cost_yr       = setup_cost + maint_cost_mo * 12

# --- ROI & Payback ---
roi_pct   = ((total_benefit_mo * 12 - total_cost_yr) / total_cost_yr * 100) if total_cost_yr else 0
payback_m = (setup_cost / (total_benefit_mo - maint_cost_mo)) if (total_benefit_mo - maint_cost_mo) > 0 else float("inf")


# ── Break-even Analysis ──────────────────────────────────────────────────
breakeven_digit = None
for d in range(0, 101):
    e_s    = error_cost_month * (d / 100)
    p_s    = paper_cost_mo    * (d / 100)
    time_s = time_benefit_mo  * (d / 100)
    b      = time_s + e_s + p_s
    roi    = ((b * 12 - total_cost_yr) / total_cost_yr * 100) if total_cost_yr else 0
    if roi >= 0:
        breakeven_digit = d
        break

# ── ROI curve graph ──────────────────────────────────────────────────
digit_range = list(range(0, 101, 5))
roi_curve   = []
for d in digit_range:
    e_s    = error_cost_month * (d / 100)
    p_s    = paper_cost_mo    * (d / 100)
    time_s = time_benefit_mo  * (d / 100)
    b      = time_s + e_s + p_s
    roi_curve.append(((b * 12 - total_cost_yr) / total_cost_yr * 100) if total_cost_yr else 0)

# ──  KPI Metric cards ──────────────────────────────────────────────────────────────
payback_str = f"{payback_m:.1f} mo" if payback_m != float("inf") else "N/A"
be_str      = f"{breakeven_digit}%" if breakeven_digit is not None else "&gt;100%"

st.markdown(f"""
<div class="metric-row">

  <div class="metric-card accent">
    <span class="card-icon"><i class="fa-solid fa-chart-line"></i></span>
    <div class="card-label">Annual ROI</div>
    <div class="card-value">{roi_pct:+.1f}%</div>
    <div class="card-sub">Year 1 return on investment</div>
  </div>

  <div class="metric-card">
    <span class="card-icon"><i class="fa-solid fa-clock-rotate-left"></i></span>
    <div class="card-label">Payback Period</div>
    <div class="card-value">{payback_str}</div>
    <div class="card-sub">months to recover setup cost</div>
  </div>

  <div class="metric-card">
    <span class="card-icon"><i class="fa-solid fa-indian-rupee-sign"></i></span>
    <div class="card-label">Monthly Savings</div>
    <div class="card-value">₹{total_benefit_mo:,.0f}</div>
    <div class="card-sub">time + errors + paper</div>
  </div>

  <div class="metric-card">
    <span class="card-icon"><i class="fa-solid fa-sliders"></i></span>
    <div class="card-label">Break-even Digitization</div>
    <div class="card-value">{be_str}</div>
    <div class="card-sub">minimum level for ROI ≥ 0</div>
  </div>

</div>
""", unsafe_allow_html=True)

# ── ROI Chart Visualisation─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="chart-card">
  <div class="section-hdr">
    <i class="fa-solid fa-arrow-trend-up"></i>
    <span>ROI vs Digitization Level</span>
  </div>
""", unsafe_allow_html=True)

fig = go.Figure()
fig.add_hline(y=0, line_dash="dot", line_color="#e74c3c", line_width=1.5)
fig.add_trace(go.Scatter(
    x=digit_range, y=roi_curve,
    mode="lines+markers",
    line=dict(color="#3b6fd4", width=2.5),
    marker=dict(size=6, color="#3b6fd4"),
    fill="tozeroy",
    fillcolor="rgba(59,111,212,0.08)",
    name="ROI %"
))
if breakeven_digit is not None:
    fig.add_vline(x=breakeven_digit, line_dash="dash", line_color="#2e9e5b",
                  annotation_text=f"Break-even {breakeven_digit}%",
                  annotation_font_color="#2e9e5b")

fig.update_layout(
    title=None,
    xaxis_title="Digitization Level (%)",
    yaxis_title="Annual ROI (%)",
    font=dict(family="Inter", size=12, color="#1a1a1a"),
    xaxis=dict(showgrid=True, gridcolor="#f0f2f7",
               tickfont=dict(color="#64748b", size=11),
               title_font=dict(color="#64748b", size=11)),
    yaxis=dict(showgrid=True, gridcolor="#f0f2f7",
               tickfont=dict(color="#64748b", size=11),
               title_font=dict(color="#64748b", size=11)),
    plot_bgcolor="white",
    paper_bgcolor="white",
    height=320,
    margin=dict(l=10, r=10, t=10, b=10),
)
st.plotly_chart(fig, use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

# ── Breakdown +Key Numbers ───────────────────────────────────────────────────
left, right = st.columns([1, 1], gap="medium")

with left:
    st.markdown("""
    <div class="chart-card">
      <div class="section-hdr">
        <i class="fa-solid fa-chart-bar"></i>
        <span>Monthly Benefit Breakdown</span>
      </div>
    """, unsafe_allow_html=True)

    df = pd.DataFrame({
        "Source": ["Time Savings", "Error Reduction", "Paper Savings"],
        "Amount (₹)": [time_benefit_mo, error_saving_mo, paper_saving_mo]
    })
    bar = go.Figure(go.Bar(
        x=df["Source"], y=df["Amount (₹)"],
        marker_color=["#3b6fd4", "#e74c3c", "#2e9e5b"],
        text=[f"₹{v:,.0f}" for v in df["Amount (₹)"]],
        textposition="outside"
    ))
    bar.update_layout(
        plot_bgcolor="white", paper_bgcolor="white",
        font=dict(family="Inter", size=12, color="#1a1a1a"),
        xaxis=dict(tickfont=dict(color="#64748b", size=11),
                   title_font=dict(color="#64748b")),
        yaxis=dict(showgrid=True, gridcolor="#f0f2f7",
                   tickfont=dict(color="#64748b", size=11),
                   title_font=dict(color="#64748b")),
        height=250, margin=dict(l=10, r=10, t=20, b=10), showlegend=False
    )
    st.plotly_chart(bar, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with right:
    st.markdown(f"""
    <div class="table-card">
      <div class="section-hdr" style="margin-bottom:1rem;">
        <i class="fa-solid fa-table-list"></i>
        <span>Key Numbers</span>
      </div>
      <table>
        <tr><th>Metric</th><th style="text-align:right;">Value</th></tr>
        <tr><td>Time saved / patient</td><td style="text-align:right;font-weight:600;color:#0f2027;">{time_saved_per} min</td></tr>
        <tr><td>Daily time saved</td><td style="text-align:right;font-weight:600;color:#0f2027;">{daily_time_saved} min</td></tr>
        <tr><td>Monthly time saved</td><td style="text-align:right;font-weight:600;color:#0f2027;">{monthly_time_hr:.1f} hrs</td></tr>
        <tr><td>Error cost / month (before)</td><td style="text-align:right;font-weight:600;color:#0f2027;">₹{error_cost_month:,.0f}</td></tr>
        <tr><td>Error saving / month</td><td style="text-align:right;font-weight:600;color:#2c8c7a;">₹{error_saving_mo:,.0f}</td></tr>
        <tr><td>Paper saving / month</td><td style="text-align:right;font-weight:600;color:#2c8c7a;">₹{paper_saving_mo:,.0f}</td></tr>
        <tr><td>Total annual benefit</td><td style="text-align:right;font-weight:700;color:#2c8c7a;">₹{total_benefit_mo*12:,.0f}</td></tr>
        <tr><td>Total annual cost</td><td style="text-align:right;font-weight:600;color:#e74c3c;">₹{total_cost_yr:,.0f}</td></tr>
      </table>
    </div>
    """, unsafe_allow_html=True)

# ── Transition note ───────────────────────────────────────────────────────────
st.markdown("""
<div class="transition-strip">
  <i class="fa-solid fa-triangle-exclamation" style="color:#f59e0b;margin-right:0.45rem;"></i>
  <strong>Transition period:</strong> Expect a small efficiency drop (~10%) for the first 3 days while
  staff adapts to EMR workflows. Performance typically returns to normal — or better — within one week.
</div>
""", unsafe_allow_html=True)

# ── Summary ───────────────────────────────────────────────────────────────────
if roi_pct >= 0:
    roi_msg = f"ROI is positive at the current digitization level ({digit_level}%) — you recover costs within <strong>{payback_m:.1f} months</strong>."
else:
    roi_msg = f"ROI turns positive once digitization reaches <strong>{breakeven_digit}%</strong> (currently at {digit_level}%)."

main_benefit = max(
    ("time savings",    time_benefit_mo),
    ("error reduction", error_saving_mo),
    ("paper savings",   paper_saving_mo),
    key=lambda x: x[1]
)[0]

st.markdown(f"""
<div class="summary-strip">
  <i class="fa-solid fa-circle-check" style="color:#2c8c7a;margin-right:0.4rem;"></i>{roi_msg}<br>
  <i class="fa-solid fa-lightbulb" style="color:#2c8c7a;margin-right:0.4rem;"></i>The largest benefit driver is
  <strong>{main_benefit}</strong> — contributing ₹{max(time_benefit_mo, error_saving_mo, paper_saving_mo):,.0f}/mo.<br>
  <i class="fa-solid fa-rotate" style="color:#2c8c7a;margin-right:0.4rem;"></i>A brief adaptation dip (~10%) is normal
  in the first few days — plan a short training buffer.
</div>
""", unsafe_allow_html=True)

# ──Footer and usage──────────────────────────────────────────────────
st.caption("Tip: Estimate time by observing 10 patient visits or use typical ranges (Paper: 10–15 min, EMR: 6–10 min).")

st.markdown("""
<div class="footer-note">
  EMR ROI Assessment Tool &nbsp;·&nbsp; Values are estimates only &nbsp;·&nbsp; Adjust inputs in the sidebar
</div>
""", unsafe_allow_html=True)