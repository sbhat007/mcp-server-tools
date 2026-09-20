from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import asyncio
import traceback

server_params = StdioServerParameters(
    command="uv",
    args=["--directory", "/Users/shreenidhi.bhatibm.com/ai/mcp-server-tools", "run", "client_server.py"],
)

# sample local mcp client that connects to a local mcp server and calls tools, resources and prompts

async def run():
    try:
        print("Starting stdio_client...")
        async with stdio_client(server_params) as (read, write):
            print("Client connected, creating session...")
            async with ClientSession(read, write) as session:

                print("Initializing session...")
                await session.initialize()

                # TOOLS
                print("Listing tools...")
                tools = await session.list_tools()
                print("Available tools:", tools)

                print("Calling tool")
                result = await session.call_tool("get_weather", arguments={"location": "San Francisco"})
                print("Result:", result)

                # RESOURCES
                print("Listing resources...")
                resources = await session.list_resources()
                print("Available resources:", resources)

                print("Listing resource templates...")
                resource_templates = await session.list_resource_templates()
                print("Available resource templates:", resource_templates)

                print("Getting resource...")
                resource = await session.read_resource("weather://statement")
                print(resource)

                print("Getting resource template...")
                resource_template = await session.read_resource("weather://Vancouver/statement")
                print(resource_template)

                # PROMPTS
                print("Listing prompts...")
                prompts = await session.list_prompts()
                print("Available prompt templates:", prompts)

                print("Prompt tool...")
                result = await session.get_prompt("get_prompt", arguments={"topic": "Water Cycle"})
                print("Prompt Result:", result)


    except Exception as e:
        print("An error occurred")
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(run())