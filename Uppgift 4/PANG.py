import matplotlib.pyplot as plt
import numpy as np


# False == av, True == på
analytisk = False
numerisk = True
analytisk_y0_neg = True
automat = False


# y' = y^2 = f(x, y)
def f(x, y):
    return y**2


# returner "analytisk" svar så att man kan plotta
def eulerAna(f, y0, t):
    y = np.zeros(len(t))
    y[0] = y0
    for i in range(len(t)-1):
        y[i+1] = y[i] + f(t[i], y[i])*(t[i+1] - t[i])
    return y


# returnerar numeriskt svar
def eulerNum(f, y, t, n):
    h = 1/n
    tvec = []
    yvec = []
    while True:
        yvec.append(y)
        tvec.append(t)
        yn = y + h * f(t, y)

        # pangar när skillnaden mellan y_n och y_n+1 är större än 10
        if abs(yn - y) > 10:
            return tvec, yvec
        y = yn
        t += h


# testar automatlösaren
def automatlösare():
    y = -1
    t = 0
    h = 0.0001
    f = lambda x: 10000*x**2
    while y <= 0:
        print(y)
        y += h * f(y)
        t += h
        if y > 0:
            y = 0
    print(f'y = {y} hoppade över y = 0 vid t = {t}')


# konstanter
N = 51
t0 = 0
t1 = 100/N
y0 = N/100
n = 100000

if analytisk:
    t_ana = np.linspace(t0, t1, n)
    y_ana = eulerAna(f, y0, t_ana)

    plt.figure(1)
    plt.title('Analystisk lösning för när det PANGAR')
    plt.plot(t_ana, y_ana, label='y = 1/(100/N - t)')
    plt.xlabel('Tid')
    plt.ylabel('Pang(Tid)')
    plt.axvline(100/N, color='red', linestyle=':', label='t = 100/N')
    plt.legend(loc='upper left')

if numerisk:
    t_num, y_num = eulerNum(f, y0, t0, n)

    plt.figure(2)
    plt.title('Numerisk lösning för när det PANGAR')
    plt.plot(t_num, y_num, label='y = 1/(100/N - t)')
    plt.xlabel('Tid')
    plt.ylabel('Pang(Tid)')
    plt.axvline(100/N, color='red', linestyle=':', label='t = 100/N')
    plt.legend(loc='upper left')

if analytisk_y0_neg:
    t0 = 100/N * 100
    t_neg = np.linspace(t0, t1, n)
    y_neg = eulerAna(f, -y0, t_neg)

    plt.figure(3)
    plt.plot(t_neg, y_neg, label='y = -1/(100/N + t)')
    plt.xlabel('Tid')
    plt.ylabel('Pang(Tid)')
    plt.axhline(0, color='red', linestyle=':', label='y = 0')
    plt.legend(loc='upper left')

if automat:
    automatlösare()

plt.show()
