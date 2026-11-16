from decimal import Decimal


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    print("Hallo" + str(1))

    print(type(str(1)))

    print(type(7 // 2 ))
    print(type(7 / 2))
    print(type(7.2))

    print(Decimal(7.2))
    print(Decimal("7.2"))

    geld = Decimal("7.2")


