# https://codingcontest.org/challenges

# ziffern einer zahl siehe euler 20
# Übung
#! bedeutet n × (n − 1) × ... × 3 × 2 × 1

#Zum Beispiel ist 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
#und die Summe der Ziffern der Zahl 10! ist 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

#Finden Sie die Summe der Ziffern der Zahl 100!

zahl = 7124
# 7 + 1 + 2 + 4

print(zahl%10)
zahl = zahl // 10

print(zahl%10)
zahl = zahl // 10

print(zahl%10)
zahl = zahl // 10

print(zahl%10)
zahl = zahl // 10