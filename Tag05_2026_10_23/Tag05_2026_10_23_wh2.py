
# https://projecteuler.net/problem=16
print(2**15)

zahl = 2**1000
print(zahl)


# zufallszahl
import random
print(random.random())  # [0..1[  1 nicht mehr dabei
# -> int [1..6]  würfel
# http://f.javier.io/rep/books/Donald-Knuth---The-Art-of-Computer-Programming-Vol-1-Fundamental-Algorithms.pdf

wuerfelZahl = int(random.random() * 6)
wuerfelZahl = wuerfelZahl + 1
print(wuerfelZahl)   # 0..5

# würfeln und zählen
anzahlWuerfe = 100000000
summe = 0
i = 1
while i <= anzahlWuerfe:
    wuerfelZahl = int(random.random() * 6)+1
    if wuerfelZahl == 1:
        summe = summe + wuerfelZahl
    i = i + 1

print (f"summe:{summe/anzahlWuerfe}" )
print (f"1/6:{1/6}" )