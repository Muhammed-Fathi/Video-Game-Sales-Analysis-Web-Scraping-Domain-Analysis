"""
=============================================================
  Task 3 Dashboard — ML Regression: Predicting Game Sales
  Premium dark-themed SaaS dashboard
  Run: streamlit run task3_dashboard.py
=============================================================
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# ───────────────────────────────────────────────────────────
# Page Configuration
# ───────────────────────────────────────────────────────────
st.set_page_config(
    page_title="ML Regression Dashboard — Video Game Sales",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ───────────────────────────────────────────────────────────
# GLOBAL CSS — Dark Futuristic Theme + Animations
# ───────────────────────────────────────────────────────────
st.markdown("""
<style>
    /* ── Premium Fonts ── */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap');

    /* ── CSS Custom Properties ── */
    :root {
        --bg-primary: #06080f;
        --bg-secondary: #0c1120;
        --bg-tertiary: #111827;
        --bg-card: rgba(15, 23, 42, 0.55);
        --bg-card-hover: rgba(15, 23, 42, 0.75);
        --border-subtle: rgba(148, 163, 184, 0.07);
        --border-glow-cyan: rgba(6, 182, 212, 0.25);
        --border-glow-purple: rgba(139, 92, 246, 0.25);
        --text-primary: #f1f5f9;
        --text-secondary: #94a3b8;
        --text-muted: #64748b;
        --accent-cyan: #06b6d4;
        --accent-purple: #8b5cf6;
        --accent-indigo: #6366f1;
        --accent-emerald: #10b981;
        --accent-rose: #f43f5e;
        --accent-amber: #f59e0b;
        --accent-blue: #3b82f6;
        --accent-pink: #ec4899;
        --accent-orange: #f97316;
        --accent-teal: #14b8a6;
        --glow-cyan: 0 0 30px rgba(6, 182, 212, 0.12);
        --glow-purple: 0 0 30px rgba(139, 92, 246, 0.12);
        --glow-emerald: 0 0 30px rgba(16, 185, 129, 0.12);
        --radius-sm: 8px;
        --radius-md: 14px;
        --radius-lg: 20px;
        --radius-xl: 24px;
        --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }

    /* ── Global Background ── */
    .stApp {
        background: var(--bg-primary) !important;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        color: var(--text-primary);
    }
    .stApp::before {
        content: '';
        position: fixed;
        top: 0; left: 0; right: 0; bottom: 0;
        background:
            radial-gradient(ellipse 70% 50% at 15% 10%, rgba(6, 182, 212, 0.05) 0%, transparent 50%),
            radial-gradient(ellipse 60% 40% at 85% 85%, rgba(139, 92, 246, 0.04) 0%, transparent 50%),
            radial-gradient(ellipse 40% 30% at 50% 50%, rgba(16, 185, 129, 0.02) 0%, transparent 50%);
        pointer-events: none;
        z-index: 0;
    }

    /* ── Scrollbar ── */
    ::-webkit-scrollbar { width: 5px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb { background: rgba(148, 163, 184, 0.12); border-radius: 10px; }
    ::-webkit-scrollbar-thumb:hover { background: rgba(148, 163, 184, 0.22); }

    /* ── Keyframe Animations ── */
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(28px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    @keyframes scaleIn {
        from { opacity: 0; transform: scale(0.92); }
        to { opacity: 1; transform: scale(1); }
    }
    @keyframes slideInLeft {
        from { opacity: 0; transform: translateX(-16px); }
        to { opacity: 1; transform: translateX(0); }
    }
    @keyframes pulseGlow {
        0%, 100% { box-shadow: 0 0 6px rgba(6, 182, 212, 0.15); }
        50% { box-shadow: 0 0 24px rgba(6, 182, 212, 0.35); }
    }
    @keyframes borderPulse {
        0%, 100% { border-color: rgba(6, 182, 212, 0.1); }
        50% { border-color: rgba(6, 182, 212, 0.3); }
    }
    @keyframes shimmer {
        0% { background-position: -200% 0; }
        100% { background-position: 200% 0; }
    }
    @keyframes countUp {
        from { opacity: 0; transform: translateY(8px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-3px); }
    }
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .anim-fade-up { animation: fadeInUp 0.6s ease-out forwards; }
    .anim-fade { animation: fadeIn 0.5s ease-out forwards; }
    .anim-scale { animation: scaleIn 0.5s ease-out forwards; }
    .anim-slide { animation: slideInLeft 0.5s ease-out forwards; }
    .anim-delay-1 { animation-delay: 0.08s; opacity: 0; }
    .anim-delay-2 { animation-delay: 0.16s; opacity: 0; }
    .anim-delay-3 { animation-delay: 0.24s; opacity: 0; }
    .anim-delay-4 { animation-delay: 0.32s; opacity: 0; }
    .anim-delay-5 { animation-delay: 0.40s; opacity: 0; }
    .anim-delay-6 { animation-delay: 0.48s; opacity: 0; }

    /* ── Sidebar ── */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #070b14 0%, #0c1120 50%, #070b14 100%) !important;
        border-right: 1px solid var(--border-subtle) !important;
    }
    section[data-testid="stSidebar"] > div:first-child { padding-top: 1.2rem; }
    section[data-testid="stSidebar"] .stMultiSelect label,
    section[data-testid="stSidebar"] .stSlider label,
    section[data-testid="stSidebar"] .stSelectbox label {
        font-size: 0.78rem !important;
        font-weight: 500 !important;
        color: var(--text-secondary) !important;
    }

    /* ── Sidebar Brand ── */
    .sidebar-brand {
        text-align: center;
        padding: 0 0 1.2rem 0;
        border-bottom: 1px solid var(--border-subtle);
        margin-bottom: 1.2rem;
        animation: fadeIn 0.5s ease-out forwards;
    }
    .sidebar-brand-name {
        font-size: 1.2rem;
        font-weight: 700;
        color: var(--text-primary);
    }
    .sidebar-brand-name span {
        background: linear-gradient(135deg, var(--accent-emerald), var(--accent-cyan));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    .sidebar-brand-tag {
        font-size: 0.68rem;
        color: var(--text-muted);
        margin-top: 3px;
        letter-spacing: 1px;
        text-transform: uppercase;
    }

    /* ── Sidebar Status Card ── */
    .sidebar-status {
        background: rgba(15, 23, 42, 0.4);
        border: 1px solid var(--border-subtle);
        border-radius: var(--radius-md);
        padding: 12px 14px;
        margin-bottom: 8px;
        font-size: 0.78rem;
        color: var(--text-secondary);
        display: flex;
        align-items: center;
        gap: 8px;
        transition: var(--transition);
    }
    .sidebar-status:hover { border-color: rgba(148, 163, 184, 0.12); }
    .sidebar-status .dot {
        width: 7px; height: 7px;
        border-radius: 50%;
        flex-shrink: 0;
    }
    .dot-green { background: var(--accent-emerald); box-shadow: 0 0 8px rgba(16, 185, 129, 0.5); animation: pulseGlow 2s infinite; }
    .dot-blue { background: var(--accent-blue); box-shadow: 0 0 8px rgba(59, 130, 246, 0.4); }

    /* ── Sidebar Info Block ── */
    .sidebar-info {
        background: rgba(15, 23, 42, 0.3);
        border: 1px solid var(--border-subtle);
        border-radius: var(--radius-md);
        padding: 14px;
        margin-bottom: 8px;
    }
    .sidebar-info-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 5px 0;
        font-size: 0.78rem;
    }
    .sidebar-info-row .label { color: var(--text-muted); }
    .sidebar-info-row .value { color: var(--text-primary); font-weight: 600; }

    /* ── Sidebar Footer ── */
    .sidebar-footer {
        text-align: center;
        padding-top: 1rem;
        border-top: 1px solid var(--border-subtle);
        margin-top: 1rem;
    }
    .sidebar-footer p { font-size: 0.65rem; color: var(--text-muted); margin: 2px 0; }

    /* ── Header ── */
    .ml-header {
        font-size: 2.8rem;
        font-weight: 900;
        text-align: center;
        padding: 1rem 0 0.15rem;
        background: linear-gradient(135deg, var(--accent-emerald) 0%, var(--accent-cyan) 35%, var(--accent-indigo) 65%, var(--accent-pink) 100%);
        background-size: 200% 200%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: fadeInUp 0.6s ease-out forwards, gradientShift 6s ease infinite;
        letter-spacing: -1px;
    }
    .ml-sub {
        font-size: 1rem;
        color: var(--text-muted);
        text-align: center;
        margin-bottom: 1.8rem;
        animation: fadeInUp 0.7s ease-out forwards;
        animation-delay: 0.1s;
        opacity: 0;
        font-weight: 400;
    }

    /* ── KPI Cards ── */
    .kpi-row {
        display: flex;
        gap: 14px;
        flex-wrap: wrap;
        justify-content: center;
        margin-bottom: 2rem;
    }
    .kpi-card {
        flex: 1 1 130px;
        max-width: 185px;
        padding: 18px 12px 14px;
        border-radius: var(--radius-lg);
        text-align: center;
        color: #fff;
        position: relative;
        overflow: hidden;
        transition: var(--transition);
        animation: scaleIn 0.5s ease-out forwards;
        cursor: default;
    }
    .kpi-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
    }
    .kpi-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 36px rgba(0, 0, 0, 0.4);
    }
    .kpi-card .val {
        font-size: 1.65rem;
        font-weight: 800;
        animation: countUp 0.6s ease-out forwards;
        letter-spacing: -0.5px;
    }
    .kpi-card .lbl {
        font-size: 0.72rem;
        opacity: 0.85;
        margin-top: 3px;
        font-weight: 500;
        letter-spacing: 0.3px;
    }
    .kpi-green  { background: linear-gradient(135deg, #10b981, #059669); box-shadow: 0 4px 20px rgba(16, 185, 129, 0.2); }
    .kpi-blue   { background: linear-gradient(135deg, #6366f1, #4f46e5); box-shadow: 0 4px 20px rgba(99, 102, 241, 0.2); }
    .kpi-purple { background: linear-gradient(135deg, #8b5cf6, #7c3aed); box-shadow: 0 4px 20px rgba(139, 92, 246, 0.2); }
    .kpi-pink   { background: linear-gradient(135deg, #ec4899, #db2777); box-shadow: 0 4px 20px rgba(236, 72, 153, 0.2); }
    .kpi-orange { background: linear-gradient(135deg, #f97316, #ea580c); box-shadow: 0 4px 20px rgba(249, 115, 22, 0.2); }
    .kpi-teal   { background: linear-gradient(135deg, #14b8a6, #0d9488); box-shadow: 0 4px 20px rgba(20, 184, 166, 0.2); }

    /* ── Section Title ── */
    .sec-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: var(--text-primary);
        margin: 1.5rem 0 1rem;
        display: flex;
        align-items: center;
        gap: 10px;
        animation: fadeInUp 0.5s ease-out forwards;
    }
    .sec-title .bar {
        width: 4px;
        height: 22px;
        border-radius: 4px;
        background: linear-gradient(180deg, var(--accent-cyan), var(--accent-emerald));
        flex-shrink: 0;
    }

    /* ── Glass Card ── */
    .glass-card {
        background: var(--bg-card);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid var(--border-subtle);
        border-radius: var(--radius-lg);
        padding: 24px;
        margin-bottom: 16px;
        transition: var(--transition);
        position: relative;
        overflow: hidden;
    }
    .glass-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(148, 163, 184, 0.08), transparent);
    }
    .glass-card:hover {
        background: var(--bg-card-hover);
        border-color: rgba(148, 163, 184, 0.12);
        transform: translateY(-2px);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    }

    /* ── Insight Callout ── */
    .insight {
        background: linear-gradient(90deg, rgba(6, 182, 212, 0.06), rgba(16, 185, 129, 0.03));
        border: 1px solid rgba(6, 182, 212, 0.1);
        border-left: 3px solid var(--accent-cyan);
        padding: 14px 18px;
        border-radius: 0 var(--radius-md) var(--radius-md) 0;
        margin: 1rem 0;
        color: var(--text-secondary);
        font-size: 0.85rem;
        line-height: 1.65;
        animation: fadeIn 0.5s ease-out forwards;
        transition: var(--transition);
    }
    .insight:hover {
        border-left-color: var(--accent-emerald);
        background: linear-gradient(90deg, rgba(16, 185, 129, 0.06), rgba(6, 182, 212, 0.03));
    }
    .insight strong { color: var(--text-primary); }

    /* ── Badges ── */
    .badge {
        display: inline-flex;
        align-items: center;
        padding: 3px 11px;
        border-radius: 999px;
        font-size: 0.68rem;
        font-weight: 600;
        letter-spacing: 0.4px;
        margin-right: 5px;
        transition: var(--transition);
    }
    .badge:hover { transform: scale(1.05); }
    .badge-tree      { background: rgba(59, 130, 246, 0.12); color: var(--accent-blue); border: 1px solid rgba(59, 130, 246, 0.15); }
    .badge-linear    { background: rgba(148, 163, 184, 0.1); color: var(--text-secondary); border: 1px solid rgba(148, 163, 184, 0.1); }
    .badge-ensemble  { background: rgba(139, 92, 246, 0.1); color: var(--accent-purple); border: 1px solid rgba(139, 92, 246, 0.12); }
    .badge-boost     { background: rgba(245, 158, 11, 0.1); color: var(--accent-amber); border: 1px solid rgba(245, 158, 11, 0.12); }

    /* ── Pipeline Step ── */
    .pipe-step {
        text-align: center;
        padding: 10px 6px;
        animation: scaleIn 0.4s ease-out forwards;
        transition: var(--transition);
    }
    .pipe-step:hover { transform: translateY(-3px); }
    .pipe-step .num {
        width: 38px; height: 38px;
        border-radius: 50%;
        background: linear-gradient(135deg, var(--accent-emerald), var(--accent-cyan));
        color: #fff;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-weight: 700;
        font-size: 0.85rem;
        box-shadow: 0 2px 12px rgba(16, 185, 129, 0.3);
        transition: var(--transition);
    }
    .pipe-step:hover .num { box-shadow: 0 4px 20px rgba(16, 185, 129, 0.5); transform: scale(1.1); }
    .pipe-step .title { font-weight: 600; font-size: 0.82rem; color: var(--text-primary); margin-top: 6px; }
    .pipe-step .desc { font-size: 0.68rem; color: var(--text-muted); margin-top: 2px; }

    /* ── Model Card ── */
    .model-card {
        background: var(--bg-card);
        border: 1px solid var(--border-subtle);
        border-radius: var(--radius-md);
        padding: 18px;
        margin-bottom: 12px;
        transition: var(--transition);
        animation: fadeInUp 0.5s ease-out forwards;
    }
    .model-card:hover {
        background: var(--bg-card-hover);
        border-color: rgba(148, 163, 184, 0.12);
        transform: translateY(-2px);
        box-shadow: 0 6px 24px rgba(0, 0, 0, 0.25);
    }
    .model-card .name { font-weight: 700; font-size: 0.92rem; color: var(--text-primary); }
    .model-card .desc { font-size: 0.75rem; color: var(--text-muted); margin-top: 4px; line-height: 1.5; }
    .model-card .metrics {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.72rem;
        color: var(--accent-cyan);
        margin-top: 8px;
    }

    /* ── Feature Item ── */
    .feat-item {
        display: flex;
        align-items: baseline;
        gap: 8px;
        padding: 5px 0;
        font-size: 0.84rem;
        color: var(--text-secondary);
    }
    .feat-item code {
        background: rgba(6, 182, 212, 0.08);
        color: var(--accent-cyan);
        padding: 2px 8px;
        border-radius: 4px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.78rem;
        border: 1px solid rgba(6, 182, 212, 0.1);
    }

    /* ── Prediction Metric ── */
    .pred-metric {
        background: var(--bg-card);
        border: 1px solid var(--border-subtle);
        border-radius: var(--radius-md);
        padding: 18px 14px;
        text-align: center;
        transition: var(--transition);
        animation: scaleIn 0.4s ease-out forwards;
    }
    .pred-metric:hover {
        border-color: var(--border-glow-cyan);
        box-shadow: var(--glow-cyan);
        transform: translateY(-3px);
    }
    .pred-metric .model-name {
        font-size: 0.75rem;
        font-weight: 600;
        color: var(--text-muted);
        margin-bottom: 6px;
        letter-spacing: 0.2px;
    }
    .pred-metric .pred-val {
        font-size: 1.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, var(--accent-cyan), var(--accent-emerald));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    .pred-metric .pred-delta {
        font-size: 0.7rem;
        color: var(--text-muted);
        margin-top: 4px;
    }
    .pred-metric .pred-delta .positive { color: var(--accent-emerald); }
    .pred-metric .pred-delta .negative { color: var(--accent-rose); }

    /* ── Engineered Feature Display ── */
    .eng-features {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 10px;
    }
    .eng-feat-item {
        background: rgba(15, 23, 42, 0.4);
        border: 1px solid var(--border-subtle);
        border-radius: var(--radius-sm);
        padding: 12px 14px;
        transition: var(--transition);
    }
    .eng-feat-item:hover { border-color: rgba(148, 163, 184, 0.15); }
    .eng-feat-item .ef-label { font-size: 0.7rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.5px; }
    .eng-feat-item .ef-value { font-size: 0.92rem; font-weight: 700; color: var(--text-primary); margin-top: 2px; }

    /* ── Colored Divider ── */
    .colored-divider {
        height: 2px;
        background: linear-gradient(90deg, var(--accent-cyan), var(--accent-purple), transparent);
        border: none;
        margin: 2rem 0;
        border-radius: 2px;
    }

    /* ── Footer ── */
    .app-footer {
        text-align: center;
        padding: 1.5rem 1rem;
        color: var(--text-muted);
        font-size: 0.75rem;
        border-top: 1px solid var(--border-subtle);
        margin-top: 2rem;
    }
    .app-footer .tech-stack {
        display: flex;
        justify-content: center;
        gap: 8px;
        margin-top: 8px;
        flex-wrap: wrap;
    }
    .app-footer .tech-tag {
        padding: 3px 10px;
        border-radius: 999px;
        font-size: 0.65rem;
        font-weight: 500;
        background: rgba(148, 163, 184, 0.06);
        border: 1px solid var(--border-subtle);
        color: var(--text-muted);
    }

    /* ── Tab Overrides ── */
    .stTabs [data-baseweb="tab-list"] {
        gap: 4px;
        background: rgba(15, 23, 42, 0.3);
        border-radius: var(--radius-md);
        padding: 4px;
        border: 1px solid var(--border-subtle);
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: var(--radius-sm) !important;
        padding: 8px 16px !important;
        font-size: 0.82rem !important;
        font-weight: 500 !important;
        color: var(--text-muted) !important;
        transition: var(--transition) !important;
    }
    .stTabs [data-baseweb="tab"]:hover {
        color: var(--text-secondary) !important;
        background: rgba(148, 163, 184, 0.04) !important;
    }
    .stTabs [aria-selected="true"] {
        background: rgba(6, 182, 212, 0.08) !important;
        color: var(--accent-cyan) !important;
        border: 1px solid rgba(6, 182, 212, 0.15) !important;
    }

    /* ── Input Overrides ── */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background: rgba(15, 23, 42, 0.4) !important;
        color: var(--text-primary) !important;
        border: 1px solid var(--border-subtle) !important;
        border-radius: var(--radius-sm) !important;
        font-family: 'Inter', sans-serif !important;
        transition: var(--transition) !important;
    }
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: rgba(6, 182, 212, 0.3) !important;
        box-shadow: 0 0 0 3px rgba(6, 182, 212, 0.06) !important;
    }
    .stSelectbox > div > div > select {
        background: rgba(15, 23, 42, 0.4) !important;
        color: var(--text-primary) !important;
        border: 1px solid var(--border-subtle) !important;
        border-radius: var(--radius-sm) !important;
    }
    .stMultiSelect > div > div {
        background: rgba(15, 23, 42, 0.4) !important;
        border: 1px solid var(--border-subtle) !important;
        border-radius: var(--radius-sm) !important;
    }

    /* ── Label Styling ── */
    .stTextInput > label,
    .stTextArea > label,
    .stSelectbox > label,
    .stSlider > label {
        font-size: 0.78rem !important;
        font-weight: 500 !important;
        color: var(--text-secondary) !important;
    }

    /* ── Button ── */
    .stButton > button {
        border-radius: var(--radius-sm) !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 600 !important;
        transition: var(--transition) !important;
    }
    .stButton > button:hover {
        transform: translateY(-1px) !important;
    }

    /* ── DataFrame ── */
    .stDataFrame {
        border: 1px solid var(--border-subtle) !important;
        border-radius: var(--radius-md) !important;
        overflow: hidden;
    }

    /* ── Metric Override ── */
    [data-testid="stMetric"] {
        background: var(--bg-card) !important;
        border: 1px solid var(--border-subtle) !important;
        border-radius: var(--radius-md) !important;
        padding: 14px !important;
        transition: var(--transition);
    }
    [data-testid="stMetric"]:hover {
        border-color: rgba(148, 163, 184, 0.12) !important;
    }
    [data-testid="stMetricValue"] {
        font-size: 1.6rem !important;
        font-weight: 800 !important;
        color: var(--text-primary) !important;
    }
    [data-testid="stMetricLabel"] {
        font-size: 0.75rem !important;
        color: var(--text-muted) !important;
    }
    [data-testid="stMetricDelta"] {
        font-size: 0.72rem !important;
    }

    /* ── Info/Success/Warning/Error ── */
    [data-testid="stSuccess"] {
        background: rgba(16, 185, 129, 0.06) !important;
        border: 1px solid rgba(16, 185, 129, 0.12) !important;
        color: var(--accent-emerald) !important;
        border-radius: var(--radius-sm) !important;
    }
    [data-testid="stInfo"] {
        background: rgba(59, 130, 246, 0.06) !important;
        border: 1px solid rgba(59, 130, 246, 0.12) !important;
        color: var(--accent-blue) !important;
        border-radius: var(--radius-sm) !important;
    }
    [data-testid="stWarning"] {
        background: rgba(245, 158, 11, 0.06) !important;
        border: 1px solid rgba(245, 158, 11, 0.12) !important;
        color: var(--accent-amber) !important;
        border-radius: var(--radius-sm) !important;
    }
    [data-testid="stError"] {
        background: rgba(244, 63, 94, 0.06) !important;
        border: 1px solid rgba(244, 63, 94, 0.12) !important;
        color: var(--accent-rose) !important;
        border-radius: var(--radius-sm) !important;
    }

    /* ── Spinner ── */
    .stSpinner > div { border-color: var(--accent-cyan) transparent transparent transparent !important; }

    /* ── Hide defaults ── */
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header { visibility: hidden; }

    /* ── Plotly chart container ── */
    .js-plotly-plot .plotly .modebar { opacity: 0; transition: opacity 0.3s; }
    .js-plotly-plot:hover .plotly .modebar { opacity: 1; }

    /* ── Responsive ── */
    @media (max-width: 768px) {
        .ml-header { font-size: 1.8rem; }
        .ml-sub { font-size: 0.85rem; }
        .kpi-card { flex: 1 1 100px; max-width: 150px; padding: 14px 8px 10px; }
        .kpi-card .val { font-size: 1.3rem; }
        .glass-card { padding: 18px; }
        .eng-features { grid-template-columns: 1fr; }
    }
    @media (max-width: 480px) {
        .ml-header { font-size: 1.5rem; }
        .kpi-row { gap: 8px; }
        .kpi-card { flex: 1 1 80px; max-width: 130px; }
    }
</style>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════
# DATA LOADING
# ═══════════════════════════════════════════════════════════
@st.cache_data
def load_and_prepare():
    """
    Load video game sales data, clean it, engineer features,
    and return everything the dashboard needs.
    """
    # ── Load ──
    try:
        url = "https://raw.githubusercontent.com/amankharwal/Website-data/master/vgsales.csv"
        df = pd.read_csv(url, on_bad_lines="skip")
        if len(df) < 100:
            raise ValueError("too small")
        source = "Real dataset from URL"
    except Exception:
        np.random.seed(42)
        n = 16500
        plat = ["PS2","X360","PS3","Wii","DS","PS4","PS","PC","GBA","PSP",
                "XOne","NES","SNES","3DS","N64","GB","PSV","DC","SAT","2600","WiiU"]
        genre = ["Action","Sports","Misc","Role-Playing","Shooter","Adventure",
                 "Racing","Platform","Simulation","Fighting","Strategy","Puzzle"]
        pub = ["Nintendo","Electronic Arts","Activision","Sony Computer Entertainment",
               "Ubisoft","Take-Two Interactive","THQ","Microsoft Game Studios",
               "Sega","Bandai Namco Games","Konami Digital Entertainment",
               "Capcom","Square Enix","Warner Bros. Interactive",
               "Disney Interactive Studios","Namco Bandai Games","Atari"]
        pfx = ["Super","Mega","Grand","Ultra","Pro","Final","Dark","New","Legend of","Battle"]
        base = ["Racer","Fighter","Soccer","Golf","Tennis","Combat","Arena",
                "Island","Kingdom","Galaxy","Tales","Fantasy","Saga","Dynasty"]
        names = [f"{np.random.choice(pfx)} {np.random.choice(base)}" for _ in range(n)]
        yw = np.array([.005 if y<1995 else .01 if y<2000 else .04 if y<2005
                       else .08 if y<2010 else .06 if y<2015 else .02 for y in range(1980,2024)])
        yw /= yw.sum()
        yrs = np.random.choice(range(1980,2024),n,p=yw).astype(float)
        yrs[np.random.choice(n,271,replace=False)] = np.nan
        na = np.round(np.random.exponential(.3,n),2)
        eu = np.round(np.random.exponential(.22,n),2)
        jp = np.round(np.random.exponential(.1,n),2)
        ot = np.round(np.random.exponential(.08,n),2)
        gl = np.round(na+eu+jp+ot,2)
        pl = np.random.choice(pub,n).tolist()
        for i in np.random.choice(n,58,replace=False): pl[i] = np.nan
        df = pd.DataFrame({"Rank":range(1,n+1),"Name":names,
            "Platform":np.random.choice(plat,n),"Year":yrs,
            "Genre":np.random.choice(genre,n),"Publisher":pl,
            "NA_Sales":na,"EU_Sales":eu,"JP_Sales":jp,
            "Other_Sales":ot,"Global_Sales":gl})
        df = df.sort_values("Global_Sales",ascending=False).reset_index(drop=True)
        df["Rank"] = range(1,len(df)+1)
        source = "Synthetic data (URL unavailable)"

    # ── Clean ──
    df_raw = df.copy()
    df = df.dropna(subset=["Year","Publisher"]).drop_duplicates().reset_index(drop=True)
    df["Year"] = df["Year"].astype(int)
    for c in ["Name","Platform","Genre","Publisher"]:
        df[c] = df[c].astype(str).str.strip()

    # ── Encode ──
    from sklearn.preprocessing import LabelEncoder
    encoders = {}
    for c in ["Platform","Genre","Publisher"]:
        le = LabelEncoder()
        df[c+"_enc"] = le.fit_transform(df[c])
        encoders[c] = le

    # ── Feature engineering ──
    df["Decade"] = (df["Year"] // 10) * 10
    top10 = df.groupby("Publisher")["Global_Sales"].sum().nlargest(10).index
    df["Is_Top_Publisher"] = df["Publisher"].isin(top10).astype(int)
    launch = df.groupby("Platform")["Year"].min().to_dict()
    df["Platform_Age"] = df.apply(lambda r: r["Year"] - launch.get(r["Platform"],r["Year"]),axis=1)
    gf = df["Genre"].value_counts(normalize=True).to_dict()
    df["Genre_Frequency"] = df["Genre"].map(gf)

    return df, df_raw, source, encoders


# ═══════════════════════════════════════════════════════════
# MODEL TRAINING (cached)
# ═══════════════════════════════════════════════════════════
@st.cache_resource
def train_models(df, _features, _target):
    """
    Train 6 regression models and return results, predictions,
    fitted models, and evaluation metrics.
    """
    from sklearn.model_selection import train_test_split, cross_val_score
    from sklearn.preprocessing import StandardScaler
    from sklearn.linear_model import LinearRegression
    from sklearn.tree import DecisionTreeRegressor
    from sklearn.ensemble import (
        RandomForestRegressor,
        GradientBoostingRegressor,
        ExtraTreesRegressor,
    )
    from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

    has_xgb = False
    try:
        from xgboost import XGBRegressor
        has_xgb = True
    except ImportError:
        pass

    sub = df[df["Global_Sales"] > 0].copy()
    X = sub[_features].values
    y = sub[_target].values

    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.20, random_state=42)
    sc = StandardScaler()
    X_tr_sc = sc.fit_transform(X_tr)
    X_te_sc = sc.transform(X_te)

    models = {
        "Linear Regression": LinearRegression(),
        "Decision Tree": DecisionTreeRegressor(random_state=42, max_depth=15),
        "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1),
        "Gradient Boosting": GradientBoostingRegressor(n_estimators=100, random_state=42),
        "Extra Trees": ExtraTreesRegressor(n_estimators=100, random_state=42, n_jobs=-1),
    }
    if has_xgb:
        models["XGBoost"] = XGBRegressor(n_estimators=100, random_state=42,
                                          learning_rate=0.1, max_depth=6, verbosity=0)

    results, preds, fitted = {}, {}, {}

    for name, mdl in models.items():
        mdl.fit(X_tr_sc, y_tr)
        fitted[name] = mdl
        yp = mdl.predict(X_te_sc)
        preds[name] = yp
        mae_  = mean_absolute_error(y_te, yp)
        rmse_ = np.sqrt(mean_squared_error(y_te, yp))
        r2_   = r2_score(y_te, yp)
        cv    = cross_val_score(mdl, X_tr_sc, y_tr, cv=5, scoring="r2", n_jobs=-1)
        results[name] = {
            "MAE": mae_, "RMSE": rmse_, "R²": r2_,
            "CV R²": cv.mean(), "CV Std": cv.std()
        }

    best_name = max(results, key=lambda k: results[k]["R²"])
    return results, preds, fitted, best_name, X_tr_sc, X_te_sc, y_tr, y_te, sc


# ═══════════════════════════════════════════════════════════
# HELPER — KPI Row
# ═══════════════════════════════════════════════════════════
def kpi_row(cards):
    """cards = [(label, value, css_class), ...]"""
    html = '<div class="kpi-row">'
    for i, (lbl, val, cls) in enumerate(cards):
        delay = min(i * 0.08, 0.5)
        html += f'''<div class="kpi-card {cls}" style="animation-delay: {delay}s; opacity: 0;">
            <div class="val">{val}</div>
            <div class="lbl">{lbl}</div>
        </div>'''
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════
# HELPER — Insight Callout
# ═══════════════════════════════════════════════════════════
def insight(text):
    st.markdown(f'<div class="insight"> {text}</div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════
# HELPER — Section Title
# ═══════════════════════════════════════════════════════════
def section_title(text):
    st.markdown(f'<div class="sec-title"><div class="bar"></div>{text}</div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════
# HELPER — Plotly dark template config
# ═══════════════════════════════════════════════════════════
PLOTLY_TEMPLATE = "plotly_dark"
PLOTLY_BG = "rgba(6, 8, 15, 0)"
PLOTLY_GRID = "rgba(148, 163, 184, 0.06)"
PLOTLY_FONT = "#94a3b8"

def style_fig(fig, height=420):
    """Apply consistent dark theme to Plotly figures."""
    fig.update_layout(
        paper_bgcolor=PLOTLY_BG,
        plot_bgcolor=PLOTLY_BG,
        font=dict(family="Inter, sans-serif", color=PLOTLY_FONT, size=12),
        height=height,
        margin=dict(l=50, r=30, t=60, b=50),
    )
    fig.update_xaxes(gridcolor=PLOTLY_GRID, zerolinecolor=PLOTLY_GRID)
    fig.update_yaxes(gridcolor=PLOTLY_GRID, zerolinecolor=PLOTLY_GRID)
    return fig


# ═══════════════════════════════════════════════════════════
# BUILD DASHBOARD
# ═══════════════════════════════════════════════════════════
def build_dashboard():

    # ── Load data & train models ──
    with st.spinner("Loading data & training models…"):
        df, df_raw, source, encoders = load_and_prepare()

        FEATURES = ["Platform_enc","Genre_enc","Publisher_enc","Year",
                     "Decade","Is_Top_Publisher","Platform_Age","Genre_Frequency"]
        results, preds, fitted, best_name, X_tr_sc, X_te_sc, y_tr, y_te, scaler = \
            train_models(df, FEATURES, "Global_Sales")

    best_r2   = results[best_name]["R²"]
    best_rmse = results[best_name]["RMSE"]

    # ──────────────────────────────────────────────
    # SIDEBAR
    # ──────────────────────────────────────────────
    with st.sidebar:
        # Branding
        st.markdown("""
        <div class="sidebar-brand">
            <div class="sidebar-brand-name">🤖 ML <span>Regression</span></div>
            <div class="sidebar-brand-tag">Video Game Sales Predictor</div>
        </div>
        """, unsafe_allow_html=True)

        # Status
        st.markdown(f"""
        <div class="sidebar-status">
            <div class="dot dot-green"></div>
            {source}
        </div>
        <div class="sidebar-status">
            <div class="dot dot-blue"></div>
            {len(df):,} clean rows loaded
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)

        # Filters
        st.markdown("**Filters**")

        all_platforms = sorted(df["Platform"].unique())
        sel_platforms = st.multiselect("Platforms", all_platforms,
                                       default=all_platforms[:6])

        all_genres = sorted(df["Genre"].unique())
        sel_genres = st.multiselect("Genres", all_genres,
                                    default=all_genres)

        yr_min, yr_max = int(df["Year"].min()), int(df["Year"].max())
        yr_range = st.slider("Year Range", yr_min, yr_max, (2000, 2015))

        # Apply filters
        dff = df[
            df["Platform"].isin(sel_platforms) &
            df["Genre"].isin(sel_genres) &
            df["Year"].between(yr_range[0], yr_range[1])
        ]

        # Model Info
        st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)
        st.markdown("**Model Info**")
        st.markdown(f"""
        <div class="sidebar-info">
            <div class="sidebar-info-row">
                <span class="label">Models</span>
                <span class="value">{len(fitted)}</span>
            </div>
            <div class="sidebar-info-row">
                <span class="label">Best Model</span>
                <span class="value" style="color: var(--accent-cyan);">{best_name}</span>
            </div>
            <div class="sidebar-info-row">
                <span class="label">Best R²</span>
                <span class="value">{best_r2:.4f}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Dataset Stats
        st.markdown("**Dataset Stats**")
        st.markdown(f"""
        <div class="sidebar-info">
            <div class="sidebar-info-row">
                <span class="label">Filtered Rows</span>
                <span class="value">{len(dff):,}</span>
            </div>
            <div class="sidebar-info-row">
                <span class="label">Genres</span>
                <span class="value">{dff['Genre'].nunique()}</span>
            </div>
            <div class="sidebar-info-row">
                <span class="label">Platforms</span>
                <span class="value">{dff['Platform'].nunique()}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Footer
        st.markdown("""
        <div class="sidebar-footer">
            <p>ML Regression Dashboard</p>
            <p>© 2024 Data Science Project</p>
        </div>
        """, unsafe_allow_html=True)

    # ──────────────────────────────────────────────
    # HEADER
    # ──────────────────────────────────────────────
    st.markdown('<h1 class="ml-header">ML Regression Dashboard</h1>',
                unsafe_allow_html=True)
    st.markdown('<p class="ml-sub">'
                'Predicting Video Game Global Sales with Machine Learning Models'
                '</p>', unsafe_allow_html=True)

    # ── KPI Cards ──
    kpi_row([
        ("Games",       f"{len(dff):,}",                    "kpi-green"),
        ("Total Sales", f"${dff['Global_Sales'].sum():.0f}M", "kpi-blue"),
        ("Avg Sales",   f"{dff['Global_Sales'].mean():.2f}M",  "kpi-purple"),
        ("Models",      str(len(fitted)),                     "kpi-pink"),
        ("Best R²",     f"{best_r2:.4f}",                     "kpi-orange"),
        ("Best RMSE",   f"{best_rmse:.4f}",                   "kpi-teal"),
    ])

    st.markdown('<hr class="colored-divider">', unsafe_allow_html=True)

    # ──────────────────────────────────────────────
    # TABS
    # ──────────────────────────────────────────────
    tab_overview, tab_eda, tab_train, tab_eval, tab_feat, tab_pred, tab_dash = \
        st.tabs([
            "Overview",
            "EDA",
            "Training",
            "Evaluation",
            "Features",
            "Predict",
            "Dashboard",
        ])

    # ══════════════════════════════════════════════
    # TAB 1 — OVERVIEW
    # ══════════════════════════════════════════════
    with tab_overview:
        section_title("Dataset Overview")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="glass-card anim-fade-up">', unsafe_allow_html=True)
            st.markdown("**Raw Data Sample**")
            st.dataframe(df_raw.head(8), use_container_width=True, hide_index=True)
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="glass-card anim-fade-up anim-delay-1">', unsafe_allow_html=True)
            st.markdown("**Cleaned Data Sample**")
            st.dataframe(dff.head(8), use_container_width=True, hide_index=True)
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<hr class="colored-divider">', unsafe_allow_html=True)

        # Data Quality Report
        section_title("Data Quality Report")
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            st.metric("Raw Rows", f"{len(df_raw):,}")
        with col_b:
            st.metric("Clean Rows", f"{len(df):,}")
        with col_c:
            st.metric("Rows Removed", f"{len(df_raw) - len(df):,}")

        # Missing value bar chart
        missing_raw = df_raw.isnull().sum()
        missing_raw = missing_raw[missing_raw > 0]
        if len(missing_raw) > 0:
            fig_miss = px.bar(x=missing_raw.index, y=missing_raw.values,
                              title="Missing Values by Column (Raw Data)",
                              labels={"x": "Column", "y": "Missing Count"},
                              color=missing_raw.values,
                              color_continuous_scale="Viridis",
                              template=PLOTLY_TEMPLATE)
            style_fig(fig_miss)
            st.plotly_chart(fig_miss, use_container_width=True)

        st.markdown('<hr class="colored-divider">', unsafe_allow_html=True)

        section_title("Summary Statistics")
        st.dataframe(dff.describe().round(3), use_container_width=True)

    # ══════════════════════════════════════════════
    # TAB 2 — EDA
    # ══════════════════════════════════════════════
    with tab_eda:
        section_title("Exploratory Data Analysis")

        # ── Distribution ──
        col1, col2 = st.columns(2)
        with col1:
            fig_hist = px.histogram(dff, x="Global_Sales", nbins=80,
                                     title="Global Sales Distribution",
                                     color_discrete_sequence=["#6366f1"],
                                     template=PLOTLY_TEMPLATE)
            fig_hist.update_xaxes(range=[0, 5])
            style_fig(fig_hist)
            st.plotly_chart(fig_hist, use_container_width=True)
        with col2:
            dff_copy = dff.copy()
            dff_copy["Log_Sales"] = np.log1p(dff_copy["Global_Sales"])
            fig_log = px.histogram(dff_copy, x="Log_Sales", nbins=50,
                                    title="Log-Transformed Sales",
                                    color_discrete_sequence=["#8b5cf6"],
                                    template=PLOTLY_TEMPLATE)
            style_fig(fig_log)
            st.plotly_chart(fig_log, use_container_width=True)

        insight("The sales distribution is heavily right-skewed. Most games sell less than 1M copies, "
                "while a few blockbusters sell tens of millions.")

        st.markdown('<hr class="colored-divider">', unsafe_allow_html=True)

        # ── Genre ──
        col1, col2 = st.columns(2)
        with col1:
            gc = dff["Genre"].value_counts().reset_index()
            gc.columns = ["Genre", "Count"]
            fig_gc = px.bar(gc, x="Genre", y="Count",
                            title="Games by Genre",
                            color="Count", color_continuous_scale="Viridis",
                            template=PLOTLY_TEMPLATE)
            fig_gc.update_xaxes(tickangle=-45)
            style_fig(fig_gc)
            st.plotly_chart(fig_gc, use_container_width=True)
        with col2:
            ga = dff.groupby("Genre")["Global_Sales"].mean().reset_index()
            ga.columns = ["Genre", "Avg_Sales"]
            fig_ga = px.bar(ga, x="Genre", y="Avg_Sales",
                            title="Avg Sales by Genre",
                            color="Avg_Sales", color_continuous_scale="Plasma",
                            template=PLOTLY_TEMPLATE)
            fig_ga.update_xaxes(tickangle=-45)
            style_fig(fig_ga)
            st.plotly_chart(fig_ga, use_container_width=True)

        insight("Action has the most titles, but Platform and Shooter tend to have the highest average sales.")

        st.markdown('<hr class="colored-divider">', unsafe_allow_html=True)

        # ── Platform ──
        ps = dff.groupby("Platform")["Global_Sales"].sum().nlargest(15).reset_index()
        fig_plat = px.bar(ps, x="Platform", y="Global_Sales",
                          title="Total Sales by Platform (Top 15)",
                          color="Global_Sales", color_continuous_scale="Teal",
                          template=PLOTLY_TEMPLATE)
        style_fig(fig_plat)
        st.plotly_chart(fig_plat, use_container_width=True)

        st.markdown('<hr class="colored-divider">', unsafe_allow_html=True)

        # ── Regional ──
        regions = {"North America": dff["NA_Sales"].sum(),
                   "Europe": dff["EU_Sales"].sum(),
                   "Japan": dff["JP_Sales"].sum(),
                   "Other": dff["Other_Sales"].sum()}
        fig_reg = px.pie(names=list(regions.keys()), values=list(regions.values()),
                         title="Market Share by Region", hole=0.45,
                         color_discrete_sequence=["#ef4444","#3b82f6","#f59e0b","#10b981"],
                         template=PLOTLY_TEMPLATE)
        style_fig(fig_reg, height=440)
        st.plotly_chart(fig_reg, use_container_width=True)

        st.markdown('<hr class="colored-divider">', unsafe_allow_html=True)

        # ── Sales over time ──
        yearly = dff.groupby("Year").agg({"Global_Sales": "sum", "Name": "count"}).reset_index()
        yearly.columns = ["Year", "Total_Sales", "Games"]
        yearly = yearly[(yearly["Year"] >= 1990) & (yearly["Year"] <= 2020)]

        fig_yr = make_subplots(rows=1, cols=2,
                                subplot_titles=("Total Sales", "Games Released"))
        fig_yr.add_trace(go.Scatter(x=yearly["Year"], y=yearly["Total_Sales"],
                                     fill="tozeroy", fillcolor="rgba(99,102,241,0.12)",
                                     line=dict(color="#6366f1", width=2.5), name="Sales"),
                         row=1, col=1)
        fig_yr.add_trace(go.Bar(x=yearly["Year"], y=yearly["Games"],
                                 marker_color="#a855f7", name="Games"),
                         row=1, col=2)
        fig_yr.update_layout(title_text="Industry Trends Over Time",
                             template=PLOTLY_TEMPLATE, showlegend=False)
        style_fig(fig_yr, height=420)
        st.plotly_chart(fig_yr, use_container_width=True)

        insight("The industry peaked around 2008-2009 with the PS2/Wii/X360 generation.")

        st.markdown('<hr class="colored-divider">', unsafe_allow_html=True)

        # ── Correlation heatmap ──
        corr_cols = ["Year","NA_Sales","EU_Sales","JP_Sales","Other_Sales",
                     "Global_Sales","Platform_enc","Genre_enc","Publisher_enc"]
        corr = dff[corr_cols].corr()
        fig_corr = px.imshow(corr, text_auto=".2f",
                              title="Correlation Heatmap",
                              color_continuous_scale="RdBu_r",
                              aspect="auto", template=PLOTLY_TEMPLATE)
        style_fig(fig_corr, height=560)
        st.plotly_chart(fig_corr, use_container_width=True)

    # ══════════════════════════════════════════════
    # TAB 3 — MODEL TRAINING
    # ══════════════════════════════════════════════
    with tab_train:
        section_title("Model Training Summary")

        # Target & Features
        col1, col2 = st.columns(2)
        with col1:
            st.info("**Target**: `Global_Sales` — total worldwide sales in millions")
        with col2:
            st.info(f"**Features**: {len(FEATURES)} engineered features")

        st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)

        # Feature list
        feat_desc = {
            "Platform_enc": "Which console the game runs on",
            "Genre_enc": "What type of game it is",
            "Publisher_enc": "Who published the game",
            "Year": "Release year",
            "Decade": "Decade of release (engineered)",
            "Is_Top_Publisher": "Top-10 publisher flag (engineered)",
            "Platform_Age": "Years since platform launch (engineered)",
            "Genre_Frequency": "Genre proportion in dataset (engineered)",
        }
        for feat, desc in feat_desc.items():
            st.markdown(f'<div class="feat-item"><code>{feat}</code> — {desc}</div>', unsafe_allow_html=True)

        st.markdown('<hr class="colored-divider">', unsafe_allow_html=True)

        # Models Trained
        section_title("Models Trained")

        model_info = {
            "Linear Regression": ("Linear", "Baseline — assumes a straight-line relationship"),
            "Decision Tree": ("Tree", "Splits data into regions using decision rules"),
            "Random Forest": ("Ensemble", "Many decision trees voting together"),
            "Gradient Boosting": ("Boosting", "Sequential trees that learn from mistakes"),
            "Extra Trees": ("Ensemble", "Extremely randomized tree ensemble"),
            "XGBoost": ("Boosting", "Extreme gradient boosting — industry standard"),
        }

        model_cols = st.columns(3)
        for i, (name, info_tuple) in enumerate(model_info.items()):
            if name in results:
                badge_cls = {"Linear":"badge-linear","Tree":"badge-tree",
                             "Ensemble":"badge-ensemble","Boosting":"badge-boost"
                            }[info_tuple[0]]
                delay_cls = f"anim-delay-{(i % 6) + 1}"
                model_cols[i % 3].markdown(f"""
                <div class="model-card {delay_cls}">
                    <div class="name">{name} <span class="badge {badge_cls}">{info_tuple[0]}</span></div>
                    <div class="desc">{info_tuple[1]}</div>
                    <div class="metrics">R² = {results[name]['R²']:.4f} &nbsp;|&nbsp; RMSE = {results[name]['RMSE']:.4f}</div>
                </div>
                """, unsafe_allow_html=True)

        st.markdown('<hr class="colored-divider">', unsafe_allow_html=True)

        # ML Pipeline
        section_title("ML Pipeline")
        pipe_steps = [
            ("1", "Load Data", "URL or synthetic fallback"),
            ("2", "Clean", "Drop missing, dedup, fix types"),
            ("3", "Encode", "LabelEncoder for categorical features"),
            ("4", "Engineer", "Decade, Top Pub, Age, Freq"),
            ("5", "Split", "80% train / 20% test, StandardScaler"),
            ("6", "Train", "Fit all regression models"),
            ("7", "Evaluate", "MAE, RMSE, R², cross-validation"),
        ]
        pipe_cols = st.columns(len(pipe_steps))
        for j, (num, title, desc) in enumerate(pipe_steps):
            pipe_cols[j].markdown(f"""
            <div class="pipe-step" style="animation-delay: {j * 0.07}s;">
                <div class="num">{num}</div>
                <div class="title">{title}</div>
                <div class="desc">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    # ══════════════════════════════════════════════
    # TAB 4 — MODEL EVALUATION
    # ══════════════════════════════════════════════
    with tab_eval:
        section_title("Model Evaluation")

        # Leaderboard table
        res_df = pd.DataFrame(results).T
        res_df = res_df.sort_values("R²", ascending=False)
        res_df["Rank"] = range(1, len(res_df) + 1)

        st.markdown("**Leaderboard**")
        st.dataframe(res_df[["Rank","MAE","RMSE","R²","CV R²","CV Std"]].round(4),
                     use_container_width=True)

        st.markdown('<hr class="colored-divider">', unsafe_allow_html=True)

        # Comparison bar charts
        section_title("Metric Comparison")
        model_names = list(res_df.index)
        r2_v   = [results[n]["R²"]   for n in model_names]
        rmse_v = [results[n]["RMSE"] for n in model_names]
        mae_v  = [results[n]["MAE"]  for n in model_names]

        clrs = ["#6366f1","#8b5cf6","#a855f7","#ec4899","#f43f5e","#f97316"]

        fig_cmp = make_subplots(1, 3,
                                subplot_titles=("R² Score (↑ better)",
                                                "RMSE (↓ better)",
                                                "MAE (↓ better)"))
        fig_cmp.add_trace(go.Bar(x=model_names, y=r2_v,
                                  marker_color=clrs[:len(model_names)],
                                  text=[f"{v:.4f}" for v in r2_v],
                                  textposition="outside", name="R²"), row=1, col=1)
        fig_cmp.add_trace(go.Bar(x=model_names, y=rmse_v,
                                  marker_color=clrs[:len(model_names)],
                                  text=[f"{v:.4f}" for v in rmse_v],
                                  textposition="outside", name="RMSE"), row=1, col=2)
        fig_cmp.add_trace(go.Bar(x=model_names, y=mae_v,
                                  marker_color=clrs[:len(model_names)],
                                  text=[f"{v:.4f}" for v in mae_v],
                                  textposition="outside", name="MAE"), row=1, col=3)
        fig_cmp.update_layout(title_text="Model Performance Comparison",
                              title_font_size=18, showlegend=False,
                              template=PLOTLY_TEMPLATE)
        fig_cmp.update_xaxes(tickangle=-30)
        style_fig(fig_cmp, height=440)
        st.plotly_chart(fig_cmp, use_container_width=True)

        insight(f"**{best_name}** achieves the best R² of {best_r2:.4f}. "
                "Ensemble methods outperform simple Linear Regression.")

        st.markdown('<hr class="colored-divider">', unsafe_allow_html=True)

        # Predicted vs Actual (best model)
        section_title("Predicted vs Actual")
        bp = preds[best_name]

        fig_pa = px.scatter(x=y_te, y=bp, opacity=0.35,
                             title=f"{best_name} — Predicted vs Actual",
                             labels={"x": "Actual (M)", "y": "Predicted (M)"},
                             color_discrete_sequence=["#6366f1"],
                             template=PLOTLY_TEMPLATE)
        fig_pa.add_shape(type="line", x0=0, y0=0, x1=10, y1=10,
                          line=dict(color="#ef4444", width=2, dash="dash"))
        fig_pa.update_xaxes(range=[0,10])
        fig_pa.update_yaxes(range=[0,10])
        style_fig(fig_pa, height=500)
        st.plotly_chart(fig_pa, use_container_width=True)

        insight("Points near the red dashed line are accurate predictions. "
                "The model predicts average games well but struggles with blockbusters.")

        st.markdown('<hr class="colored-divider">', unsafe_allow_html=True)

        # Residual plots
        section_title("Residual Analysis")
        resid = y_te - bp
        fig_res = px.scatter(x=bp, y=resid, opacity=0.3,
                              title=f"{best_name} — Residuals",
                              labels={"x": "Predicted (M)", "y": "Residual"},
                              color_discrete_sequence=["#f97316"],
                              template=PLOTLY_TEMPLATE)
        fig_res.add_hline(y=0, line_dash="dash", line_color="#ef4444")
        fig_res.update_xaxes(range=[0,5])
        fig_res.update_yaxes(range=[-5,5])
        style_fig(fig_res)
        st.plotly_chart(fig_res, use_container_width=True)

        col1, col2 = st.columns(2)
        with col1:
            fig_rdist = px.histogram(x=resid, nbins=60,
                                      title="Residual Distribution",
                                      color_discrete_sequence=["#f97316"],
                                      template=PLOTLY_TEMPLATE)
            style_fig(fig_rdist)
            st.plotly_chart(fig_rdist, use_container_width=True)
        with col2:
            bins = pd.cut(bp, bins=[0,0.3,0.5,1,2,5], labels=["0-.3",".3-.5",".5-1","1-2","2-5"])
            fig_rbox = px.box(x=bins.astype(str), y=resid,
                               title="Residuals by Prediction Bin",
                               labels={"x":"Predicted Bin (M)","y":"Residual"},
                               color_discrete_sequence=["#8b5cf6"],
                               template=PLOTLY_TEMPLATE)
            style_fig(fig_rbox)
            st.plotly_chart(fig_rbox, use_container_width=True)

    # ══════════════════════════════════════════════
    # TAB 5 — FEATURE IMPORTANCE
    # ══════════════════════════════════════════════
    with tab_feat:
        section_title("Feature Importance")

        feat_names = FEATURES

        # Let user pick model
        tree_models = {n: m for n, m in fitted.items() if hasattr(m, "feature_importances_")}
        sel_model = st.selectbox("Select model:", list(tree_models.keys()), index=0)

        imp = tree_models[sel_model].feature_importances_
        fi_df = pd.DataFrame({"Feature": feat_names, "Importance": imp})
        fi_df = fi_df.sort_values("Importance", ascending=True)

        fig_fi = px.bar(fi_df, x="Importance", y="Feature", orientation="h",
                         title=f"{sel_model} — Feature Importance",
                         color="Importance", color_continuous_scale="Viridis",
                         template=PLOTLY_TEMPLATE)
        style_fig(fig_fi, height=500)
        st.plotly_chart(fig_fi, use_container_width=True)

        insight(f"Publisher, Platform, and Genre are the strongest predictors in {sel_model}.")

        st.markdown('<hr class="colored-divider">', unsafe_allow_html=True)

        # Compare feature importance across ALL tree models
        section_title("All Models — Feature Importance Comparison")
        for name, mdl in tree_models.items():
            imp2 = mdl.feature_importances_
            fi2 = pd.DataFrame({"Feature": feat_names, "Importance": imp2})
            fi2 = fi2.sort_values("Importance", ascending=True)
            fig2 = px.bar(fi2, x="Importance", y="Feature", orientation="h",
                           title=f"{name}", color="Importance",
                           color_continuous_scale="Plasma",
                           template=PLOTLY_TEMPLATE)
            style_fig(fig2, height=350)
            st.plotly_chart(fig2, use_container_width=True)

    # ══════════════════════════════════════════════
    # TAB 6 — PREDICTIONS
    # ══════════════════════════════════════════════
    with tab_pred:
        section_title("Interactive Predictions")

        st.markdown("""
        <div class="glass-card anim-fade-up">
            <div style="font-size: 0.9rem; font-weight: 600; color: var(--text-primary); margin-bottom: 12px;">
                Predict Global Sales for a New Game
            </div>
            <div style="font-size: 0.82rem; color: var(--text-muted); margin-bottom: 8px;">
                Adjust the features below and see predicted sales from all models.
            </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        with col1:
            plat_choices = list(encoders["Platform"].classes_)
            sel_plat = st.selectbox("Platform", plat_choices, index=0)
            plat_enc = encoders["Platform"].transform([sel_plat])[0]

            genre_choices = list(encoders["Genre"].classes_)
            sel_genre = st.selectbox("Genre", genre_choices, index=0)
            genre_enc = encoders["Genre"].transform([sel_genre])[0]

        with col2:
            pub_choices = list(encoders["Publisher"].classes_)
            sel_pub = st.selectbox("Publisher", pub_choices, index=0)
            pub_enc = encoders["Publisher"].transform([sel_pub])[0]

            sel_year = st.slider("Year", 1980, 2023, 2010)

        with col3:
            decade = (sel_year // 10) * 10
            is_top = 1 if sel_pub in df.groupby("Publisher")["Global_Sales"].sum().nlargest(10).index else 0
            launch_yr = df[df["Platform"] == sel_plat]["Year"].min()
            plat_age = sel_year - launch_yr if pd.notna(launch_yr) else 0
            gen_freq = (df["Genre"] == sel_genre).mean()

            st.markdown(f"""
            <div class="eng-features">
                <div class="eng-feat-item">
                    <div class="ef-label">Decade</div>
                    <div class="ef-value">{decade}</div>
                </div>
                <div class="eng-feat-item">
                    <div class="ef-label">Top Publisher</div>
                    <div class="ef-value" style="color: {'var(--accent-emerald)' if is_top else 'var(--text-muted)'};">{'Yes' if is_top else 'No'}</div>
                </div>
                <div class="eng-feat-item">
                    <div class="ef-label">Platform Age</div>
                    <div class="ef-value">{plat_age} yrs</div>
                </div>
                <div class="eng-feat-item">
                    <div class="ef-label">Genre Freq</div>
                    <div class="ef-value">{gen_freq:.3f}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)  # close glass-card

        # Build feature vector
        features_vec = np.array([[plat_enc, genre_enc, pub_enc, sel_year,
                                   decade, is_top, plat_age, gen_freq]])
        features_sc = scaler.transform(features_vec)

        # Predict with all models
        st.markdown('<hr class="colored-divider">', unsafe_allow_html=True)
        section_title("Predictions from All Models")

        avg_sales = dff['Global_Sales'].mean()
        pred_cols = st.columns(len(fitted))
        for i, (name, mdl) in enumerate(fitted.items()):
            pred_val = mdl.predict(features_sc)[0]
            delta = pred_val - avg_sales
            delta_cls = "positive" if delta >= 0 else "negative"
            delta_sign = "+" if delta >= 0 else ""
            pred_cols[i % len(fitted)].markdown(f"""
            <div class="pred-metric anim-scale" style="animation-delay: {i * 0.07}s; opacity: 0;">
                <div class="model-name">{name}</div>
                <div class="pred-val">{pred_val:.2f}M</div>
                <div class="pred-delta"><span class="{delta_cls}">{delta_sign}{delta:.2f}M vs avg</span></div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown('<hr class="colored-divider">', unsafe_allow_html=True)
        insight(f"The average game in this dataset sells {avg_sales:.2f}M copies. "
                "Predictions above the average suggest higher commercial potential.")

    # ══════════════════════════════════════════════
    # TAB 7 — FULL DASHBOARD
    # ══════════════════════════════════════════════
    with tab_dash:
        section_title("Complete Analytics Dashboard")

        # ── Sunburst ──
        sun_data = dff.groupby(["Genre","Platform"])["Global_Sales"].sum().reset_index()
        top_g = dff["Genre"].value_counts().head(8).index
        sun_data = sun_data[sun_data["Genre"].isin(top_g)]

        fig_sun = px.sunburst(sun_data, path=["Genre","Platform"],
                               values="Global_Sales",
                               title="Sales Sunburst — Genre → Platform",
                               color="Global_Sales",
                               color_continuous_scale="RdYlBu",
                               template=PLOTLY_TEMPLATE)
        style_fig(fig_sun, height=620)
        st.plotly_chart(fig_sun, use_container_width=True)

        st.markdown('<hr class="colored-divider">', unsafe_allow_html=True)

        # ── Regional trends ──
        yr_agg = dff.groupby("Year").agg({
            "NA_Sales": "sum", "EU_Sales": "sum",
            "JP_Sales": "sum", "Other_Sales": "sum", "Global_Sales": "sum"
        }).reset_index()
        yr_agg = yr_agg[(yr_agg["Year"] >= 1990) & (yr_agg["Year"] <= 2020)]

        fig_rt = go.Figure()
        for col, clr, nm in [("NA_Sales","#ef4444","North America"),
                              ("EU_Sales","#3b82f6","Europe"),
                              ("JP_Sales","#f59e0b","Japan"),
                              ("Other_Sales","#10b981","Other"),
                              ("Global_Sales","#6366f1","Global")]:
            fig_rt.add_trace(go.Scatter(x=yr_agg["Year"], y=yr_agg[col],
                                         mode="lines+markers", name=nm,
                                         line=dict(color=clr, width=2)))
        fig_rt.update_layout(title="Regional Sales Trends",
                              template=PLOTLY_TEMPLATE, height=450)
        style_fig(fig_rt, height=450)
        st.plotly_chart(fig_rt, use_container_width=True)

        st.markdown('<hr class="colored-divider">', unsafe_allow_html=True)

        # ── Top publishers bubble ──
        pub_st = dff.groupby("Publisher").agg(
            Total=("Global_Sales","sum"),
            Avg=("Global_Sales","mean"),
            Games=("Name","count")
        ).reset_index()
        pub_st = pub_st[pub_st["Games"] >= 30].nlargest(15, "Total")

        fig_bub = px.scatter(pub_st, x="Games", y="Avg", size="Total",
                              color="Total", hover_name="Publisher",
                              color_continuous_scale="Plasma",
                              title="Publishers — Games vs Avg Sales (bubble = total)",
                              labels={"Games": "Number of Games",
                                      "Avg": "Avg Sales per Game (M)"},
                              template=PLOTLY_TEMPLATE)
        style_fig(fig_bub, height=520)
        st.plotly_chart(fig_bub, use_container_width=True)

        st.markdown('<hr class="colored-divider">', unsafe_allow_html=True)

        # ── All models predicted vs actual ──
        section_title("All Models — Predicted vs Actual")
        n_models = len(preds)
        ncols = 3
        fig_all = make_subplots(rows=(n_models + ncols - 1) // ncols, cols=ncols,
                                 subplot_titles=list(preds.keys()))

        r, c = 1, 1
        for name, yp in preds.items():
            idx = (r - 1) * ncols + (c - 1)
            fig_all.add_trace(go.Scatter(x=y_te, y=yp, mode="markers",
                                          marker=dict(size=3, opacity=0.25,
                                                      color=clrs[idx % len(clrs)]),
                                          name=name),
                               row=r, col=c)
            fig_all.add_shape(type="line", x0=0, y0=0, x1=10, y1=10,
                               line=dict(color="#ef4444", width=1, dash="dash"),
                               row=r, col=c)
            fig_all.update_xaxes(range=[0,10], row=r, col=c)
            fig_all.update_yaxes(range=[0,10], row=r, col=c)
            c += 1
            if c > ncols:
                c = 1
                r += 1

        fig_all.update_layout(height=300 * ((n_models + ncols - 1) // ncols),
                               showlegend=False, template=PLOTLY_TEMPLATE)
        fig_all.update_layout(
            paper_bgcolor=PLOTLY_BG,
            plot_bgcolor=PLOTLY_BG,
            font=dict(family="Inter, sans-serif", color=PLOTLY_FONT, size=11),
        )
        st.plotly_chart(fig_all, use_container_width=True)

        st.markdown('<hr class="colored-divider">', unsafe_allow_html=True)

        # ── Leaderboard table (Plotly) ──
        rows_t = []
        for n in res_df.index:
            rows_t.append({
                "Rank": int(res_df.loc[n,"Rank"]),
                "Model": n,
                "R²": f"{results[n]['R²']:.4f}",
                "RMSE": f"{results[n]['RMSE']:.4f}",
                "MAE": f"{results[n]['MAE']:.4f}",
                "CV R²": f"{results[n]['CV R²']:.4f}"
            })
        tdf = pd.DataFrame(rows_t)

        fig_tbl = go.Figure(data=[go.Table(
            header=dict(values=list(tdf.columns),
                        fill_color="#0c1120",
                        font=dict(color="#06b6d4", size=13, family="Inter"),
                        align="center", height=42,
                        line=dict(color="rgba(148,163,184,0.08)")),
            cells=dict(values=[tdf[c] for c in tdf.columns],
                       fill_color="#111827",
                       font=dict(color="#f1f5f9", size=12, family="Inter"),
                       align="center", height=36,
                       line=dict(color="rgba(148,163,184,0.06)"))
        )])
        fig_tbl.update_layout(title="Final Model Leaderboard",
                               title_font_size=18,
                               template=PLOTLY_TEMPLATE, height=380)
        fig_tbl.update_layout(
            paper_bgcolor=PLOTLY_BG,
            font=dict(family="Inter, sans-serif", color=PLOTLY_FONT),
        )
        st.plotly_chart(fig_tbl, use_container_width=True)

    # ──────────────────────────────────────────────
    # FOOTER
    # ──────────────────────────────────────────────
    st.markdown("""
    <div class="app-footer">
        <p>ML Regression Dashboard — Data Science Course Project</p>
        <div class="tech-stack">
            <span class="tech-tag">Streamlit</span>
            <span class="tech-tag">Plotly</span>
            <span class="tech-tag">scikit-learn</span>
            <span class="tech-tag">XGBoost</span>
            <span class="tech-tag">Pandas</span>
            <span class="tech-tag">NumPy</span>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ───────────────────────────────────────────────────────────
# Entry Point
# ───────────────────────────────────────────────────────────
if __name__ == "__main__":
    build_dashboard()