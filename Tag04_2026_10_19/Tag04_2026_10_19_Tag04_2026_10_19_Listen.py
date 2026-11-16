# minimum  suchen , maximum suchen
liste = [10,10,-4,-10, 100,1000]

print(liste)

print(liste[0])
print(liste[1])
print(liste[2])
# fehler print(liste[3])
i = 0
print(liste[i])
i = i + 1
print(liste[i])
i = i + 1
print(liste[i])
i = i + 1

i = 0
summe = 0
while i <  len(liste) :
    print(liste[i])
    summe = summe + liste[i]
    i = i + 1

# print(len(liste))
print(summe)