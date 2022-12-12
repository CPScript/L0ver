import time
from subprocess import call


print(DO YOU LOVE YOUR PC?)
print("Yes/No")
choice = input("")

if choice == "yes":
    print("OK")
    
if choice == "no":
  call(["python", ".py"])
  time.sleep(1)
  
  
  

call(["python", "PS.py"])
time.sleep(1)
