import clipboard
import os
import sys
from colorama import Fore, init
from requests import get
from typing import List
from termcolor import colored
import threading

init(convert=True)

intro = """
                    Made by REZIZT. I already know your skidding this just admit it
                            Discord : https://discord.gg/XgpXMWk2bG
         ██▓ ███▄    █ ██▒   █▓ ██▓▄▄▄█████▓▓█████   ██████  ██▓███   ██▓     ▒█████   ██▓▄▄▄█████▓
        ▓██▒ ██ ▀█   █▓██░   █▒▓██▒▓  ██▒ ▓▒▓█   ▀ ▒██    ▒ ▓██░  ██▒▓██▒    ▒██▒  ██▒▓██▒▓  ██▒ ▓▒
        ▒██▒▓██  ▀█ ██▒▓██  █▒░▒██▒▒ ▓██░ ▒░▒███   ░ ▓██▄   ▓██░ ██▓▒▒██░    ▒██░  ██▒▒██▒▒ ▓██░ ▒░
        ░██░▓██▒  ▐▌██▒ ▒██ █░░░██░░ ▓██▓ ░ ▒▓█  ▄   ▒   ██▒▒██▄█▓▒ ▒▒██░    ▒██   ██░░██░░ ▓██▓ ░ 
        ░██░▒██░   ▓██░  ▒▀█░  ░██░  ▒██▒ ░ ░▒████▒▒██████▒▒▒██▒ ░  ░░██████▒░ ████▓▒░░██░  ▒██▒ ░ 
        ░▓  ░ ▒░   ▒ ▒   ░ ▐░  ░▓    ▒ ░░   ░░ ▒░ ░▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░░ ▒░▓  ░░ ▒░▒░▒░ ░▓    ▒ ░░   
         ▒ ░░ ░░   ░ ▒░  ░ ░░   ▒ ░    ░     ░ ░  ░░ ░▒  ░ ░░▒ ░     ░ ░ ▒  ░  ░ ▒ ▒░  ▒ ░    ░    
         ▒ ░   ░   ░ ░     ░░   ▒ ░  ░         ░   ░  ░  ░  ░░         ░ ░   ░ ░ ░ ▒   ▒ ░  ░      
         ░           ░      ░   ░              ░  ░      ░               ░  ░    ░ ░   ░           
                           ░                                                                       


                                            [+]1 Vanity changer
                                            [+]2 invite bypass
                                            [+]3 Vanity checker


"""

def changer():
    # legit just gunna use my old code lol hashtag lazy
    
    server = input("Server invite:\n")
    invite = input("new invite name:\n")
    
    gay = "discοrd.gg/" + invite + "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||" + server
    clipboard.copy(gay)

    print('Copyed to clipboard!')
    os.system('cls')
    startMenu()
    
    
def bypass():
    bypass = input("your server invite:\n")
    fart = bypass.replace('discord.gg/', '')
    invite = 'Discord\.gg\/' + fart
    clipboard.copy(invite)
    print('copyed to clipboard')
    os.system('cls')
    startMenu()
    



def check():
    names = []
    with open("invites.txt", "r") as f:
        names = f.read().splitlines()
    for name in names:
        pog = "https://discord.com/api/v8/invites/" + name
   
    req = get(pog)
    status_code = req.status_code
    if status_code == 200:
        print(colored('Invite is taken: ' + name, 'red'))
    elif status_code == 404:
        print(colored('Invite is Free: ' + name, 'green'))
    

    startMenu()
def startMenu():
    print(intro)
    print(f'[{Fore.RED}>{Fore.RESET}] Your choice', end=''); choice = str(input('  :  '))
    if choice == '1':
       os.system('cls')
       changer()

    elif choice == '2':
        os.system('cls')
        bypass()

    elif choice == '3':
        os.system('cls')
        check()



if __name__ == '__main__':
    startMenu()