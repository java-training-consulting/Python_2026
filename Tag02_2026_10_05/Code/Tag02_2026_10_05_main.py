# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')

    # Sequenz 1. Grundbaustein von Algorythem und Programmen
    print(1)
    print(2)
    print(3)
    print(4)
    print(5)

    intvar = 1
    print(intvar)
    intvar = intvar + 1
    print(intvar)
    intvar = intvar + 1
    print(intvar)
    intvar = intvar + 1
    print(intvar)
    intvar = intvar + 1
    print(intvar)
    intvar = intvar + 1

i = 1
#while i <= 10_000_000:
#    print(i)
#    i = i + 1

# EVA Eingabe Verarbeitung Ausgabe

# Eingabe
# ganze Zahl n , n=3 , 1 +2 +3 -> 6
print("summme von n zahlen")
# V erarbeitung ???
summe = 0

summe = 1 + 2 + 3

summe = 0
summe = summe + 1
summe = summe + 2
summe = summe + 3


i = 1
summe = 0
summe = summe + i
i = i + 1
summe = summe + i
i = i + 1
summe = summe + i
i = i + 1

n = 100
i = 1
summe = 0
while  i <= n:
    summe = summe + i
    i = i + 1


# https://www.wolframalpha.com/input?i=1%2B2%2B3%2B...%2Bn
# O(1)   Laufzeit
summe = n * (n + 1) // 2

# Ausgabe
print(summe)

print("ende vom Programm")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# https://www.cise.ufl.edu/~manuel/obfuscate/nqueens.c