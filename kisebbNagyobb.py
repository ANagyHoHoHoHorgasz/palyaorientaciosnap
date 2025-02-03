import random
number = random.randint(1, 10)


for i in range(4):
    bekero = int(input("Gondolj egy számra 1 és 10 között!"))
    if number > bekero:
        print("A gondolt szám nagyobb!")
    elif number < bekero:
        print("A gondolt szám kisebb!")
    else:
        print("Egyenlő a gondolt szám és a megadott szám! Gratulálok!")

if bekero != number:
    print(f"A gondolt szám: {number}, szar vagy!")