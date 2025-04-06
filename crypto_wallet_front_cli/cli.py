from rich.console import Console
from rich.prompt import Prompt
from requests import request

# Initialize the console
console = Console()

def check_transaction_status(transaction_id: int) -> str:
    url = "http://localhost:5002/get_transaction_status/" + str(transaction_id)
    try:
        response = request("GET", url)
        if response.status_code == 200:
            return response.json().get("status")
        else:
            raise Exception("Transaction not found")
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        return None

def create_transaction_request(user_id: int, amount: float, currency_from: str, currency_to: str) -> int:
    url = "http://localhost:5002/create_transaction_request"
    data = {
        "user_id": user_id,
        "amount": amount,
        "currency_from": currency_from,
        "currency_to": currency_to
    }
    try:
        response = request("POST", url, json=data)
        if response.status_code == 201:
            return response.json().get("id")
        else:
            raise Exception("Failed to create transaction request")
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        return None



#Example usage (Delete this later)

create_transaction_request_result = create_transaction_request(1, 100.0, "EURC", "USDC")
if create_transaction_request_result:
    console.print(f"[bold green]Transaction Request ID:[/bold green] {create_transaction_request_result}")
    transaction_status = check_transaction_status(create_transaction_request_result)
    if transaction_status:
        console.print(f"[bold green]Transaction Status:[/bold green] {transaction_status}")


# Display a welcome message
console.print("[bold green]Welcome to the Crypto Wallet CLI![/bold green]")
console.print("Please choose an option to proceed:")

# Define a function to make a request to localhost:5002

# Display options
console.print("[1] Conversion")
console.print("[2] Load Balance")


# Wait for user input
choice = Prompt.ask("Enter your choice", choices=["1", "2"])

# Handle user choice
if choice == "1":
    console.print("[bold blue]You selected Conversion.[/bold blue]")
    # Add logic for conversion here
elif choice == "2":
    console.print("[bold blue]You selected Load Balance.[/bold blue]")
    # Add logic for load balance here