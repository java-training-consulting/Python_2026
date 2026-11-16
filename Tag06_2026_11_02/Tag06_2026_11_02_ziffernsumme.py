#  123 -> 1 + 2 + 3 -> 6

# V .... Verarbeitung
def xziffersum(zahl):
    summe = 0
    # 15   1  5   ? %
    print(f"{zahl}%10  {zahl%10}")
    summe = summe + zahl%10
    zahl = zahl // 10
    summe = summe + zahl%10
    zahl = zahl // 10
    summe = summe + zahl%10
    zahl = zahl // 10
    return summe

def ziffersum(zahl):
    summe = 0

    while ( zahl > 0):
        summe = summe + zahl%10
        zahl = zahl // 10

    return summe

print(f"ziffersum(5) {ziffersum(5)}")
print(f"ziffersum(15) {ziffersum(15)}")
print(f"ziffersum(111) {ziffersum(111)}")
print(f"ziffersum(222) {ziffersum(222)}")
