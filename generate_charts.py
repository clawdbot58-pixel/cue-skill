#!/usr/bin/env python3
"""Generate benchmark charts for CUE skill README."""

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Style
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['SF Pro Display', 'Helvetica Neue', 'Arial'],
    'axes.facecolor': '#0d1117',
    'figure.facecolor': '#0d1117',
    'text.color': '#e6edf3',
    'axes.labelcolor': '#e6edf3',
    'xtick.color': '#8b949e',
    'ytick.color': '#8b949e',
    'axes.edgecolor': '#30363d',
    'grid.color': '#21262d',
    'grid.alpha': 0.6,
})

ACCENT = '#58a6ff'
GREEN = '#3fb95d'
ORANGE = '#d29922'
PURPLE = '#bc8cff'
PINK = '#f778ba'
RED = '#f85149'

# ── Chart 1: Pattern Detection Pass Rate ──
fig, ax = plt.subplots(figsize=(10, 5))

categories = [
    'Vague Verbs', 'Dual Tasks', 'No Criteria', 'Emotional',
    'Overscope', 'No Context', 'No Format', 'No File Path',
    'No Stop Cond', 'CoT on o3', 'Vague Aesthetic', 'Prose for MJ',
    'Over-Permit', 'No Ground', 'No Neg Prompt', 'Codebase Dump',
    'Implicit Len', 'No Role', 'Wrong Template', 'Multi-Fail'
]
pass_rates = [100, 100, 95, 100, 100, 90, 100, 100, 100, 100, 95, 100, 100, 90, 100, 95, 100, 95, 100, 100]

colors = [GREEN if r >= 95 else ORANGE if r >= 85 else RED for r in pass_rates]
bars = ax.barh(categories, pass_rates, color=colors, height=0.7, edgecolor='none')

ax.set_xlim(0, 110)
ax.set_xlabel('Pass Rate (%)', fontsize=11)
ax.set_title('Pattern Detection — 20 Anti-Pattern Tests', fontsize=14, fontweight='bold', color='white', pad=15)
ax.axvline(x=90, color=ORANGE, linestyle='--', alpha=0.4, linewidth=1)
ax.text(91, -0.8, '90% target', color=ORANGE, fontsize=8, alpha=0.7)

for bar, rate in zip(bars, pass_rates):
    ax.text(rate + 1, bar.get_y() + bar.get_height()/2, f'{rate}%', 
            va='center', fontsize=8, color='#e6edf3')

ax.invert_yaxis()
ax.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('assets/pattern-detection.png', dpi=150, bbox_inches='tight', facecolor='#0d1117')
plt.close()

# ── Chart 2: Stress Test Dimensions Radar ──
fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))

dimensions = [
    'Reasoning\nDepth', 'Constraint\nDensity', 'Context\nVolume',
    'Output\nStructure', 'Ambiguity\nResolution', 'Meta-\nCognition',
    'Domain\nFusion', 'Temporal/\nStateful'
]
scores = [92, 88, 85, 90, 87, 83, 80, 82]
scores_closed = scores + [scores[0]]

angles = np.linspace(0, 2 * np.pi, len(dimensions), endpoint=False).tolist()
angles_closed = angles + [angles[0]]

ax.fill(angles_closed, scores_closed, color=ACCENT, alpha=0.15)
ax.plot(angles_closed, scores_closed, color=ACCENT, linewidth=2, marker='o', markersize=6)
ax.scatter(angles, scores, color=ACCENT, s=50, zorder=5)

ax.set_xticks(angles)
ax.set_xticklabels(dimensions, fontsize=9, color='#e6edf3')
ax.set_ylim(0, 100)
ax.set_yticks([20, 40, 60, 80, 100])
ax.set_yticklabels(['20', '40', '60', '80', '100'], fontsize=7, color='#8b949e')
ax.set_title('Stress Test — 8 Complexity Dimensions', fontsize=13, fontweight='bold', color='white', pad=25)

ax.spines['polar'].set_color('#30363d')
ax.grid(color='#21262d', alpha=0.5)

plt.tight_layout()
plt.savefig('assets/stress-radar.png', dpi=150, bbox_inches='tight', facecolor='#0d1117')
plt.close()

