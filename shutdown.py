from datetime import datetime as t
import time
import os
now = t.now()
current = now.strftime("%H:%M:%S")
print(f"CURRENT TIME : {current}")
user = input("INPUT SHUTDOWN TIME 00:00 - 24:00 : ")
shutdown = current > user
print ("STARTING...")
while shutdown == False:
    now = t.now()
    current = now.strftime("%H:%M:%S")
    shutdown = current > user
    print(F"TIME NOW {current} SHUT DOWN AT {user}")
    time.sleep(300)
    if shutdown == True :
        break
print ("SHUTTING DOWN")
os.system("shutdown /s /t 1")