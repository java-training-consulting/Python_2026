
def funktion_rek(n):
    # Abbruch
    if n == 0:
        print("*")
        return 0
    print("*")
    return funktion_rek(n-1)

#  fib(0) = 1
#  fib(1) = 1
#  fib(n) = fib(n-1) + fib(n-2)
#
#
def fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    # funktion_rek(10)
    # fibonaci zahl
    print(fib(0))
    print(fib(1))
    print(fib(2))
    print(fib(3))
    print(fib(4))
