import math
import matplotlib.pyplot as plt

switch = False  # Treu = kör euler_stuck, False = kör euler_graph


# räknar antalet tidssteg innanför intervallet
# returnerar antalet tidssteg samt tiden vi spenderar innanför intervallet
def euler_stuck(t, y, h):
    count = 0
    while y < 1:
        if -1e-4 <= y <= 1e-4:
            h = h**2
            t += h
            count += 1
        y += h*math.sqrt(abs(y))
    return count, t


# returnerar array med värden för t och y för att kunna plotta
def euler_graph(t, y, h):
    t_vec = []
    y_vec = []
    while y <= 1:
        y_vec.append(y)
        t_vec.append(t)
        y += h*math.sqrt(abs(y))
        t += h
    return t_vec, y_vec


y0 = -1
t0 = -1

if switch:
    euler_stuck(y0, t0, 0.0000001)  # kommentera ut ifall man vill köra euler_graph
else:
    a, b = euler_graph(t0, y0, 0.00001)
    c, d = euler_graph(t0, y0, 0.1)

    plt.plot(a, b, label='h = 0.00001')
    plt.plot(c, d, label='h = 0.1')
    plt.xlabel('t')
    plt.ylabel('y(t)')
    plt.title('Nummerisk lösning för y(t) i intervallet [-1, 1]')
    plt.axhline(color='red', linestyle=':', label='y = 0')
    plt.legend(loc='upper left')
    plt.show()




