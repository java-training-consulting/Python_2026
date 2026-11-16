# 5 , 101, 13
'''
5%2 == 0 -> keine Primzahl
5%3 == 0 -> keine Primzahl
5%4 == 0 -> keine Primzahl
'''

zahl = 1234545222222
isPrim = True
div = 2
while div < zahl:
    if zahl%div == 0:
        # keine Primzahl
        isPrim = False
        break
    div = div + 1

print(isPrim)
