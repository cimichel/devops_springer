import random

JERRY_LINES = [
    "So you said this was production-ready… that was a lie.",
    "Security!!!",
    "This pipeline is OUT OF CONTROL.",
]

AUDIENCE = [
    "JERRY! JERRY! JERRY!",
    "BOOOOOOOO",
]

DEV_EXCUSES = [
    "It worked on my machine!",
    "We skipped tests for speed...",
]


def jerry():
    return random.choice(JERRY_LINES)


def audience():
    return random.choice(AUDIENCE)


def dev():
    return random.choice(DEV_EXCUSES)