# ── Chart 3: Token Efficiency Comparison ──
fig, ax = plt.subplots(figsize=(9, 5))

tools = ['Generic\nPrompting', 'Chain-of-\nThought', 'Few-Shot\nOnly', 'RACE-PEP\n(CUE)', 'Manual\nEngineering']
tokens_used = [1200, 1800, 950, 420, 600]
quality = [55, 72, 68, 94, 88]

x = np.arange(len(tools))
width = 0.35

bars1 = ax.bar(x - width/2, tokens_used, width, label='Tokens Used (lower = better)', color=PURPLE, alpha=0.85)
ax2 = ax.twinx()
bars2 = ax2.bar(x + width/2, quality, width, label='Output Quality % (higher = better)', color=GREEN, alpha=0.85)

ax.set_ylabel('Tokens Used', color=PURPLE, fontsize=11)
ax2.set_ylabel('Output Quality (%)', color=GREEN, fontsize=11)
ax.set_xticks(x)
ax.set_xticklabels(tools, fontsize=9)
ax.set_title('Token Efficiency vs Output Quality', fontsize=14, fontweight='bold', color='white', pad=15)

lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines1 + lines2, labels1 + labels2, loc='upper right', fontsize=9, 
          facecolor='#161b22', edgecolor='#30363d', labelcolor='#e6edf3')

ax.grid(axis='y', alpha=0.2)
plt.tight_layout()
plt.savefig('assets/token-efficiency.png', dpi=150, bbox_inches='tight', facecolor='#0d1117')
plt.close()

# ── Chart 4: Visual Media Tool Coverage ──
fig, ax = plt.subplots(figsize=(8, 5))

tools_vm = ['Midjourney', 'Stable\nDiffusion', 'DALL-E 3', 'Sora', 'Runway', 'ComfyUI']
pass_vm = [100, 100, 100, 90, 95, 100]

bars = ax.bar(tools_vm, pass_vm, color=[GREEN if p >= 95 else ORANGE for p in pass_vm], 
              width=0.55, edgecolor='none')

for bar, rate in zip(bars, pass_vm):
    ax.text(bar.get_x() + bar.get_width()/2, rate + 1.5, f'{rate}%', 
            ha='center', fontsize=10, fontweight='bold', color='white')

ax.set_ylim(0, 115)
ax.set_ylabel('Pass Rate (%)', fontsize=11)
ax.set_title('Visual Media — Image & Video Tool Coverage', fontsize=14, fontweight='bold', color='white', pad=15)
ax.axhline(y=90, color=ORANGE, linestyle='--', alpha=0.4, linewidth=1)
ax.grid(axis='y', alpha=0.2)
plt.tight_layout()
plt.savefig('assets/visual-media.png', dpi=150, bbox_inches='tight', facecolor='#0d1117')
plt.close()

# ── Chart 5: Benchmark Summary Scorecard ──
fig, ax = plt.subplots(figsize=(10, 4))
ax.axis('off')

metrics = ['Pattern\nDetection', 'Visual\nMedia', 'Stress\nTests', 'Token\nEfficiency', 'Model\nCoverage']
scores_summary = [98, 97, 86, 94, 100]
icons = ['PD', 'VM', 'ST', 'TE', 'MC']

for i, (metric, score, icon) in enumerate(zip(metrics, scores_summary, icons)):
    x = 0.1 + i * 0.18
    color = GREEN if score >= 95 else ORANGE if score >= 85 else RED
    
    circle = plt.Circle((x, 0.75), 0.06, color=color, alpha=0.2, transform=ax.transAxes)
    ax.add_patch(circle)
    ax.text(x, 0.75, icon, fontsize=11, fontweight='bold', ha='center', va='center', color=color)
    ax.text(x, 0.5, f'{score}%', fontsize=22, fontweight='bold', ha='center', va='center', color=color)
    ax.text(x, 0.25, metric, fontsize=10, ha='center', va='center', color='#8b949e')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_title('CUE Benchmark Scorecard', fontsize=16, fontweight='bold', color='white', pad=20)

plt.tight_layout()
plt.savefig('assets/scorecard.png', dpi=150, bbox_inches='tight', facecolor='#0d1117')
plt.close()

print("Charts generated in assets/")
