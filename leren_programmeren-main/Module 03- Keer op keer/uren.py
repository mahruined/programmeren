for x in range(1, 24):
    if x < 12:
        print(f"{x}Am" )
    elif x > 12:
        pm = x - 12
        print(f"{pm}Pm")
    else:
        print(f'{x}AM')