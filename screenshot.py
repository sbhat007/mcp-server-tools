from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.utilities.types import Image

import pyautogui
import io

#create mcp server
mcp = FastMCP("Screenshot demo")

@mcp.tool()
def screenshot() -> Image:
    """
    Capture the current screen and return the image. us this tool whenever the user requests a screenshot of their activity
    :return:
    """

    buffer = io.BytesIO()

    # if the file exceeds 1MB, it'll be rejected by the claude
    screenshot = pyautogui.screenshot()
    screenshot.convert("RGB").save(buffer, format="JPEG", quality=60, optimize=True)
    return Image(data=buffer.getvalue(), format="JPEG")

if __name__ == "__main__":
    mcp.run()