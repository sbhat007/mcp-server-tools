from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Remote Server")

# How does this work?
# 1. Start remote server at http://127.0.0.1:8000 i.e., run this pythin file.
# 2. MCP always exposes server at 8000 by default
# 3. Add below json to your client config.json
# 4. Arguments are important to let the client know to use the mcp that is already running remotely and not to bring up the mcp server on boot up

# to run this tool you need to add below to your config.json

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