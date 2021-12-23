import requests
from utils.api.GetApi import prefix, setHeaders, checkToken


def setCustomStatus():
    token = input(f"{prefix}Token: ")
    if not checkToken(token):
        return

    stat = input(f"{prefix}Status: ")
    requests.patch(
        "https://discord.com/api/v8/users/@me/settings", headers=setHeaders(token),
        json={"custom_status": {"text": "https://github.com/oyzipfile/Discord.Tools"}})
    print(f"{prefix}Custom-Status: {str(stat)}")
