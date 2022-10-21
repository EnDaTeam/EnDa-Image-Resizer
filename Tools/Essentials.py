#The EnDa Image Resizer's Essentials

#Import needed modules
import os
from colorama import Fore
from pystyle import Colors,Colorate
import random
import pathlib
import time
from PIL import Image

#Define a space function
def space():
    print()

#Define a clear terminal function
def clearConsole():
    command = "clear"
    if os.name in ("dos","nt"):
        command = "cls"
    os.system(command)

#Define a banner function
def banner(option):
    if int(option) == 1:
        print(Colorate.Horizontal(Colors.green_to_cyan,r"""
___________      ________           .___                                __________              .__                     
\_   _____/ ____ \______ \ _____    |   | _____ _____     ____   ____   \______   \ ____   _____|__|_______ ___________ 
 |    __)_ /    \ |    |  \\__  \   |   |/     \\__  \   / ___\_/ __ \   |       _// __ \ /  ___/  \___   // __ \_  __ \
 |        \   |  \|    `   \/ __ \_ |   |  Y Y  \/ __ \_/ /_/  >  ___/   |    |   \  ___/ \___ \|  |/    /\  ___/|  | \/
/_______  /___|  /_______  (____  / |___|__|_|  (____  /\___  / \___  >  |____|_  /\___  >____  >__/_____ \\___  >__|   
        \/     \/        \/     \/            \/     \//_____/      \/          \/     \/     \/         \/    \/                                                                        
        """,1))
    elif int(option) == 2:
        print(Colorate.Horizontal(Colors.white_to_red,r"""
            (             (                                (                               
            )\ )          )\ )                             )\ )                            
 (         (()/(      )  (()/(    )       )  (  (     (   (()/(   (     (         (   (    
 )\    (    /(_))  ( /(   /(_))  (     ( /(  )\))(   ))\   /(_)) ))\ (  )\  (    ))\  )(   
((_)   )\ )(_))_   )(_)) (_))    )\  ' )(_))((_))\  /((_) (_))  /((_))\((_) )\  /((_)(()\  
| __| _(_/( |   \ ((_)_  |_ _| _((_)) ((_)_  (()(_)(_))   | _ \(_)) ((_)(_)((_)(_))   ((_) 
| _| | ' \))| |) |/ _` |  | | | '  \()/ _` |/ _` | / -_)  |   // -_)(_-<| ||_ // -_) | '_| 
|___||_||_| |___/ \__,_| |___||_|_|_| \__,_|\__, | \___|  |_|_\\___|/__/|_|/__|\___| |_|   
                                            |___/                                                                                                
        """,1))
    elif int(option) == 3:
        print(Colorate.Horizontal(Colors.yellow_to_red,"""
  ______       _____          _____                              _____           _              
 |  ____|     |  __ \        |_   _|                            |  __ \         (_)             
 | |__   _ __ | |  | | __ _    | |  _ __ ___   __ _  __ _  ___  | |__) |___  ___ _ _______ _ __ 
 |  __| | '_ \| |  | |/ _` |   | | | '_ ` _ \ / _` |/ _` |/ _ \ |  _  // _ \/ __| |_  / _ \ '__|
 | |____| | | | |__| | (_| |  _| |_| | | | | | (_| | (_| |  __/ | | \ \  __/\__ \ |/ /  __/ |   
 |______|_| |_|_____/ \__,_| |_____|_| |_| |_|\__,_|\__, |\___| |_|  \_\___||___/_/___\___|_|   
                                                     __/ |                                      
                                                    |___/                                                                                                     
        """,1))
    elif int(option) == 4:
        print(Colorate.Horizontal(Colors.white_to_red,"""
▒█▀▀▀ █▀▀▄ ▒█▀▀▄ █▀▀█ 　 ▀█▀ █▀▄▀█ █▀▀█ █▀▀▀ █▀▀ 　 ▒█▀▀█ █▀▀ █▀▀ ░▀░ ▀▀█ █▀▀ █▀▀█ 
▒█▀▀▀ █░░█ ▒█░▒█ █▄▄█ 　 ▒█░ █░▀░█ █▄▄█ █░▀█ █▀▀ 　 ▒█▄▄▀ █▀▀ ▀▀█ ▀█▀ ▄▀░ █▀▀ █▄▄▀ 
▒█▄▄▄ ▀░░▀ ▒█▄▄▀ ▀░░▀ 　 ▄█▄ ▀░░░▀ ▀░░▀ ▀▀▀▀ ▀▀▀ 　 ▒█░▒█ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀░▀▀                                                                
        """,1))

#Define an error function
def error(string):
    print(Fore.RED + "[ERROR]" + Fore.WHITE + " >> " + Fore.LIGHTRED_EX + str(string))

#Define an options list function
def options():
    print(Fore.MAGENTA + "[1]" + Fore.WHITE + " >> " + Fore.LIGHTYELLOW_EX + "Traditional Method")
    print(Fore.MAGENTA + "[2]" + Fore.WHITE + " >> " + Fore.LIGHTYELLOW_EX + "New Method (BETA)")
    print(Fore.MAGENTA + "[3]" + Fore.WHITE + " >> " + Fore.LIGHTYELLOW_EX + "Image Informations")
    print(Fore.MAGENTA + "[0]" + Fore.WHITE + " >> " + Fore.LIGHTRED_EX + "Exit the program")