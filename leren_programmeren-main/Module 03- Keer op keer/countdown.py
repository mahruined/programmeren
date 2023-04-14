from multiprocessing import Event
import time

while True:
    try:
       countdown = int(input("Hoelang moet de countdown zijn?"))
       break
    except:
        print("Voer een geldig aantal seconden in!")
for i in range(countdown,-1,-1):
    print(i)
    Event().wait(1)
print("Launching!")