import time
import winsound

frequency = 15000  # Set Frequency To 2500 Hertz
duration = 500  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)

# Variaben
summe = 12 * 3    # Ausdruck typ wert

rest = 12 % 3  # int 0

ganzeZahl = int(12.7 + 0.5)

print(ganzeZahl)
print(type(12.7))

print(12 / 3)
print(type(12 / 3))

print(12 // 3)
print(type(12 // 3))

print(0.1 + 0.2) # 101101.100010111 * 2^010

print("hallo")   # unicode
print(type("hallo"))

# 3 Bausteine
# Sequenz
print("***********")
print("*  hallo  *")
print("***********")

# Wiederholung
running = True

#while running:
#    print("*")


print(1)
print(2)
print(3)
# ...
i = 1

print(i)
i = i + 1

print(i)
i = i + 1
print(i)
i = i + 1

i = 0
while i < 1000 :
    # wird 10 mal wiederholt
    i += 1  # i = i + 1
    time.sleep(1)
    print(i)



