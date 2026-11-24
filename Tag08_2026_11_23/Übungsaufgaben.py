from decimal import Decimal


def auf_001():
    meter =  123  # typ
    print(type(meter))
    geld = Decimal("0.1")  # 0.1 -> float 0.1000000000000000055511151231257827021181583404541015625
    print(geld)
    print(type(geld))


def auf_002():
    print(4%2)
    print(5%2)
    #
    print(4 - ( 4 // 2) * 2)
    print(5 - (5 // 2) * 2)
    # wie geht das ohne  // -> int()
    # ????


def auf_004():
    eingabe = input("eingabe:")
    print(eingabe)

if __name__ == '__main__':
    # auf_001()
    # auf_002()

    auf_004()
