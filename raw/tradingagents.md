# TradingAgents — Raw Source

**URL:** https://tradingagents-ai.github.io/
**Fetched:** 2026-05-05
**Title:** TradingAgents: Multi-Agents LLM Financial Trading Framework

## Abstract
We introduce TradingAgents, a novel stock trading framework inspired by trading firms, utilizing multiple LLM-powered agents with specialized roles such as fundamental, sentiment, and technical analysts, as well as traders with diverse risk profiles. The system features Bull and Bear researchers evaluating market conditions, a risk management team overseeing exposure, and traders integrating insights from debates and historical data to make informed decisions.

## Authors
- Yijia Xiao (UCLA)
- Edward Sun (MIT)
- Di Luo
- Wei Wang

## Key Points

### Roles
- Fundamental Analysts
- Sentiment Analysts
- News Analysts
- Technical Analysts
- Bullish Researchers
- Bearish Researchers
- Trader Agents
- Risk Management Team
- Fund Manager

### Technologies
- ReAct prompting framework
- Multi-modal data (prices, news, social media, technical indicators)
- Structured communication + natural language debates

### Results (June-November 2024 backtest)
- AAPL: +26.6% cumulative return (vs -5.2% Buy&Hold)
- GOOGL: +24.4% (vs 7.8% B&H)
- AMZN: +23.2% (vs 17.1% B&H)
- Sharpe Ratio up to 8.21 (AAPL)
- Max Drawdown 0.91% (AAPL)

### Paper
arXiv:2412.20138 (2024)