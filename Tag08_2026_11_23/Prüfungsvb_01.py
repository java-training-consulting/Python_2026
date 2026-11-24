#math
# https://docs.python.org/3/library/math.html
#time
# https://docs.python.org/3/library/time.html

import math
# nicht 0/0 -> vorher prüfen
print(math.nan == math.nan)

print(float('nan') == float('nan'))

print(math.isnan(math.nan))

print(math.isnan(float('nan')))

print(math.sin(360))  # 360 grad -> 2*PI in Randiant
print(math.sin(2 * math.pi))


grad = math.degrees(math.pi)  # 180.0
print(grad)

print(math.radians(180))

print(math.sqrt(64*64))

# time

import time

startzeit = time.time()
print(time.time())
# brechnung
erg = 0
for i in range(1,100000000):
    erg =erg + i

print(time.time() - startzeit)