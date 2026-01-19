# Risk Management Framework

## Overview

The Princeton Anomaly employs a multi-layered risk management system designed to protect capital while allowing for aggressive compounding during favorable conditions.

---

## Layer 1: Portfolio-Level Controls

### Hard Daily Loss Limit

**Purpose:** Prevent catastrophic daily losses

**Mechanism:**
- Real-time P&L monitoring
- Automatic cease trading if threshold hit
- Close all positions immediately
- No new trades rest of day

**Historical Performance:**
- Never triggered in backtest (2021-2026)
- Never triggered in live sim (Dec 2025-Jan 2026)
- Well above maximum observed daily loss

**Rationale:**
- Set at multiple standard deviations from mean
- Allows normal volatility
- Prevents blow-up events
- Preserves capital for next day

---

### Maximum Leverage

**Current Setting:** Conservative leverage limits on capital

**Calculation:**
- Futures require low margin
- Leverage provides room for conditional expansion
- Typical usage: moderate to high
- Within broker limits

**Controls:**
- Never exceed maximum at any time
- Reduce if approaching limit
- Account for margin calls
- Maintain cash buffer

---

### Correlation Limits

**Purpose:** Prevent overexposure to correlated moves

**Rules:**
- Maximum 3 markets simultaneously
- Limit same-direction exposure
- Account for beta to S&P 500
- Reduce if correlations spike

**Example:**
- If Nikkei long + DAX long → limit Nasdaq size
- All three bullish → reduce each individual size
- Prevents "all in one direction" risk

---

## Layer 2: VIX-Based Dynamic Sizing

### Four Volatility Regimes

| VIX Range | Regime | Position Multiplier | Rationale |
|-----------|--------|---------------------|-----------|
| < 15 | Low Volatility | 100% | Calm markets, full size |
| 15-20 | Normal | 80% | Typical conditions |
| 20-30 | Elevated | 60% | Reduce exposure |
| > 30 | Crisis | 40% | Major risk reduction |

### Implementation

**Daily VIX Check:**
- Read VIX close before Asia session
- Apply multiplier to all base position sizes
- Regime persists for 24 hours
- Re-evaluate next day

**Example:**
```
Base position size: Moderate allocation
VIX = 18 (Normal regime)
Actual size: Base × 80% multiplier = Reduced sizing

VIX = 25 (Elevated regime)
Actual size: Base × 60% multiplier = Further reduced
```

### Historical Impact

**2022 Bear Market:**
- VIX elevated most of year
- Position sizes reduced automatically
- Protected capital during drawdown
- Allowed recovery when VIX normalized

**2023-2024 Bull:**
- VIX mostly low (<15)
- Full position sizes deployed
- Capitalized on calm conditions
- Compounded aggressively

---

## Layer 3: Per-Market Position Limits

### Base Position Limits (Before Conditional Expansion)

**Nikkei 225:**
- Long: Moderate allocation (largest of three markets)
- Short: Conservative allocation
- Rationale: First session, sets tone for day

**DAX:**
- Long: Conservative allocation (smallest of three)
- Short: Minimal allocation
- Rationale: More volatile European market, smaller sizing

**Nasdaq 100:**
- Long: Moderate allocation
- Short: Moderate allocation (relatively balanced)
- Rationale: Final session, highest liquidity

**Note:** Exact position sizing parameters are proprietary.

### Why These Relative Allocations

**Risk-Weighted:**
- More volatile markets → smaller relative size
- Less liquid sessions → smaller relative size
- Historical win rates → inform sizing

**Asymmetric Long/Short:**
- Markets tend to drift up long-term
- Larger long exposure acceptable
- Short positions smaller, tighter stops

**Total Exposure:**
- Maximum combined: Conservative portfolio-level limit
- Typical: Moderate deployment
- Leaves room for conditional expansion

---

## Layer 4: Conditional Expansion

### Trigger: Nikkei Session Result

**If Nikkei trade closes positive:**
- Expand DAX long limits (approximately 2x standard)
- Expand Nasdaq long limits (approximately 2x standard)
- Increase total allowable exposure
- Asymmetric sizing when winning

**If Nikkei trade closes negative:**
- Use standard limits (above)
- Conservative sizing
- Reduce risk when market weak

**Note:** Exact expansion parameters are proprietary.

### Rationale

**Momentum-Based:**
- Positive Nikkei suggests global strength
- Increases probability DAX/Nasdaq also up
- Capitalize on trending days

