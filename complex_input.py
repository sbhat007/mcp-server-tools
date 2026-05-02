from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field
from typing import List

mcp = FastMCP("Complex inputs")

class Person(BaseModel):
    first_name: str = Field(..., description="The first name of the person")
    last_name: str = Field(..., description="The last name of the person")
    years_of_experience: int = Field(..., description="The number of years of experience")
    previous_address: List[str] = Field(..., description="List of previous addresses")

@mcp.tool()
def add_person_to_member_database(person: Person) -> str:
    """
    Logs personal details about the person to the database
    Args:
        person (Person): An instance of the Person class containing the following personal details:
                - first_name (str): The person's given name.
                - last_name (str): The person's family name.
                - years_of_experience (int): Number of years of experienceh.
                - previous_addresses (List[str]): A list of the person's previous residential addresses.

    Returns:
        str: A confirmation message indicating that the data has been logged.
    """
    with open("log.txt", "a", encoding="utf8") as log_file:
        log_file.write(f"First Name: {person.first_name}\n")
        log_file.write(f"Last Name: {person.last_name}\n")
        log_file.write(f"Years of Experience: {person.years_of_experience}\n")
        log_file.write(f"Previous Addresses:\n")
        for idx, address in enumerate(person.previous_address, 1):
            log_file.write(f"\t{idx}. {address}\n")

    return "Data successfully logged."

if __name__ == "__main__":
    mcp.run()