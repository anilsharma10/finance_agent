# 📊 Claude Finance Agent

A comprehensive financial analysis agent powered by Claude AI with extensive market data capabilities.

## Features

• **Claude 3 Opus** for advanced financial analysis
• **Comprehensive YFinance Integration** with 15+ data sources:
  - Real-time stock prices and fundamentals
  - Historical data and technical analysis
  - Company information and sector data
  - Latest news and earnings information
  - Financial statements (income, balance sheet, cash flow)
  - Options data and institutional holdings
  - Dividends, stock splits, and corporate actions
  - ESG sustainability scores
• **DuckDuckGo Search** for additional market research
• **Professional Web Interface** with markdown support
• **Advanced Financial Ratios** (P/E, P/B, ROE, Debt-to-Equity)

## Quick Start

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Get your Anthropic API key:
   • Sign up at [Anthropic Console](https://console.anthropic.com/)
   • Set your environment variable:

```bash
export ANTHROPIC_API_KEY='your-anthropic-api-key-here'
```

3. Run the agent:
```bash
python main.py
```

4. Open your browser to `http://localhost:8000`

## What it can analyze

Ask comprehensive questions like:
- **Stock Analysis**: "Analyze AAPL stock with technical and fundamental analysis"
- **Investment Decisions**: "Should I buy TSLA? Include risk assessment"
- **Company Comparison**: "Compare MSFT vs GOOGL financial performance"
- **Market Research**: "What's happening with Bitcoin and crypto markets?"
- **Financial Health**: "Analyze Tesla's financial statements and cash flow"
- **Earnings Analysis**: "What were Apple's latest earnings results?"
- **Technical Analysis**: "Show me TSLA's price history and technical indicators"
- **Risk Assessment**: "What are the risks of investing in GameStop?"

## Data Sources

The agent provides access to:
- **Real-time market data** from Yahoo Finance
- **Financial statements** (income, balance sheet, cash flow)
- **Analyst recommendations** and price targets
- **Historical price data** for technical analysis
- **Company news** and earnings calendar
- **Institutional holdings** and insider trading
- **Options data** and volatility metrics
- **ESG scores** and sustainability metrics
- **Dividends** and corporate actions

## Analysis Features

• **Professional financial ratios** and metrics
• **Technical and fundamental analysis**
• **Risk assessment** and balanced recommendations
• **Historical performance** trends
• **News integration** for context
• **Tabular data presentation** for financial metrics
• **Markdown formatting** for clear, readable reports