import os
import time
import subprocess
from colorama import Fore

print(f"{Fore.RED} ▄▄▄██▀▀▀▄▄▄       ██▓ ██▓     ▄▄▄▄    ██▀███  ▓█████ ▄▄▄       ██ ▄█▀")
time.sleep(0.2)
print(f"{Fore.RED}   ▒██  ▒████▄    ▓██▒▓██▒    ▓█████▄ ▓██ ▒ ██▒▓█   ▀▒████▄     ██▄█▒") 
time.sleep(0.2)
print(f"{Fore.RED}   ░██  ▒██  ▀█▄  ▒██▒▒██░    ▒██▒ ▄██▓██ ░▄█ ▒▒███  ▒██  ▀█▄  ▓███▄░")
time.sleep(0.2) 
print(f"{Fore.RED}▓██▄██▓ ░██▄▄▄▄██ ░██░▒██░    ▒██░█▀  ▒██▀▀█▄  ▒▓█  ▄░██▄▄▄▄██ ▓██ █▄")
time.sleep(0.2) 
print(f"{Fore.RED} ▓███▒   ▓█   ▓██▒░██░░██████▒░▓█  ▀█▓░██▓ ▒██▒░▒████▒▓█   ▓██▒▒██▒ █▄")
time.sleep(0.2)
print(f"{Fore.RED} ▒▓▒▒░   ▒▒   ▓▒█░░▓  ░ ▒░▓  ░░▒▓███▀▒░ ▒▓ ░▒▓░░░ ▒░ ░▒▒   ▓▒█░▒ ▒▒ ▓▒")
time.sleep(0.2)
print(f"{Fore.RED} ▒ ░▒░    ▒   ▒▒ ░ ▒ ░░ ░ ▒  ░▒░▒   ░   ░▒ ░ ▒░ ░ ░  ░ ▒   ▒▒ ░░ ░▒ ▒░")
time.sleep(0.2)
print(f"{Fore.RED} ░ ░ ░    ░   ▒    ▒ ░  ░ ░    ░    ░   ░░   ░    ░    ░   ▒   ░ ░░ ░")
time.sleep(0.2)
print(f"{Fore.RED} ░   ░        ░  ░ ░      ░  ░ ░         ░        ░  ░     ░  ░░  ░")
time.sleep(0.2)   
print(f"{Fore.RED}                                    ░{Fore.WHITE}")

time.sleep(1)
ip = input("IP Address ----> ")
response = os.system("ping -c 100000 " + ip)
