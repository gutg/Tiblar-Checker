from colorama import Fore, init
from datetime import datetime
import requests
import aiohttp
import asyncio
import json
import time
import os

os.system('cls')

init()

print(f"""{Fore.LIGHTMAGENTA_EX}
                                  
╔════╗  ╔╗  ╔╗                 ╔╗          ╔╗         
║╔╗╔╗║  ║║  ║║                 ║║          ║║         
╚╝║║╚╝╔╗║╚═╗║║ ╔══╗ ╔═╗    ╔══╗║╚═╗╔══╗╔══╗║║╔╗╔══╗╔═╗
  ║║  ╠╣║╔╗║║║ ╚ ╗║ ║╔╝    ║╔═╝║╔╗║║╔╗║║╔═╝║╚╝╝║╔╗║║╔╝
 ╔╝╚╗ ║║║╚╝║║╚╗║╚╝╚╗║║     ║╚═╗║║║║║║═╣║╚═╗║╔╗╗║║═╣║║ 
 ╚══╝ ╚╝╚══╝╚═╝╚═══╝╚╝     ╚══╝╚╝╚╝╚══╝╚══╝╚╝╚╝╚══╝╚╝                                                       
                                                      
                                                                                     {Fore.RESET}""")

with open('usernames.txt', 'r', encoding='UTF-8', errors='replace') as u:
    usernames = u.read().splitlines()
    all_usernames = len(usernames)
    if all_usernames == 0:
        print(f'{Fore.LIGHTRED_EX} [!] No usernames found!\n Make sure to paste them into usernames.txt and save.{Fore.RESET}')
        quit()

async def check():
    session = requests.Session()
    for username in usernames:
        c = session.get(f'https://tiblar.com/api/v2/users/profile/{username}')
        check = c.status_code
        if check == 404:
            print(f"{Fore.LIGHTGREEN_EX} [+]{Fore.RESET} Available Username found! -> {Fore.LIGHTCYAN_EX}{username}")
            with open('availables.txt','a',encoding='utf8') as f:
                    f.write(f'{username}\n')
        elif check == 200:
            print(f"{Fore.LIGHTRED_EX} [-]{Fore.RESET} Username {username} is taken.")
        elif check == 429:
            print(f"\n{Fore.LIGHTRED_EX} [!]{Fore.RESET} You are being ratelimited! Sleeping for 30 Seconds . . .\n")
            time.sleep(30)
            check()
            return
        else:
            print(f"{Fore.LIGHTRED_EX} [?]{Fore.RESET} Unknown Error . . . - {check}")
    
    print(f"\n{Fore.LIGHTGREEN_EX} Done.{Fore.LIGHTMAGENTA_EX} Available Usernames are saved in {Fore.LIGHTGREEN_EX}available.txt!\n{Fore.LIGHTMAGENTA_EX} Press Enter to exit.{Fore.RESET}\n")
    input()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(check())