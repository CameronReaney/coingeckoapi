import requests
import json
import os
import time
import schedule
from tkinter import *
#ask user what mode they want to use, print pirces every 60 seconds or send email every hour
#seperate modes into two functions , "secsPrint" and "hourlyEmail" and hourly notif
def secsPrint():
    coinChoice = input("Enter Crypto: ")
    fiatChoice = input("Enter Fiat Currency: ")
    while True:
        t = time.localtime()
        currentTime = time.strftime("%H:%M:%S", t)
        t = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=" + coinChoice + "&vs_currencies="+ fiatChoice).text
        t = json.loads(t)
        print("The Price of " + coinChoice + "is: ")
        price = print(t[coinChoice][fiatChoice] , fiatChoice, "Time: ", currentTime)
        print(price)
        time.sleep(60)


secsPrint()
