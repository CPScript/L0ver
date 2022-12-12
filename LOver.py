import time
from subprocess import call


print("DO YOU LOVE YOUR PC?")
print("Yes/No")
choice = input("")

if choice == "yes":
    print("OK")
    call(["python", "L0ver.py"])
    time.sleep(1)
    
if choice == "no":
  call(["python", "Random.py"])
  time.sleep(1)
