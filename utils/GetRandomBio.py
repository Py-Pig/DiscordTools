import random
from colorama import Fore

from utils.api.GetApi import prefix, genc


def getGeneratedBio():
    print("")
    print(prefix + "Name: " + genc("lL1!jJ", 32))
    print(prefix + "Bio: " + genc("lL1!jJ", 190))
    print(prefix + "Status: " + genc("lL1!jJ", 128) + "\n")

