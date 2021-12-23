import time

import requests

from utils.api.GetApi import prefix, checkWebhook, setUserAgent


def sendMessageToWebhook():
    webhook = input(f"{prefix}Webhook: ")
    if not checkWebhook(webhook):
        return
    msg = input(f"{prefix}Message: ")
    attempts = int(input(f"{prefix}Attempts: "))

    for k in range(attempts):
        time.sleep(float(0.1))
        requests.post(webhook, json={"username": str("DiscordTools"), "content": str(msg)}, headers=setUserAgent())
