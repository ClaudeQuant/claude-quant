# Strategy Methodology

## High-Level Overview

The Princeton Anomaly exploits systematic inefficiencies in global futures markets through time-zone arbitrage, adaptive risk management, and conditional position sizing.

---

## Core Strategy Components

### 1. Time-Zone Arbitrage

**Concept:** Trade three global futures markets sequentially across 24-hour trading day

**Markets:**
- **Nikkei 225** (Japan) - Asia session
- **DAX** (Germany) - Europe session  
- **Nasdaq 100** (US) - US session

**Edge:**
- Information flow across time zones
- Session transition patterns
- Cross-market correlation exploitation

---

### 2. VIX-Based Risk Management

**Concept:** Dynamically adjust position sizes based on market volatility

**Four Volatility Regimes:**

| VIX Level | Position Sizing |
|-----------|----------------|
| < 15 | Full sizing |
| 15-20 | Modest reduction |
| 20-30 | Significant reduction |
| > 30 | Minimal sizing |

**Portfolio-Level Controls:**
- Hard daily loss limit (trading ceases)
- Per-market exposure caps
- Dynamic sizing adjustments

---

### 3. Conditional Position Expansion

**Concept:** Increase position limits when Nikkei session is profitable

**Position Sizing Framework:**

**Standard Allocation (Nikkei Negative):**
- Nikkei: Moderate long bias / Conservative short sizing
- DAX: Conservative long allocation / Minimal short exposure  
- Nasdaq: Balanced directional limits

**Expanded Allocation (Nikkei Positive):**
- DAX: Increased long limit (~2x standard)
- Nasdaq: Enhanced long limit (~2x standard)

**Note:** Exact position sizing parameters are proprietary. Values shown represent relative sizing relationships.

---

## Risk Framework

### Multi-Layer Protection

**Layer 1:** Portfolio-level hard stop
**Layer 2:** Per-market exposure limits  
**Layer 3:** VIX-adaptive sizing
**Layer 4:** Conditional expansion controls

---

## Signal Generation

**Note:** Signal methodology is proprietary.

### General Approach
- Technical indicator combinations
- Pattern recognition
- Statistical arbitrage
- Machine learning enhancement

---

## What's Public vs Proprietary

**Public (GitHub):**
- Session sequencing framework
- VIX-adaptive approach
- Conditional expansion theory
- Performance verification data

**Proprietary:**
- Exact position sizing values
- Signal generation algorithms  
- Entry/exit trigger logic
- Specific indicator combinations

---

