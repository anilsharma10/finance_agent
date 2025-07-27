# 📊 Simple AI Finance Agent

A minimalist financial analysis agent powered by Claude AI and real-time stock data.

## Features

• Claude AI for financial analysis
• Real-time stock data via YFinance  
• Simple web interface
• No external API dependencies for search

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

## What it does

Ask questions like:
- "Analyze AAPL stock"
- "Should I buy TSLA?"
- "Compare MSFT vs GOOGL"
- "What's happening with Bitcoin?"

The agent will fetch real-time data and give you AI-powered insights.