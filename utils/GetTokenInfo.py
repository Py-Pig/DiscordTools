import requests

from utils.api.GetApi import prefix, checkToken, setHeaders


def getInfoFromToken():
    token = input(prefix + "Token: ")
    if not checkToken(token):
        return

    data = requests.get('https://discord.com/api/v9/users/@me', headers=setHeaders(token)).json()
    data = {"id": data["id"], "name": data["username"], "locale": data["locale"], "checkNsfw": data["nsfw_allowed"],
            "checkMfa": data["mfa_enabled"], "email": data["email"], "phone": data["phone"],
            "verified": data["verified"], "avatar": data["avatar"], "bio": data["bio"]}
    print(
        f"""\n{prefix}ID: {data["id"]} \n{prefix}NAME: {data["name"]} \n{prefix}LOCALE: {data["locale"]} \n{prefix}NSFW: {data["checkNsfw"]} \n{prefix}MFA: {data["checkMfa"]} \n{prefix}EMAIL: {data["email"]} \n{prefix}PHONE: {data["phone"]} \n{prefix}VERIFIED: {data["verified"]} \n{prefix}AVATAR: https://cdn.discordapp.com/avatars/{data["id"]}/{data["avatar"]}.webp \n{prefix}TOKEN: {token}
    """)
    print(prefix + "BIO: " + data["bio"] + "\n")