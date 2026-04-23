import argparse
from .pipeline import plan, apply
from .chaos import run_chaos
from .utils import banner


def run():
    banner()

    parser = argparse.ArgumentParser(
        prog="springer",
        description="DevOps pipeline simulator with emotional damage"
    )

    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("plan", help="Preview pipeline changes")
    subparsers.add_parser("apply", help="Run pipeline")
    subparsers.add_parser("chaos", help="Trigger random failure")

    args = parser.parse_args()

    if args.command == "plan":
        plan()
    elif args.command == "apply":
        apply()
    elif args.command == "chaos":
        run_chaos()
    else:
        parser.print_help()
