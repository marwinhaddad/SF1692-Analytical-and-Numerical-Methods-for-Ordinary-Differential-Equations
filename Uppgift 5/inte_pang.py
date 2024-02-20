import math


# skriver ut analytisk lösning
def facit():
    print('FACIT: ')
    for k in range(1, 10):
        y = 51*math.exp(2**k)
        print(k, y)


# beräknar och skriver ut numerisk lösning
def inte_pang():
    N = 51
    t0 = 0
    n = 1000000
    f = lambda y: y
    print('\nk y(2^k)')
    for k in range(1, 10):
        T = 2**k
        h = (T-t0)/n
        y = N
        for i in range(n):
            y = y + h * f(y)
        print(k, y)
        n *= 100


facit()
inte_pang()

