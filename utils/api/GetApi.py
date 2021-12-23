import ctypes
import os
import platform
import random

import requests
from colorama import Fore


welcomer = f"""{Fore.LIGHTBLUE_EX}
   ██████╗ ██╗ ██████╗     ██████╗  █████╗ ███╗   ██╗███████╗██╗     
   ██╔══██╗██║██╔════╝     ██╔══██╗██╔══██╗████╗  ██║██╔════╝██║     
   ██████╔╝██║██║  ███╗    ██████╔╝███████║██╔██╗ ██║█████╗  ██║     
   ██╔═══╝ ██║██║   ██║    ██╔═══╝ ██╔══██║██║╚██╗██║██╔══╝  ██║     
   ██║     ██║╚██████╔╝    ██║     ██║  ██║██║ ╚████║███████╗███████╗
   ╚═╝     ╚═╝ ╚═════╝     ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝
       {Fore.CYAN}v1.2 {Fore.RESET}| https://github.com/oyzipfile/Discord.Tools                                             
   """

choiceList2 = f"""
    {Fore.LIGHTBLUE_EX}[1]{Fore.RESET} Get info from token           | {Fore.LIGHTBLUE_EX}[6]{Fore.RESET} Tokens generator            | {Fore.LIGHTBLUE_EX}[11]{Fore.RESET} Token nuker
    {Fore.LIGHTBLUE_EX}[2]{Fore.RESET} Check token or webhook        | {Fore.LIGHTBLUE_EX}[7]{Fore.RESET} Gifts generator             | {Fore.LIGHTBLUE_EX}[12]{Fore.RESET} ...
    {Fore.LIGHTBLUE_EX}[3]{Fore.RESET} Send message to webhook       | {Fore.LIGHTBLUE_EX}[8]{Fore.RESET} Bio generator               | {Fore.LIGHTBLUE_EX}[13]{Fore.RESET} ...
    {Fore.LIGHTBLUE_EX}[4]{Fore.RESET} Destroy the webhook           | {Fore.LIGHTBLUE_EX}[9]{Fore.RESET} Random text generator       | {Fore.LIGHTBLUE_EX}[14]{Fore.RESET} ...
    {Fore.LIGHTBLUE_EX}[5]{Fore.RESET} Account info backup           | {Fore.LIGHTBLUE_EX}[10]{Fore.RESET} Custom status              | {Fore.LIGHTBLUE_EX}[15]{Fore.RESET} ...                    
"""


prefix = f'{Fore.LIGHTBLUE_EX}[█]{Fore.RESET} '


def setUserAgent():
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
    return headers


def setHeaders(token=None):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
    if token:
        headers.update({"Authorization": token})
    return headers


def setHeadersContent(token=None, content_type="application/json"):
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
    if token:
        headers.update({"Authorization": token})
    return headers


def genc(symbols, length):
    return ''.join(random.choice(symbols) for _ in range(length))


def checkToken(token):
    res = requests.get('https://discord.com/api/v9/users/@me', headers=setHeaders(token))
    if res.status_code == 200:
        print(f"{prefix}Token is valid")
        return True
    else:
        print(f"{prefix}Token is invalid")
        return False


def checkWebhook(webhook):
    res = requests.get(
        'https://canary.discord.com/api/webhooks/' + webhook.replace('https://canary.discord.com/api/webhooks/', ''),
        headers=setUserAgent())
    if res.status_code == 200:
        print(f"{prefix}Webhook is valid")
        return True
    else:
        print(f"{prefix}Webhook is invalid")
        return False

def setTitle():
    system = platform.system()
    if system == 'Windows':
        ctypes.windll.kernel32.SetConsoleTitleW("P I G - P A N E L")
    else:
        os.system("P I G - P A N E L")


