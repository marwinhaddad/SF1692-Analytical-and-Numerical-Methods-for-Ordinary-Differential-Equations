import numpy as np
import matplotlib.pyplot as plt

plotta = False  # True = plottar graf, False = räknar pi med euler och rk4 steglängd
steglängd = 0.000000001


# explicit euler
def euler(h):
    t = 0
    u = np.array([1, 0])
    F = lambda z: np.array([z[1], -z[0]])
    while u[0] > 0:
        u = u + h * F(u)
        t = t + h
    print('Euler:     ', t*2)


# runge-kutta 4
def nographrk4(h):
    t = 0
    u = 1                   # u = y
    v = 0                   # v = y'
    F = lambda u, v, t: -u  # F(y,y',t) = y"
    while u > 0:
        l1 = h * v
        k1 = h * F(u, v, t)

        l2 = h * (v + k1/2)
        k2 = h * F(u + l1/2, v + k1/2, t + h/2)

        l3 = h * (v + k2/2)
        k3 = h * F(u + l2/2, v + k2/2, t + h/2)

        l4 = h * (v + k3)
        k4 = h * F(u + l3, v + k3, t + h)

        u += (l1 + 2*l2 + 2*l3 + l4)/6
        v += (k1 + 2*k2 + 2*k3 + k4)/6
        t = t + h
    print('RK4:       ', t*2)


def eulerplott():
    h = 0.001
    F = lambda z: np.array([z[1], -z[0]])
    t = 0
    t_vec = [t]
    u = np.array([1, 0])
    y_vec = [u[0]]
    while u[0] > 0:
        u = u + h * F(u)
        t = t + h
        y_vec.append(u[0])
        t_vec.append(t)
    return y_vec, t_vec


if plotta:
    t_vec, y_vec = eulerplott()
    plt.plot(y_vec, t_vec, label='y = cos(t)')
    plt.axhline(0, linestyle=':', color='red')
    plt.legend(loc='upper left')
    plt.show()
else:
    print('Exakt pi:', np.pi)
    euler(steglängd)
    nographrk4(steglängd)
