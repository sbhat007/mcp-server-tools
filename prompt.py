from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Get Prompt")

@mcp.prompt()
def get_prompt(topic: str) -> str:
    """
    Returns a prompt for the given topic that will do a detailed analysis on the topic
    :param topic: the topic to do research on
    :return:
    """

    return f"Do a detailed analysis on the following topic: {topic}"

# in both of these prompts, they are hardcoded. they can be fetched from a reserved prompts inventory by making API calls too!
@mcp.prompt()
def write_detailed_historical_report(topic:str, number_of_paragraphs:int) -> str:
    """
    Writes a detailed historical report
    Args:
        topic: the topic to do research on
        number_of_paragraphs: the number of paragraphs that the main body should be
    """

    prompt = """
    Create a concise research report on the history of {topic}. 
    The report should contain 3 sections: INTRODUCTION, MAIN, and CONCLUSION.
    The MAIN section should be {number_of_paragraphs} paragraphs long. 
    Include a timeline of key events.
    The conclusion should be in bullet points format. 
    """

    prompt = prompt.format(topic=topic, number_of_paragraphs=number_of_paragraphs)

    return prompt

if __name__ == "__main__":
    mcp.run()