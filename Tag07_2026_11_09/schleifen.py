
def demo_while():
    # wiederholung

    # n-mal
    n = 1000
    i = 1
    while i <= n:
        # block
        print(f"{i}*")
        i += 1


# Press the green button in the gutter to run the script.
def demo_for():

    for i in range(10):
        print(f"{i}*")

    namensliste = ['franz','frank', 'fra']
    for i in namensliste:
        print(f"{i}*")


if __name__ == '__main__':
    # demo_while()
    demo_for()

    print(range(10))
    print(list(range(10)))
