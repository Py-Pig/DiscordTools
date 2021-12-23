import random
from colorama import Fore

from utils.api.GetApi import prefix, genc


def getRandomMessage():
    symbols = str(input(f"{prefix}Symbols: "))
    length = int(input(f"{prefix}Length: "))
    attempts = int(input(f"{prefix}Attempts: "))
    for z in range(attempts):
        text = genc(symbols, length)
        print(f"{prefix}{text}")
