from rich import print
from rich.panel import Panel
import logging
import os

LOG_PATH = "logs/springer.log"


def banner():
    print(Panel.fit(
        "🎭 DEVOPS SPRINGER CLI\n[italic]Where pipelines come to fight[/italic]",
        style="bold magenta"
    ))


def setup_logger():
    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger("springer")
    logger.setLevel(logging.INFO)

    # limpa handlers antigos (evita duplicação sempre)
    if logger.hasHandlers():
        logger.handlers.clear()

    file_handler = logging.FileHandler(LOG_PATH)
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger
