#inputs voor je min/max
A = int ( input ('wat is de waarde van A '))
B = int ( input ('wat is de waarde van B '))

#if statements
if A > B:
    max = A
    min = B 
    print('A is het grootse getal met de waarde van',max )
elif B > A:
    max = B
    min = A
    print('A is het kleinste getal  ')
else:
    print ('a en b zijn gelijk')
    max = A
    min = B 
#waarde van min/max 
print ('het maximum is', max)
print ('het minimum is', min)