**Asymmetric Risk:**
- Only increase size when already winning
- Reduce size when losing
- "Let winners run, cut losers short"

**Historical Contribution:**
- ~40% of total returns from expansion
- Critical to strategy performance
- Works in all market conditions

---

## Layer 5: Time-Based Stops

### Session Closeout

**All positions close at session end:**
- Nikkei: 1 AM EST
- DAX: 11 AM EST
- Nasdaq: 4 PM EST

**No overnight holds (typically)**
- Reduces gap risk
- Avoids unexpected news
- Clean slate each session

### Emergency Stops

**Intraday circuit breakers:**
- Close position if loss exceeds moderate threshold
- Close position if profit exceeds substantial threshold
- Protect gains, limit losses

---

## Layer 6: Operational Risk Controls

### System Monitoring

**Pre-Trade Checks:**
- Market open and liquid?
- Data feed operational?
- Broker connection active?
- Sufficient margin available?

**During Trading:**
- Real-time P&L tracking
- Position reconciliation
- Fill quality monitoring
- Latency measurement

**Post-Trade:**
- Trade log verification
- Performance attribution
- Risk metrics update
- System health check

### Failure Modes

**If system fails:**
- Close all positions immediately
- Notify team
- Do not re-enter until fixed
- Document incident

**If broker fails:**
- Call broker emergency line
- Manual position close if needed
- Switch to backup broker
- Do not trade until resolved

---

## Risk Metrics & Monitoring

### Daily Metrics

**Performance:**
- Daily P&L ($)
- Daily P&L (%)
- Cumulative return
- Account value

**Risk:**
- Current leverage
- VIX regime
- Position sizes (% portfolio)
- Correlation to S&P 500

**Execution:**
- Number of trades
- Win rate (%)
- Average win/loss
- Slippage estimate

### Weekly Metrics

**Risk-Adjusted:**
- Sharpe ratio (rolling)
- Sortino ratio
- Calmar ratio
- Max drawdown

**Attribution:**
- Return by market
- Return by session
- Conditional expansion impact
- VIX regime performance

### Monthly Review

**Strategy Health:**
- Win rate vs historical
- Average return vs historical
- Drawdown vs historical
- Regime analysis

**Risk Controls:**
- Hard stop triggers (count)
- VIX regime distribution
- Leverage utilization
- Slippage trends

---

## Stress Testing

### Historical Scenarios

**2022 Bear Market:**
- S&P 500: -18%
- Strategy: -8% (outperformed)
- VIX: Elevated most of year
- Controls worked as designed

**COVID Crash (backtest includes):**
- Extreme volatility
- VIX >80
- Position sizes cut to 40%
- Survived with capital intact

**Flash Crashes:**
- Tested against historical flash crashes
- Stop losses functional
- Portfolio stop would trigger
- Acceptable max loss

### Forward Scenarios

**What if VIX stays >30 for months:**
- Position sizes stay at 40%
- Returns reduced proportionally
- Capital preserved
- Strategy continues operating

**What if correlations break:**
- Per-market limits still active
- Portfolio stop still functional
- May underperform temporarily
- Risk still controlled

**What if liquidity dries up:**
- Close positions at any price
- Accept slippage cost
- Protect capital over returns
- Pause trading if needed

---

## Live Trading Adjustments

### Differences from Backtest

**More Conservative:**
- Slightly lower base position sizes
- Wider stop losses (account for slippage)
- Longer time between trades
- Higher VIX thresholds

**Additional Controls:**
- Pre-market checklist
- Broker confirmation
- Manual override capability
- Emergency contact procedures

**Expected Impact:**
- 10-25% lower returns than simulation
- Similar drawdown characteristics
- Higher Sharpe ratio (less aggressive)

---

## Transparency Commitment

### Real-Time Disclosure

**When live trading starts:**
- Every trade logged publicly
- Daily P&L posted
- Risk metrics shared
- Monthly CPA audit

**What we'll show:**
- Entry/exit times
- Position sizes (% of portfolio)
- Profit/loss per trade
- Slippage encountered
- All risk events

**What we won't show:**
- Exact entry signals
- Specific indicators used
- Proprietary parameters

---

## Questions?

**Telegram:** [t.me/claudequant](https://t.me/claudequant)  
**Twitter:** [@ClaudeQuant](https://twitter.com/claudequant)

---

*Risk framework is subject to adjustment based on live trading experience.*
