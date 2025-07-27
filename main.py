from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.tools.yfinance import YFinanceTools
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.playground import Playground, serve_playground_app

# create the AI finance agent with enhanced YFinance tools
agent = Agent(
    name="claude-finance-agent",
    model=Claude(id="claude-3-opus-20240229"),
    tools=[
        DuckDuckGoTools(), 
        YFinanceTools(
            # Basic data (what you already have)
            stock_price=True,
            analyst_recommendations=True, 
            stock_fundamentals=True,
            
            # NEW: Enhanced data features
            company_info=True,           # Company description, sector, industry
            historical_data=True,        # Price history for charts/trends
            news=True,                   # Latest company news
            earnings=True,               # Earnings data and calendar
            financials=True,             # Income statement, balance sheet
            cash_flow=True,              # Cash flow statements
            balance_sheet=True,          # Balance sheet data
            income_statement=True,       # P&L statements
            options=True,                # Options data
            holders=True,                # Institutional/insider holdings
            calendar=True,               # Earnings calendar
            actions=True,                # Dividends, stock splits
            shares=True,                 # Share count data
            sustainability=True,         # ESG scores
        )
    ],
    instructions=[
        "You are a professional financial analyst with access to comprehensive market data.",
        "Always use tables to display financial/numerical data.",
        "For text data use bullet points and small paragraphs.",
        "Include key financial ratios in your analysis (P/E, P/B, ROE, Debt-to-Equity).",
        "Provide both technical and fundamental analysis when possible.",
        "Include recent news and earnings information in your recommendations.",
        "Show historical performance and trends.",
        "Always mention risks and provide balanced analysis."
    ],
    show_tool_calls=True,
    markdown=True,
)

# UI for finance agent
app = Playground(agents=[agent]).get_app()
if __name__ == "__main__":
    serve_playground_app(app, port=8000)