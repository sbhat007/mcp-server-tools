from mcp.server.fastmcp import FastMCP
from openai import OpenAI

YOUR_API_KEY = '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'

mcp = FastMCP("Web Search")

# using this tool, you can basically forward your request from MCP client to any other AI models!
@mcp.tool()
def perform_websearch(query: str) -> str:
    """
    Perform a web search using the OpenAI API for a query
    :param query: the query to perform the web search
    :return:
    """

    messages = [
        {
            "role": "system",
            "content": (
                "You are an AI assistant that searches the web and responds to questions"
            ),
        },
        {
            "role": "user",
            "content": (
                query
            ),
        },
    ]

    client = OpenAI(api_key=YOUR_API_KEY, base_url="https://api.perplexity.ai")

    # chat completion without streaming
    response = client.chat.completions.create(
        model="sonar-pro",
        messages=messages,
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    mcp.run()