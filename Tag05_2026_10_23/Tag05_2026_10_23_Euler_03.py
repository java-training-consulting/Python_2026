from math import sqrt
from datetime import datetime

#<p>The prime factors of $13195$ are $5, 7, 13$ and $29$.</p>
#<p>What is the largest prime factor of the number $600851475143$?</p>


# def isPrime(param):
#    pass

zahl = 600851475143
zahl = 13195
'''
print(13195%2)  # 0 -> zahl wird von 2 geteilt
print(13195%3)  # 0 -> zahl wird von 3 geteilt
print(13195%4)  # 0 -> zahl wird von 4 geteilt
print(13195%5)  # 0 -> zahl wird von 5 geteilt
print(13195%6)  # 0 -> zahl wird von 6 geteilt


print(13195%13195)  # 0 -> zahl wird von 13195 geteilt


print(13195%13194)  # 0 -> zahl wird von 13194 geteilt
print(13195%13193)  # 0 -> zahl wird von 13193 geteilt

teiler = 13194
print(13195%teiler)  # 0 -> zahl wird von ? geteilt
teiler = teiler - 1
print(13195%teiler)  # 0 -> zahl wird von ? geteilt
teiler = teiler - 1
print(13195%teiler)  # 0 -> zahl wird von ?  geteilt
teiler = teiler - 1
'''

zahl = 600851475143


print(datetime.now())
# schleife
teiler = zahl -1
while teiler > 1:
    # print13195(13195%teiler)  # 0 -> zahl wird von ?  geteilt
    if teiler % 100000000 == 0:
        print(f"running teiler:{teiler} time: {datetime.now()}")
    if zahl % teiler == 0:
        # ist teiler eine Primzahl
        isPrim = True
        # programmteil ist zu langsam
        div = 2  # 2 extra
        if teiler % div == 0:
            isPrim = False
        # while div < teiler:  # optimierung < wurzel(teiler reicht)
        div = 3
        while div <= sqrt(teiler):
            if teiler % div == 0:
                # keine Primzahl
                isPrim = False
                break
            div = div + 2 # nur ungerade zahlen
        if  isPrim:
            print(f"teiler: {teiler}")
    teiler = teiler - 1
print(datetime.now())
#isPrime(7)