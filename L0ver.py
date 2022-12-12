import time
from subprocess import call
from os import system
import os

os.system(delet)
print("DO YOU LOVE YOUR PC??????")
print("Yes/No")
choice = input("")

if choice == "yes":
    print("OK")
    call(["python", "Lovr.py"])
    time.sleep(1)
    
if choice == "no":
  call(["python", "Random.py"])
  time.sleep(1)
