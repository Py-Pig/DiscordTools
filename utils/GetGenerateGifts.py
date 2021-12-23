from utils.api.GetApi import prefix, genc


def getGeneratedGifts():
    attempts = int(input(f"{prefix}Attempts: "))
    symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz'
    print("")
    for zk in range(attempts):
        gifts = f"https://discord.gift/{genc(symbols, 16)}"
        print(f"{prefix}{gifts}")