#!/usr/bin/env python3
"""
Performance Visualization Script
=================================

Creates visual charts of the trading performance data.

Usage:
    python visualize_performance.py

Requirements:
    pip install pandas matplotlib numpy
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

def create_equity_curve(df, output_file='equity_curve.png'):
    """Create equity curve visualization"""
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))
    
    # Main equity curve
    ax1.plot(df['date'], df['account_value_usd'] / 1e6, 
             linewidth=2.5, color='#FF8F00', label='Account Value')
    ax1.set_title('Claude Quant - Live Simulation Equity Curve', 
                  fontsize=16, fontweight='bold', pad=20)
    ax1.set_ylabel('Account Value ($M)', fontsize=12, fontweight='bold')
    ax1.grid(alpha=0.3, linestyle='--')
    ax1.legend(fontsize=11)
    
    # Add starting value line
    starting_value = df.iloc[0]['account_value_usd'] / 1e6
    ax1.axhline(y=starting_value, color='gray', linestyle='--', 
                alpha=0.5, label=f'Starting: ${starting_value:.1f}M')
    
    # Format y-axis
    ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:.1f}M'))
    
    # Daily returns
    colors = ['green' if x > 0 else 'red' for x in df['daily_return_pct']]
    ax2.bar(df['date'], df['daily_return_pct'], color=colors, alpha=0.7)
    ax2.set_title('Daily Returns', fontsize=14, fontweight='bold', pad=15)
    ax2.set_xlabel('Date', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Daily Return (%)', fontsize=12, fontweight='bold')
    ax2.axhline(y=0, color='black', linewidth=0.8)
    ax2.grid(alpha=0.3, linestyle='--', axis='y')
    
    # Rotate x-axis labels
    for ax in [ax1, ax2]:
        ax.tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"✓ Equity curve saved: {output_file}")
    
    return fig

def create_distribution_chart(df, output_file='return_distribution.png'):
    """Create return distribution histogram"""
    
    fig, ax = plt.subplots(figsize=(12, 7))
    
    # Histogram
    n, bins, patches = ax.hist(df['daily_return_pct'], bins=20, 
                                edgecolor='black', alpha=0.7)
    
    # Color bars
    for i, patch in enumerate(patches):
        if bins[i] < 0:
            patch.set_facecolor('red')
        else:
            patch.set_facecolor('green')
    
    # Add mean line
    mean_return = df['daily_return_pct'].mean()
    ax.axvline(x=mean_return, color='blue', linestyle='--', 
               linewidth=2, label=f'Mean: {mean_return:+.2f}%')
    
    # Add zero line
    ax.axvline(x=0, color='black', linewidth=1)
    
    ax.set_title('Daily Return Distribution', 
                 fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel('Daily Return (%)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Frequency', fontsize=12, fontweight='bold')
    ax.legend(fontsize=11)
    ax.grid(alpha=0.3, axis='y', linestyle='--')
    
    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"✓ Distribution chart saved: {output_file}")
    
    return fig

def create_drawdown_chart(df, output_file='drawdown.png'):
    """Create drawdown visualization"""
    
    # Calculate drawdown
    returns = df['daily_return_pct'] / 100
    cumulative = (1 + returns).cumprod()
    running_max = cumulative.expanding().max()
    drawdown = ((cumulative / running_max) - 1) * 100
    
    fig, ax = plt.subplots(figsize=(14, 6))
    
    ax.fill_between(df['date'], drawdown, 0, 
                     color='red', alpha=0.3, label='Drawdown')
    ax.plot(df['date'], drawdown, color='darkred', linewidth=2)
    
    # Mark maximum drawdown
    max_dd_idx = drawdown.idxmin()
    max_dd_date = df.loc[max_dd_idx, 'date']
    max_dd_value = drawdown[max_dd_idx]
    ax.scatter([max_dd_date], [max_dd_value], 
               color='darkred', s=100, zorder=5)
    ax.annotate(f'Max DD: {max_dd_value:.2f}%', 
                xy=(max_dd_date, max_dd_value),
                xytext=(10, -20), textcoords='offset points',
                fontsize=11, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.7))
    
    ax.set_title('Drawdown Analysis', fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel('Date', fontsize=12, fontweight='bold')
    ax.set_ylabel('Drawdown (%)', fontsize=12, fontweight='bold')
    ax.grid(alpha=0.3, linestyle='--')
    ax.tick_params(axis='x', rotation=45)
    ax.legend(fontsize=11)
    
    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"✓ Drawdown chart saved: {output_file}")
    
    return fig

def create_cumulative_returns(df, output_file='cumulative_returns.png'):
    """Create cumulative returns chart"""
    
    returns = df['daily_return_pct'] / 100
    cumulative = ((1 + returns).cumprod() - 1) * 100
    
    fig, ax = plt.subplots(figsize=(14, 7))
    
    ax.plot(df['date'], cumulative, linewidth=2.5, 
            color='#FF8F00', label='Cumulative Return')
    ax.fill_between(df['date'], 0, cumulative, 
                     alpha=0.2, color='#FF8F00')
    
    ax.set_title('Cumulative Returns', fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel('Date', fontsize=12, fontweight='bold')
    ax.set_ylabel('Cumulative Return (%)', fontsize=12, fontweight='bold')
    ax.grid(alpha=0.3, linestyle='--')
    ax.tick_params(axis='x', rotation=45)
    ax.legend(fontsize=11)
    
    # Add final value annotation
    final_return = cumulative.iloc[-1]
    final_date = df.iloc[-1]['date']
    ax.annotate(f'{final_return:+.1f}%', 
                xy=(final_date, final_return),
                xytext=(-50, 20), textcoords='offset points',
                fontsize=12, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='lightgreen', alpha=0.8))
    
    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"✓ Cumulative returns chart saved: {output_file}")
    
    return fig

def main():
    """Generate all visualizations"""
    
    print("\n" + "=" * 60)
    print("CLAUDE QUANT - PERFORMANCE VISUALIZATION")
    print("=" * 60 + "\n")
    
    print("Loading data...")
    
    try:
        df = pd.read_csv('data/live_simulation_dec3_jan16.csv')
        df['date'] = pd.to_datetime(df['date'])
    except FileNotFoundError:
        print("ERROR: Could not find data/live_simulation_dec3_jan16.csv")
        print("Please run this script from the repository root directory.")
        return
    
    print(f"Loaded {len(df)} days of data\n")
    print("Creating visualizations...\n")
    
    # Create all charts
    create_equity_curve(df)
    create_distribution_chart(df)
    create_drawdown_chart(df)
    create_cumulative_returns(df)
    
    print("\n" + "=" * 60)
    print("✅ All visualizations created successfully!")
    print("=" * 60 + "\n")
    
    print("Generated files:")
    print("  - equity_curve.png")
    print("  - return_distribution.png")
    print("  - drawdown.png")
    print("  - cumulative_returns.png")
    print()

if __name__ == "__main__":
    # Set style
    plt.style.use('seaborn-v0_8-darkgrid')
    main()
