'''zahl = 600851475143
i = 1
while i <= zahl:
    print(i)
    i = i + 1

'''
import math
# funktionen
# https://www.python-lernen.de/funktionen-in-python.htm
def ausgabe():
    print("Ausgabe von Text aus einer Funktion")

# ausgabe()
# print("Programm abgelaufen")

# EVA  -> Eingabe Verarbeitung Ausgabe

# DRY -> Don't Repaet Yourselv -> funktion Programmieren

# Besser Testen komplexität reduzieren

def isPrim(zahl):
    i = 2
    while(i <= math.sqrt(zahl)):
        if zahl % i == 0:
            return False
        i = i + 1
    return True


print(isPrim(2))
print(isPrim(25))
print(isPrim(101))
print(f"isPrim(12) {isPrim(12)}")
print(f"isPrim(144) {isPrim(144)}")
print(f"isPrim(101) {isPrim(101)}")
print(f"isPrim(600851475143) {isPrim(600851475143)}")
