from rich import print
import random

SERVICES = ["auth-service", "payment-service", "database"]

def run_chaos():
    victim = random.choice(SERVICES)

    print("\n[bold red]💥 CHAOS MODE ACTIVATED 💥[/bold red]")
    print(f"[yellow]{victim}[/yellow] just collapsed in production")
    print("[red][JERRY][/red] This relationship is broken.")