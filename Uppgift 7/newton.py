import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import G

switch = True  # True = euler framåt, False = semi-implicit euler
hastighet = False  # visar hur hastighet i x- och y-led förhåller sig till varandra

# n = antal iterationer, h = steglängd, varv = antal varv jorden gör runt solen
varv = 1
h = 0.01
n = int(998*varv/h)

# mass in kg
M = 1.9891e30
m = 5.9726e24

# begynnelsevärden
# r = [x-position, y-position]
r = np.array([1496e5, 0])

# v = [hastighet i x-led, hastighet i y-led]
v = np.array([0, np.sqrt((G*M)/np.linalg.norm(r))])

# diskret funktion som returnerar acceleration
F = lambda x: -(x*G*M)/(np.linalg.norm(x)**3)


# lösning med explicit euler
def frameuler(n, r, v):
    pos = np.zeros([n, 2])
    vel = np.zeros([n, 2])
    for i in range(n):
        pos[i] = r
        vel[i] = v

        r = r + h * v
        v = v + h * F(r)
    return pos, vel


# lösning med semi-implicit euler
def semieuler(n, r, v):
    pos = np.zeros([n, 2])
    vel = np.zeros([n, 2])
    v = v + h * F(r)
    for i in range(n):
        pos[i] = r
        vel[i] = v

        v = v + h * F(r)
        r = r + h * v
    return pos, vel


# switch = True/ False
if switch:
    pos, vel = frameuler(n, r, v)
    plt.title('Frammåt Euler')

else:
    pos, vel = semieuler(n, r, v)
    plt.title('Semi-implicit Euler')


# plottar banan
plt.figure(1)
plt.plot(pos[:, 0], pos[:, 1])
plt.axis('equal')
plt.scatter(0, 0, color='yellow')
plt.scatter(pos[:, 0][0], pos[:, 1][0], color='red', label='start pos.')
plt.scatter(pos[:, 0][-1], pos[:, 1][-1], color='green', label='slut pos.')
plt.legend(loc='upper left')
plt.xlabel('km')
plt.ylabel('km')

# hastighet = True/ False
if hastighet:
    plt.figure(2)
    plt.plot(vel[:, 0], label='Vx')
    plt.plot(vel[:, 1], label='Vy')
    plt.xlabel('tid')
    plt.ylabel('km/t')
    plt.legend(loc='lower right')
    plt.title('Hastighet i x- y-led per tidsenhet')

plt.show()
