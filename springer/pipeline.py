from rich import print
from rich.console import Console
from rich.panel import Panel
import random
import time

from springer.jerry import jerry, audience, dev
from springer.utils import setup_logger

logger = setup_logger()
console = Console()


def apply():
    console.print(Panel("💅 Executing pipeline drama...", style="bold green"))

    logger.info("Pipeline started")

    print("\n[blue][BUILD][/blue] 🔧 Building...")
    logger.info("Build started")

    time.sleep(1)

    if random.random() < 0.8:
        print("[green][BUILD][/green] ✅ Success")
        logger.info("Build success")
    else:
        print("[red][BUILD][/red] ❌ Failed")
        logger.error("Build failed")
        logger.error(jerry())
        return

    print("\n[blue][TEST][/blue] 🧪 Running tests...")
    logger.info("Tests started")

    time.sleep(1)

    if random.random() < 0.6:
        print("[green][TEST][/green] ✅ Passed")
        logger.info("Tests passed")
    else:
        print("[red][TEST][/red] ❌ Failed")
        logger.error("Tests failed")
        logger.warning(dev())
        return

    print("\n[blue][DEPLOY][/blue] 🚀 Deploying...")
    logger.info("Deploy started")

    time.sleep(1)

    if random.random() < 0.7:
        print("[green][DEPLOY][/green] ✅ Success 🎉")
        logger.info("Deploy success")
    else:
        print("[red][DEPLOY][/red] 💥 Failed")
        logger.error("Deploy failed")
        logger.error(jerry())


def plan():
    print("📋 [PLAN] Reviewing upcoming chaos...\n")

    print("[PLAN] ➕ Something will be deployed")
    print("[PLAN] ⚠️ Tests might fail (as always)")


print("pipeline loaded")
