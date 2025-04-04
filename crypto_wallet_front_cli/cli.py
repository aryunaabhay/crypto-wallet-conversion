from rich.console import Console
from rich.prompt import Prompt

# Initialize the console
console = Console()

# Display a welcome message
console.print("[bold green]Welcome to the Crypto Wallet CLI![/bold green]")
console.print("Please choose an option to proceed:")

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