import sys, time, os

import colorama
from colorama import Fore

from utils.GetAccountBackup import getTokenBackupInformation
from utils.GetAccountNuker import getAccountNuke
from utils.GetCheckTokenOrWebhook import checkTokenOrWebhook
from utils.GetDestroyWebhook import destroyTheWebhook
from utils.GetGenerateGifts import getGeneratedGifts
from utils.GetGenerateTokens import getGeneratedTokens
from utils.GetMessageWebhook import sendMessageToWebhook
from utils.GetRandomBio import getGeneratedBio
from utils.GetRandomMessage import getRandomMessage
from utils.GetSetCustomStatus import setCustomStatus
from utils.GetTokenInfo import getInfoFromToken
from utils.api.GetApi import *


def doGo():
    input(f"\n{Fore.LIGHTBLUE_EX}[Press enter to continue]")
    os.system('cls')


def main():
    setTitle()
    os.system('cls')
    colorama.init()
    print(welcomer)
    print(choiceList2)
    stage = input(prefix + "Choice: ")
    if stage == 0:
        exit(0)

    if stage == '1':
        getInfoFromToken()
        doGo()
        # get info from token

    elif stage == '2':
        checkTokenOrWebhook()
        doGo()
        # check token or webhook

    elif stage == '3':
        sendMessageToWebhook()
        doGo()
        # send message to webhook

    elif stage == '4':
        destroyTheWebhook()
        doGo()
        # destroy te webhook

    elif stage == '5':
        getTokenBackupInformation()
        doGo()
        # account nuker

    elif stage == '6':
        getGeneratedTokens()
        doGo()
        # generate tokens

    elif stage == '7':
        getGeneratedGifts()
        doGo()
        # generate gifts

    elif stage == '8':
        getGeneratedBio()
        doGo()

    elif stage == '9':
        getRandomMessage()
        doGo()
        # generate random text

    elif stage == '10':
        setCustomStatus()
        doGo()
        # set custom status
    elif stage == '11':
        getAccountNuke()
        doGo()


if __name__ == "__main__":
    while 1:
        try:
            main()
        except KeyboardInterrupt:
            sys.exit()
