from utils.api.GetApi import *
import requests


def getTokenBackupInformation():
    token = input(f"{prefix}Token: ")
    # get all friends
    resFriend = requests.get("https://canary.discord.com/api/v8/users/@me/relationships",
                             headers=setHeaders(token)).json()
    resServers = requests.get("https://canary.discord.com/api/v8/users/@me/guilds",
                              headers=setHeaders(token)).json()
    resDms = requests.get("https://canary.discord.com/api/v8/users/@me/channels",
                       headers=setHeaders(token)).json()

    print(f"{prefix}{resFriend}")
    print(f"{prefix}{resServers}")
    print(f"{prefix}{resDms}")
    print(f"\n{prefix}Friends backup: \n")
    for i in resFriend:
        print(f"{prefix}F: {i['user']['username']}#{i['user']['discriminator']} - ID: {i['id']}")
    print(f"\n{prefix}Server backup: \n")
    for i in resServers:
        print(f"{prefix}S: {i['name']} - ID: {i['id']}")
    print(f"\n{prefix}Dms backup: \n")
    for i in resDms:
        print(f"{prefix}{i['recipients']}")


getTokenBackupInformation()
