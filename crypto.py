from mcp.server.fastmcp import FastMCP
import requests

mcp = FastMCP("Crypto")

@mcp.tool()
def get_crypto_value(crypto: str) -> str:
    """
    Gets the price of a cryptocurrency. use this tool when user queries for the price of any cryptocurrency
    Args:
    crypto: cryptocurrency to get price. eg. bitcoin, ethereum, etc.
    :param crypto:
    :return:
    """
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price"
        params = {"ids": crypto, "vs_currencies": "usd"}
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        price = data.get(crypto.lower(), {}).get("usd")

        if price is not None:
            return f"The price of {crypto} is {price} USD"
        else:
            return f"Price for cryptocurrency {crypto} isn't available"

    except Exception as e:
        return f"Error returning cryptocurrency price: {e}"

if __name__ == "__main__":
    mcp.run()