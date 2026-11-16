# https://projecteuler.net/
'''

If we list all the natural numbers below 10
that are multiples of 3
or 5
,   we get
and
. The sum of these multiples is 23
.

Find the sum of all the multiples of 3
or 5
below 1000
'''

# teilbar  -> kein Rest -> Rest ist 0 -> Zahl ist teilbar
print( 5/3 )  # int / int  -> float
print (type(5/3))

print( 5//3 )  # int // int  -> int
print (type(5//3))

# modulo
print( 5%3 )  # int % int  -> int
print (type(5%3))

zahl = 5
if zahl % 2 == 0:
    print("zahlt ist gerade")
else:
    # zahl % 2 != 0
    print("zahlt ist ungerade")

sum_euler_01 = 0
zahl = 1
if zahl % 3 == 0:
    sum_euler_01 = sum_euler_01 + zahl
zahl = zahl + 1

if zahl % 3 == 0:
    sum_euler_01 = sum_euler_01 + zahl
zahl = zahl + 1

if zahl % 3 == 0:
    sum_euler_01 = sum_euler_01 + zahl

sum_euler_01 = 0
zahl = 1
while zahl < 1000:
    if zahl % 3 == 0:
        sum_euler_01 = sum_euler_01 + zahl
    else:
        if zahl % 5 == 0:
            sum_euler_01 = sum_euler_01 + zahl
    zahl = zahl + 1

print(sum_euler_01)

sum_euler_01 = 0
zahl = 1
while zahl < 1000:
    if zahl % 3 == 0  or zahl % 5 == 0:
        sum_euler_01 = sum_euler_01 + zahl
    zahl = zahl + 1

print(sum_euler_01)
