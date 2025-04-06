from rich.console import Console
from rich.prompt import Prompt
from requests import request

# Initialize the console
console = Console()

def make_request_to_service(method="GET"):
    url = "http://localhost:5002"
    try:
        response = request(method, url)
        console.print(response.text)
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        return None

make_request_to_service()

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