
# 1 + 2 + 3 + ... + 100
# O(n)   Laufzeit
n = 100
i = 1
summe = 0
while  i <= n:
    summe = summe + i
    i = i + 1


# https://www.wolframalpha.com/input?i=1%2B2%2B3%2B...%2Bn
# O(1)   Laufzeit

# https://oeis.org/
summe = n * (n + 1) // 2

# Ausgabe
print(summe)
# faktuelle
# 1              -> 1       1!
# 1 * 2          -> 2       2!
# 1 * 2 * 3      -> 6       3!
# 1 * 2 * 3 * 4  -> 24      4!

fakt = 0
fakt = 1 * 2 * 3
print(fakt)

fakt = 0
fakt = 1 * 2 * 3 * 4

fakt = 1 * 2 * 3
fakt = 1 * 2 * 3 * 4

fakt = 1 * 2 * 3

fakt = fakt * 4
fakt = fakt * 5

i = 4
fakt = fakt * i
i = i + 1
fakt = fakt * i
i = i + 1

i = 1
n = 100
fakt = 1
while i <= n:
    fakt = fakt * i
    i = i + 1

print(fakt)
print(type(fakt))

print("ende vom Programm")
