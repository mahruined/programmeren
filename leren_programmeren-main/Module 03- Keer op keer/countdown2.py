
from multiprocessing import Event

num = 30

while num >=1:
    Event().wait(1)
    print(f"{num}seconden")
    num = num - 1
    

print("Launching!")