# mcp-server-tools
Examples of mcp tools that does below functions - 

1. Forward your request from MCP client to any other AI models
2. Takes screenshot
3. Retrieves price of a given cryptocurrency via API calls to a open source server
4. Constructing object using given list of strings and saving it to a local file - can be enhanced to write to a db

@mcp.resource() examples - claude didn't support to test
@mcp.prompt() examples - claude didn't support to test

How to bring up mcp servers locally with stdio_client w/o mcp client booting it up
How to use openAI as mcp client - our own mcp client

json for 1 - 
~~~
Don't bother as you need openAI key - go purchase it first!
~~~
json for 2 - 
~~~
    "screenshot": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/Users/shreenidhi.bhatibm.com/ai/mcp-server-tools",
        "mcp",
        "run",
        "screenshot.py"
      ]
    }
~~~
json for 3 - 
~~~
"Crypto": {
      "command": "/opt/homebrew/bin/uv",
      "args": [
        "run",
        "--directory",
        "/Users/shreenidhi.bhatibm.com/ai/mcp-server-tools",
        "mcp",
        "run",
        "crypto.py"
      ]
    }
~~~
json for 4 - 
~~~
"Complex-input": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/Users/shreenidhi.bhatibm.com/ai/mcp-server-tools",
        "mcp",
        "run",
        "complex_input.py"
      ]
    }
~~~

