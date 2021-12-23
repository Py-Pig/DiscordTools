from utils.api.GetApi import prefix, genc


def getGeneratedTokens():
    attempts = int(input(f"{prefix}Attempts: "))
    symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz'
    print("")
    for zk in range(attempts):
        tokens = f"{genc('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 24)}.{genc(symbols, 6)}.{genc(symbols, 27)}"
        print(f"{prefix}{tokens}")