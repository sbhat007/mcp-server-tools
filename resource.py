from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Resource Demo")

@mcp.resource("inventory://overview")
def get_inventory_overview() -> str:
    """
    Returns the inventory overview
    :return:
    """

    overview = """
    Inventory Overview:
    - Coffee
    - Tea
    - Cookies
    """

    return overview.strip()

inventory_id_to_price = {
    "123": "6.99",
    "456": "17.99",
    "789": "84.99"
}

inventory_name_to_id = {
    "Coffee": "123",
    "Tea": "456",
    "Cookies": "789"
}

@mcp.resource("inventory://overview/{inventory_id}/price")
def get_inventory_price_from_id(inventory_id: str) -> str:
    """
    Returns price for the given inventory id
    :return:
    """
    return inventory_id_to_price[inventory_id]

@mcp.resource("inventory://overview/{inventory_name}/id")
def get_inventory_id_from_name(inventory_name: str) -> str:
    """
    Returns id for the given inventory name
    :return:
    """

    return inventory_name_to_id[inventory_name]

if __name__ == "__main__":
    mcp.run()