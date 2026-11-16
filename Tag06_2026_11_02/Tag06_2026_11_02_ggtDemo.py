# https://de.wikipedia.org/wiki/Gr%C3%B6%C3%9Fter_gemeinsamer_Teiler

# https://www.mrge.de/lehrer/sigismund/python/grundlagen/gcd.html

def ggt(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

a=24
b=16
print("ggT(", a, ",", b, " = ", end="")
while a!=b:
    if a>b:
        a=a-b
    else:
        b=b-a
print(a)

print(f" ggt(24,16) = {ggt(24,16)}")
print(f" ggt(101,16) = {ggt(101,16)}")
print(f" ggt(13,234) = {ggt(13,234)}")