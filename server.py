from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Remote Server")

# to run this tool you need to add below to your config.json
# for the below to run, need to start remote server at http://127.0.0.1:8000
# "Remote-example": {
#      "command": "/Users/shreenidhi.bhatibm.com/.nvm/versions/node/v20.18.1/bin/npx",
#       "args": [
#       "mcp-remote",
#       "http://127.0.0.1:8000/mcp",
#       "--allow-http"
#       ],
#       "env": {
#           "PATH": "/Users/shreenidhi.bhatibm.com/.nvm/versions/node/v20.18.1/bin:/usr/bin:/bin"
#       }
# }

@mcp.tool()
def greeting(name: str) -> str:
    "Send a greeting message"
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")