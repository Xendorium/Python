import random

random1 = 0

while random1 < 1000 or random1 > 9999:
    random1 = random.randint(0000, 9999)
print(random1)
i=1
shot = int(input("Podaj liczbe: "))
while shot != random1:
    if shot > random1:
        print("Podano za duza liczbe")
    else:
        print("Podano za mala liczbe")
    shot = int(input("Sprobuj ponownie: "))
    i+=i
print("Udało ci sie zgadnac za "+ str(i) + " razem")