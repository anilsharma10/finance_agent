from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.tools.yfinance import YFinanceTools
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.playground import Playground, serve_playground_app

# create the AI finance agent with enhanced YFinance tools
agent = Agent(
    name="claude-finance-agent",
    model=Claude(id="claude-3-5-sonnet-20241022"),
    tools=[
        DuckDuckGoTools(), 
        YFinanceTools(
            # Basic data
            stock_price=True,
            analyst_recommendations=True, 
            stock_fundamentals=True,
            
            # Enhanced data features
            company_info=True,           # Company description, sector, industry
            historical_prices=True,      # Price history for charts/trends
            company_news=True,           # Latest company news
            income_statements=True,      # Income statement data
            key_financial_ratios=True,   # Financial ratios (P/E, P/B, ROE, etc.)
            technical_indicators=True,   # Technical analysis indicators
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
        "Always mention risks and provide balanced analysis.",
        "Use real-time data from your tools to provide current market insights.",
        "When analyzing stocks, always check the latest news and market conditions.",
        "Provide actionable investment recommendations with clear reasoning.",
        "Include both bullish and bearish perspectives in your analysis.",
        "Mention any recent significant events that might impact the stock.",
        "Use current market data to overcome any training data limitations.",
        "Always verify information using your available tools before making recommendations."
    ],
    show_tool_calls=True,
    markdown=True,
)

# UI for finance agent
app = Playground(agents=[agent]).get_app()
if __name__ == "__main__":
    serve_playground_app(app, port=8000)