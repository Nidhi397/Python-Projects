import random

#x=random.random()
#print(x)
#But for dice we need numbers from 1 to 6 specifically
print("This is a Dice Simulator:")

x="y"

while(x=="y"):
    num=random.randint(1,6)
    if num==1:
        print('----------')
        print('|        |')
        print('|    0   |')
        print('|        |')
        print('----------')

    if num==2:
        print('----------')
        print('|        |')
        print('| 0    0 |')
        print('|        |')
        print('----------')

    if num==3:
        print('----------')
        print('|    0   |')
        print('|    0   |')
        print('|    0   |')
        print('----------')


    if num==4:
        print('----------')
        print('| 0    0 |')
        print('|        |')
        print('| 0    0 |')
        print('----------')

    if num==5:
        print('----------')
        print('| 0    0 |')
        print('|    0   |')
        print('| 0    0 |')
        print('----------')

    if num==6:
        print('----------')
        print('| 0    0 |')
        print('| 0    0 |')
        print('| 0    0 |')
        print('----------')
    x=input("Press y to roll again:\n")
