"""
Apple Inc (AAPL) — Financial Intelligence & Strategic Analysis
==============================================================
Data sourced from Apple's official SEC 10-K annual filings (FY2020–FY2025).
Run this script to regenerate all 4 charts in /assets/.

Usage:
    pip install -r requirements.txt
    python analysis.py
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import os

os.makedirs('assets', exist_ok=True)

# ── Dark GitHub-style theme ────────────────────────────────────────────────
plt.rcParams.update({
    'figure.facecolor': '#0d1117', 'axes.facecolor': '#161b22',
    'axes.edgecolor': '#30363d', 'axes.labelcolor': '#e6edf3',
    'xtick.color': '#8b949e', 'ytick.color': '#8b949e',
    'text.color': '#e6edf3', 'grid.color': '#21262d', 'grid.linewidth': 0.6,
    'font.family': 'DejaVu Sans', 'axes.titlesize': 12,
    'axes.titleweight': 'bold', 'axes.titlecolor': '#e6edf3', 'axes.titlepad': 10,
})
BLUE = '#2f81f7'; GREEN = '#3fb950'; RED = '#f85149'; AMBER = '#d29922'
PURPLE = '#a371f7'; TEAL = '#39d353'; MUTED = '#8b949e'

# ══════════════════════════════════════════════════════════════════════════
# DATA — Apple Inc Official SEC 10-K Filings (FY2020–FY2025)
# All values in $USD Billions unless noted
# Sources: investor.apple.com, SEC EDGAR
# ══════════════════════════════════════════════════════════════════════════
years = [2020, 2021, 2022, 2023, 2024, 2025]

# ── Revenue by Product Segment ($B) ───────────────────────────────────────
iphone    = [137.78, 191.97, 205.49, 200.58, 201.18, 209.59]
mac       = [ 28.62,  35.19,  40.18,  29.36,  29.98,  33.71]
ipad      = [ 23.72,  31.86,  29.29,  28.30,  26.69,  28.02]
wearables = [ 30.62,  38.37,  41.24,  39.85,  37.01,  35.69]
services  = [ 53.77,  68.43,  78.13,  85.20,  96.17, 109.16]
total_rev = [274.52, 365.82, 394.33, 383.29, 391.04, 416.16]

# ── P&L Summary ($B) ──────────────────────────────────────────────────────
gross_profit = [104.96, 152.84, 170.78, 169.15, 180.68, 195.20]
op_income    = [ 66.29, 108.95, 119.44, 114.30, 123.22, 133.05]
net_income   = [ 57.41,  94.68,  99.80,  96.99, 101.96, 111.96]
rd_expense   = [ 18.75,  21.91,  26.25,  29.92,  31.37,  31.37]

# ── Margin (%) ────────────────────────────────────────────────────────────
gross_margin = [38.23, 41.78, 43.31, 44.13, 46.21, 46.91]
op_margin    = [24.15, 29.78, 30.29, 29.82, 31.51, 31.97]
net_margin   = [20.91, 25.88, 25.31, 25.31, 26.08, 26.92]
svc_gm       = [66.0,  69.7,  72.4,  70.8,  73.9,  75.0 ]
prod_gm      = [31.5,  35.3,  36.3,  36.5,  37.2,  36.8 ]

# ── Regional Revenue ($B) ─────────────────────────────────────────────────
americas      = [124.56, 153.31, 169.66, 162.56, 167.00, 176.09]
europe        = [ 68.64,  89.31,  95.12,  94.29, 101.33, 108.19]
greater_china = [ 40.31,  68.37,  74.20,  72.56,  70.97,  66.95]
japan         = [ 21.42,  28.48,  25.98,  24.26,  25.05,  25.31]
rest_apac     = [ 19.59,  26.36,  29.38,  29.62,  26.69,  39.62]

# ── Market Capitalisation ($T, approx year-end) ───────────────────────────
mktcap = [2.26, 2.91, 2.37, 2.99, 3.45, 3.67]


# ══════════════════════════════════════════════════════════════════════════
# CHART 1 — Executive Overview
# ══════════════════════════════════════════════════════════════════════════
fig, axes = plt.subplots(2, 3, figsize=(20, 11))
fig.patch.set_facecolor('#0d1117')
fig.suptitle('Apple Inc (AAPL) — Executive Financial Overview  FY2020–FY2025',
             fontsize=17, fontweight='bold', color='#e6edf3', y=0.98)

x = np.arange(len(years)); w = 0.38

# Revenue & Net Income bars
ax = axes[0, 0]
ax.bar(x - w/2, total_rev, w, color=BLUE, alpha=0.9, label='Revenue')
ax.bar(x + w/2, net_income, w, color=GREEN, alpha=0.9, label='Net Income')
ax.set_xticks(x); ax.set_xticklabels(years, fontsize=9)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f'${v:.0f}B'))
ax.set_title('Revenue & Net Income ($B)'); ax.grid(axis='y', alpha=0.5); ax.legend(fontsize=9)
for i, (r, n) in enumerate(zip(total_rev, net_income)):
    ax.text(i - w/2, r + 4, f'${r:.0f}B', ha='center', fontsize=7.5, color=BLUE)
    ax.text(i + w/2, n + 4, f'${n:.0f}B', ha='center', fontsize=7.5, color=GREEN)

# Triple-margin lines
ax = axes[0, 1]
ax.plot(years, gross_margin, 'o-', color=BLUE, lw=2.2, ms=7, label='Gross Margin')
ax.plot(years, op_margin, 's-', color=GREEN, lw=2.2, ms=7, label='Operating Margin')
ax.plot(years, net_margin, '^-', color=AMBER, lw=2.2, ms=7, label='Net Margin')
ax.fill_between(years, gross_margin, alpha=0.08, color=BLUE)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f'{v:.0f}%'))
ax.set_title('Profitability Margins (%)'); ax.grid(axis='y', alpha=0.5); ax.legend(fontsize=9)
ax.set_ylim(15, 55)

# YoY Growth %
ax = axes[0, 2]
growth = [0] + [(total_rev[i] - total_rev[i-1]) / total_rev[i-1] * 100 for i in range(1, len(years))]
bar_colors = [GREEN if g >= 0 else RED for g in growth[1:]]
ax.bar(years[1:], growth[1:], color=bar_colors, alpha=0.9)
ax.axhline(0, color=MUTED, lw=1)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f'{v:.0f}%'))
ax.set_title('YoY Revenue Growth'); ax.grid(axis='y', alpha=0.5)
for yr, g in zip(years[1:], growth[1:]):
    ax.text(yr, g + (1.5 if g >= 0 else -3), f'{g:.1f}%',
            ha='center', fontsize=9, fontweight='bold',
            color=GREEN if g >= 0 else RED)

# Stacked Area — Product Revenue
ax = axes[1, 0]
ax.stackplot(years, [iphone, services, wearables, mac, ipad],
    labels=['iPhone', 'Services', 'Wearables', 'Mac', 'iPad'],
    colors=[BLUE, GREEN, PURPLE, AMBER, TEAL], alpha=0.85)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f'${v:.0f}B'))
ax.set_title('Revenue by Product Segment — Stacked ($B)')
ax.legend(fontsize=8, loc='upper left'); ax.grid(axis='y', alpha=0.3)

# Services vs Products GM
ax = axes[1, 1]
ax.plot(years, svc_gm, 'o-', color=GREEN, lw=2.5, ms=8, label='Services GM')
ax.plot(years, prod_gm, 's-', color=BLUE, lw=2.5, ms=8, label='Products GM')
ax.fill_between(years, svc_gm, prod_gm, alpha=0.12, color=GREEN, label='Margin gap')
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f'{v:.0f}%'))
ax.set_title('Services vs Products Gross Margin')
ax.legend(fontsize=9); ax.grid(axis='y', alpha=0.5); ax.set_ylim(25, 82)
ax.annotate('Gap: 38pp\n(Services 75% vs\nProducts 37%)',
            xy=(2025, 56), fontsize=8, color='#e6edf3',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#21262d', alpha=0.8))

# Revenue vs Market Cap
ax = axes[1, 2]
ax2 = ax.twinx()
ax.bar(years, total_rev, color=BLUE, alpha=0.7, label='Revenue ($B)')
ax2.plot(years, mktcap, 'o-', color=AMBER, lw=2.5, ms=8, label='Mkt Cap ($T)')
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f'${v:.0f}B'))
ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f'${v:.1f}T'))
ax2.tick_params(colors='#e6edf3')
ax.set_title('Revenue vs Market Capitalisation'); ax.grid(axis='y', alpha=0.3)
lines1, labs1 = ax.get_legend_handles_labels()
lines2, labs2 = ax2.get_legend_handles_labels()
ax.legend(lines1 + lines2, labs1 + labs2, fontsize=9, loc='upper left')

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('assets/01_executive_overview.png', dpi=150, bbox_inches='tight', facecolor='#0d1117')
plt.close()
print("  [1/4] Executive Overview saved.")


# ══════════════════════════════════════════════════════════════════════════
# CHART 2 — Product Segment Deep Dive
# ══════════════════════════════════════════════════════════════════════════
fig, axes = plt.subplots(2, 2, figsize=(18, 12))
fig.patch.set_facecolor('#0d1117')
fig.suptitle('Apple Inc — Product Segment Deep Dive  FY2020–FY2025',
             fontsize=17, fontweight='bold', color='#e6edf3', y=0.99)

# Individual product lines
ax = axes[0, 0]
for (name, vals), color in zip({
    'iPhone': iphone, 'Services': services,
    'Wearables': wearables, 'Mac': mac, 'iPad': ipad
}.items(), [BLUE, GREEN, PURPLE, AMBER, TEAL]):
    ax.plot(years, vals, 'o-', color=color, lw=2.2, ms=7, label=name)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f'${v:.0f}B'))
ax.set_title('Revenue by Product Line ($B)'); ax.legend(fontsize=9); ax.grid(axis='y', alpha=0.5)

# 2025 Revenue Share Donut
ax = axes[0, 1]
shares_2025 = [209.59, 109.16, 35.69, 33.71, 28.02]
labels_2025 = ['iPhone\n50.4%', 'Services\n26.2%', 'Wearables\n8.6%', 'Mac\n8.1%', 'iPad\n6.7%']
ax.pie(shares_2025, labels=labels_2025, colors=[BLUE, GREEN, PURPLE, AMBER, TEAL],
    startangle=90, textprops={'fontsize': 9, 'color': '#e6edf3'},
    wedgeprops={'linewidth': 2, 'edgecolor': '#0d1117'})
ax.add_patch(plt.Circle((0, 0), 0.55, color='#0d1117'))
ax.text(0, 0.07, 'FY2025\n$416B', ha='center', va='center',
        fontsize=11, color='#e6edf3', fontweight='bold')
ax.set_title('Revenue Share by Product — FY2025')

# Services acceleration
ax = axes[1, 0]
svc_share = [s / t * 100 for s, t in zip(services, total_rev)]
ax2 = ax.twinx()
ax.bar(years, services, color=GREEN, alpha=0.8, label='Services Rev ($B)')
ax2.plot(years, svc_share, 'o--', color=AMBER, lw=2.5, ms=8, label='% of Total Revenue')
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f'${v:.0f}B'))
ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f'{v:.0f}%'))
ax2.tick_params(colors='#e6edf3')
ax.set_title('Services: Revenue & Share of Total'); ax.grid(axis='y', alpha=0.3)
lines1, labs1 = ax.get_legend_handles_labels()
lines2, labs2 = ax2.get_legend_handles_labels()
ax.legend(lines1 + lines2, labs1 + labs2, fontsize=9)
for yr, v in zip(years, services):
    ax.text(yr, v + 1.5, f'${v:.0f}B', ha='center', fontsize=8, color=GREEN)

# YoY Growth by Segment
ax = axes[1, 1]
segs_data = {'iPhone': iphone, 'Services': services, 'Mac': mac, 'iPad': ipad, 'Wearables': wearables}
x = np.arange(len(years) - 1)
yr_labels = [f'{years[i]}→{years[i+1]}' for i in range(len(years) - 1)]
bar_w = 0.15
for idx, (name, vals) in enumerate(segs_data.items()):
    growths = [(vals[i+1] - vals[i]) / vals[i] * 100 for i in range(len(vals) - 1)]
    offset = (idx - 2) * bar_w
    clr = [GREEN, BLUE, AMBER, TEAL, PURPLE][idx]
    ax.bar(x + offset, growths, bar_w, color=clr, alpha=0.9, label=name)
ax.axhline(0, color=MUTED, lw=1)
ax.set_xticks(x); ax.set_xticklabels(yr_labels, fontsize=8)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f'{v:.0f}%'))
ax.set_title('YoY Growth by Product Segment (%)'); ax.legend(fontsize=8); ax.grid(axis='y', alpha=0.5)

plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.savefig('assets/02_product_segments.png', dpi=150, bbox_inches='tight', facecolor='#0d1117')
plt.close()
print("  [2/4] Product Segments saved.")


# ══════════════════════════════════════════════════════════════════════════
# CHART 3 — Regional Analysis
# ══════════════════════════════════════════════════════════════════════════
fig, axes = plt.subplots(2, 2, figsize=(18, 12))
fig.patch.set_facecolor('#0d1117')
fig.suptitle('Apple Inc — Regional Performance & Geographic Strategy  FY2020–FY2025',
             fontsize=17, fontweight='bold', color='#e6edf3', y=0.99)

# Stacked regional area
ax = axes[0, 0]
ax.stackplot(years, [americas, europe, greater_china, rest_apac, japan],
    labels=['Americas', 'Europe', 'Greater China', 'Rest of APAC', 'Japan'],
    colors=[BLUE, GREEN, RED, PURPLE, AMBER], alpha=0.85)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f'${v:.0f}B'))
ax.set_title('Revenue by Region — Stacked ($B)'); ax.legend(fontsize=8, loc='upper left')
ax.grid(axis='y', alpha=0.3)

# 2025 Region Donut
ax = axes[0, 1]
ax.pie([176.09, 108.19, 66.95, 39.62, 25.31],
    labels=['Americas\n42.3%', 'Europe\n26.0%', 'Greater China\n16.1%', 'Rest APAC\n9.5%', 'Japan\n6.1%'],
    colors=[BLUE, GREEN, RED, PURPLE, AMBER], startangle=90,
    textprops={'fontsize': 9, 'color': '#e6edf3'},
    wedgeprops={'linewidth': 2, 'edgecolor': '#0d1117'})
ax.add_patch(plt.Circle((0, 0), 0.55, color='#0d1117'))
ax.text(0, 0, 'FY2025\n$416B', ha='center', va='center',
        fontsize=11, color='#e6edf3', fontweight='bold')
ax.set_title('Revenue Share by Region — FY2025')

# China Risk Chart
ax = axes[1, 0]
china_share = [c / t * 100 for c, t in zip(greater_china, total_rev)]
ax2 = ax.twinx()
ax.bar(years, greater_china, color=RED, alpha=0.8, label='China Revenue ($B)')
ax2.plot(years, china_share, 'o--', color=AMBER, lw=2.5, ms=8, label='% of Total')
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f'${v:.0f}B'))
ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f'{v:.0f}%'))
ax2.tick_params(colors='#e6edf3')
ax.set_title('Greater China: Revenue & % of Total'); ax.grid(axis='y', alpha=0.3)
ax.annotate('⚠ 3-year decline\n(18.7% → 16.1%)',
            xy=(2024, 70.97), xytext=(2022.5, 78), fontsize=9, color=AMBER,
            arrowprops=dict(arrowstyle='->', color=AMBER, lw=1.5),
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#21262d', alpha=0.9))
lines1, labs1 = ax.get_legend_handles_labels()
lines2, labs2 = ax2.get_legend_handles_labels()
ax.legend(lines1 + lines2, labs1 + labs2, fontsize=9)

# Region × Year Heatmap
ax = axes[1, 1]
regions = ['Americas', 'Europe', 'Gr. China', 'Japan', 'Rest APAC']
matrix = np.array([americas, europe, greater_china, japan, rest_apac])
cmap_h = mcolors.LinearSegmentedColormap.from_list('apple', [BLUE, '#161b22', GREEN])
im = ax.imshow(matrix, cmap=cmap_h, aspect='auto')
ax.set_xticks(range(len(years))); ax.set_xticklabels(years, fontsize=9)
ax.set_yticks(range(len(regions))); ax.set_yticklabels(regions, fontsize=9)
for i in range(len(regions)):
    for j in range(len(years)):
        ax.text(j, i, f'${matrix[i, j]:.0f}B',
                ha='center', va='center', fontsize=8.5, fontweight='bold', color='#e6edf3')
plt.colorbar(im, ax=ax, format=lambda x, _: f'${x:.0f}B')
ax.set_title('Revenue Heatmap: Region × Year ($B)')

plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.savefig('assets/03_regional_analysis.png', dpi=150, bbox_inches='tight', facecolor='#0d1117')
plt.close()
print("  [3/4] Regional Analysis saved.")


# ══════════════════════════════════════════════════════════════════════════
# CHART 4 — Investor & Strategic Intelligence
# ══════════════════════════════════════════════════════════════════════════
fig, axes = plt.subplots(2, 2, figsize=(18, 12))
fig.patch.set_facecolor('#0d1117')
fig.suptitle('Apple Inc — Investor & Strategic Intelligence  FY2020–FY2025',
             fontsize=17, fontweight='bold', color='#e6edf3', y=0.99)

# Profit Waterfall
ax = axes[0, 0]
ax.plot(years, gross_profit, 'o-', color=BLUE, lw=2.5, ms=8, label='Gross Profit')
ax.plot(years, op_income, 's-', color=GREEN, lw=2.5, ms=8, label='Operating Income')
ax.plot(years, net_income, '^-', color=AMBER, lw=2.5, ms=8, label='Net Income')
ax.fill_between(years, net_income, alpha=0.1, color=AMBER)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f'${v:.0f}B'))
ax.set_title('Profit Waterfall: Gross → Operating → Net ($B)')
ax.legend(fontsize=9); ax.grid(axis='y', alpha=0.5)
for yr, v in zip(years, net_income):
    ax.text(yr, v - 8, f'${v:.0f}B', ha='center', fontsize=8, color=AMBER)

# R&D Investment
ax = axes[0, 1]
rd_pct = [r / t * 100 for r, t in zip(rd_expense, total_rev)]
ax2 = ax.twinx()
ax.bar(years, rd_expense, color=PURPLE, alpha=0.8, label='R&D Spend ($B)')
ax2.plot(years, rd_pct, 'o--', color=AMBER, lw=2.5, ms=8, label='% of Revenue')
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f'${v:.0f}B'))
ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f'{v:.1f}%'))
ax2.tick_params(colors='#e6edf3')
ax.set_title('R&D Investment — $31B in FY2025'); ax.grid(axis='y', alpha=0.3)
lines1, labs1 = ax.get_legend_handles_labels()
lines2, labs2 = ax2.get_legend_handles_labels()
ax.legend(lines1 + lines2, labs1 + labs2, fontsize=9)

# Services vs Products Gross Margin (annotated)
ax = axes[1, 0]
ax.plot(years, svc_gm, 'o-', color=GREEN, lw=2.8, ms=9, label='Services GM %')
ax.plot(years, prod_gm, 's-', color=BLUE, lw=2.8, ms=9, label='Products GM %')
for yr, s, p in zip(years, svc_gm, prod_gm):
    ax.annotate(f'{s:.0f}%', (yr, s), textcoords='offset points', xytext=(0, 8),
                ha='center', fontsize=8, color=GREEN)
    ax.annotate(f'{p:.0f}%', (yr, p), textcoords='offset points', xytext=(0, -14),
                ha='center', fontsize=8, color=BLUE)
ax.fill_between(years, svc_gm, prod_gm, alpha=0.1, color=GREEN)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f'{v:.0f}%'))
ax.set_title('Services (75%) vs Products (37%) Gross Margin Gap')
ax.legend(fontsize=9); ax.grid(axis='y', alpha=0.5); ax.set_ylim(22, 85)

# Revenue vs Market Cap Bubble
ax = axes[1, 1]
sc = ax.scatter(total_rev, [m * 1000 for m in mktcap],
    s=[n * 8 for n in net_income],
    c=years, cmap='YlGn', alpha=0.85, edgecolors='#30363d', lw=1.5, zorder=3)
for yr, r, m, n in zip(years, total_rev, mktcap, net_income):
    ax.annotate(f'FY{yr}\n${n:.0f}B NI', (r, m * 1000),
        textcoords='offset points', xytext=(8, 4), fontsize=8, color='#e6edf3')
plt.colorbar(sc, ax=ax, label='Fiscal Year')
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f'${v:.0f}B'))
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f'${v:.0f}B'))
ax.set_xlabel('Annual Revenue'); ax.set_ylabel('Market Cap ($B)')
ax.set_title('Revenue vs Market Cap  (bubble size = Net Income)')
ax.grid(alpha=0.4)

plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.savefig('assets/04_investor_strategy.png', dpi=150, bbox_inches='tight', facecolor='#0d1117')
plt.close()
print("  [4/4] Investor Strategy saved.")
print("\nAll 4 charts generated successfully in /assets/")
