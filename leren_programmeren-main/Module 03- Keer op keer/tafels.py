nummer = int(input("Welke tafel wilt u weten?"))

for x in range(1, 11):
    tafel = x * nummer
    print(f"{x}x{nummer}={tafel}")