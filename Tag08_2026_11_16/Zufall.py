from random import random

# eingabe = input("Bitte zahl eingeben")


#print(f"eingabe {eingabe}")

print((random() * 6) + 1)
print(int((random() * 6) + 1))   # zufall zwischen 1 .. 6

anzahlEins = 0

for i in range(1,5000):
    zufallsZahl = int((random() * 6) + 1)
    if zufallsZahl == 1:
        anzahlEins += 1

print(anzahlEins)
print(1/6)
print(anzahlEins/5000)