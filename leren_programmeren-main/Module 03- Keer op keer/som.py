teller = 0
x = 50
som = x + teller

while x <= 2000:
    if x >= 1100:
        break
    print(x)
    teller = teller + 1
    x = som + x + teller
print("einde")
