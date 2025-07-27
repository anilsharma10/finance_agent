from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.tools.yfinance import YFinanceTools
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.playground import Playground, serve_playground_app

# create the AI finance agent
agent = Agent(
    name="claude-finance-agent",
    model=Claude(id="claude-3-opus-20240229"),
    tools=[DuckDuckGoTools(), YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    instructions=["Always use tables to display financial/numerical data. For text data use bullet points and small paragraphs."],
    show_tool_calls=True,
    markdown=True,
)

# UI for finance agent
app = Playground(agents=[agent]).get_app()
if __name__ == "__main__":
    serve_playground_app(app, port=8000)