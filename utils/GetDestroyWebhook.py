import requests

from utils.api.GetApi import checkWebhook, prefix


def destroyTheWebhook():
    webhook = input(f"{prefix}Webhook: ")
    if not checkWebhook(webhook):
        return
    requests.delete(webhook)