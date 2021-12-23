from utils.api.GetApi import prefix, checkToken, checkWebhook


def checkTokenOrWebhook():
    gett = input(f"{prefix}Token or Webhook? [token 1 / webhook 2]: ")
    if gett.lower() == "token" or gett.lower() == "1":
        token = input(f"{prefix}Token: ")
        checkToken(token)

    elif gett.lower() == "webhook" or gett.lower() == "2":
        webhook = input(f"{prefix}Webhook: ")
        webhook = str(webhook)
        checkWebhook(webhook)
    else:
        return
