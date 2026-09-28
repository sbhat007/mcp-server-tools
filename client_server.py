from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

# below tools are utilized by client_query.py and client_simple.py
# usually these are exposed to mcp clients like claude or any other client via config.json
# but here these are utilized programmatically by above two files

@mcp.tool()
def get_weather(location: str) -> str:
    """
    Gets weather for given city
    :param
    location: can be city, county or state
    :return:
    """
    return f"The weather for {location} is hot and dry"

@mcp.resource("weather://statement")
def get_weather_statement() -> str:
    """
    Returns the weather statement
    """
    return "This is an example weather statement"

@mcp.resource("weather://{city}/statement")
def get_weather_statement_from_city(city: str) -> str:
    """
        Returns the weather statement based on a particular city
        """
    return f"No special statements for this city: {city}"

@mcp.prompt()
def get_prompt(topic: str) -> str:
    """
    Returns a prompt related to asking for more information on weather concepts about {topic}
    Args:
        topic: the topic to do research on
    """
    return f"Describe the weather concept of {topic}"

if __name__ == "__main__":
    mcp.run()