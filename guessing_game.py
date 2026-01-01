import random

from click import prompt

random_number = random.randint(0 , 1000)
attemt=1
while True:
    prompt=("guss the number:{}\n".format(attemt))
    guss=int(input(prompt))
    if random_number == guss :
        print("your guss is correct")
        break
    elif random_number > guss:
        print("your guss is smaller")
    else :
        print("your guss is larger")
    attemt+=1