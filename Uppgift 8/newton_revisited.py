import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import G

# E = Jorden (Earth)
# S = Solen
# J = Jupiter
# Ship = Skepp

# varv = antal var jorden gör runt solen. det fungerar att ange tal mellan noll och ett också
varv = float(input('Ange antal varv: '))
h = 0.01
n = int(998 * (varv/h))

# massor i kg
M = 2e30
m = 6e24
MJ = 1.9e27

# astronomical enhet i km
Au = 149597870

# begynnelsepositioner för varje kropp - [x-position, y-positiono]
rE = np.array([Au, 0])
rJ = np.array([-671781772.1396432, 329300609.97475713])
rS = np.array([0, 0])
rShip = np.array([Au + 10000, 0])

# begynnellehastighet för varje kropp - [hastighet x-led, hastighet y-led]
vE = np.array([0, np.sqrt((G*M)/np.linalg.norm(rE-rS))])
vJ = np.array([-184939.5543436754, -379672.3817097624])
vS = np.array([0, 0])
vShip = np.array([0, np.sqrt((G*m)/np.linalg.norm(rJ-rS)) + 11200000])
print(vShip)

x_posE = np.zeros(n)
y_posE = np.zeros(n)

x_posJ = np.zeros(n)
y_posJ = np.zeros(n)

x_posS = np.zeros(n)
y_posS = np.zeros(n)

x_posShip = np.zeros(n)
y_posShip = np.zeros(n)
vel_Ship = np.zeros(n)

for i in range(n):
    x_posE[i] = rE[0]
    y_posE[i] = rE[1]

    x_posJ[i] = rJ[0]
    y_posJ[i] = rJ[1]

    x_posS[i] = rS[0]
    y_posS[i] = rS[1]

    x_posShip[i] = rShip[0]
    y_posShip[i] = rShip[1]
    vel_Ship[i] = np.linalg.norm(vShip)

    # acceleration jorden
    aE = -(rE-rS)*G*M/np.linalg.norm(rE-rS)**3 - (rE-rJ)*G*MJ/np.linalg.norm(rE-rJ)**3
    vE = vE + h * aE
    rE = rE + h * vE

    # acceleration jupiter
    aJ = -(rJ-rS)*G*M/np.linalg.norm(rJ-rS)**3 - (rJ-rE)*G*m/np.linalg.norm(rJ-rE)**3
    vJ = vJ + h * aJ
    rJ = rJ + h * vJ

    # acceleration solen
    aS = -(rS-rE)*G*m/np.linalg.norm(rS-rE)**3 - (rS-rJ)*G*MJ/np.linalg.norm(rS-rJ)**3
    vS = vS + h * aS
    rS = rS + h * vS

    # acceleration skepp
    aShip = -(rShip-rE)*G*m/np.linalg.norm(rShip-rE)**3 - (rShip-rJ)*G*MJ/np.linalg.norm(rShip-rJ)**3 - (rShip-rS)*G*M/np.linalg.norm(rShip-rS)**3
    vShip = vShip + h + aShip
    rShip = rShip + h * vShip


# används för att rita cirkeln som motsvarar solsystemet
def circle(radie):
    x = []
    y = []
    t = np.linspace(0, 2*np.pi, 360)
    for a in t:
        x.append(radie * np.cos(a))
        y.append(radie * np.sin(a))
    return x, y


plt.figure(1)
plt.title('Slingshot närbild')
plt.xlabel('meter')
plt.ylabel('meter')
plt.axis('equal')
ax = 7*Au
plt.axis([-ax, ax, -ax, ax])
plt.plot(x_posE, y_posE, label='Bana Jorden')
plt.plot(x_posJ, y_posJ, label='Bana Jupiter')
plt.plot(x_posS, y_posS, label='Bana Solen')
plt.plot(x_posShip, y_posShip, label='Bana Skepp')
plt.scatter(x_posE[-1], y_posE[-1], label='Jorden', color='blue')
plt.scatter(x_posJ[-1], y_posJ[-1], label='Jupiter', color='orange')
plt.scatter(x_posS[-1], y_posS[-1], label='Solen', color='yellow')
plt.scatter(x_posShip[-1], y_posShip[-1], label='Skepp', color='black')
plt.legend(loc='upper right')

plt.figure(2)
plt.title('Slingshot solsystem')
plt.xlabel('meter')
plt.ylabel('meter')
plt.axis('equal')
ax = 45*Au
plt.axis([-ax, ax, -ax, ax])
plt.plot(x_posE, y_posE, label='Bana Jorden')
plt.plot(x_posJ, y_posJ, label='Bana Jupiter')
plt.plot(x_posS, y_posS, label='Bana Solen')
plt.plot(x_posShip, y_posShip, label='Bana Skepp')
plt.plot(*circle(40*Au), color='black', linestyle='--', label='Radie Solsystem')
plt.scatter(x_posE[-1], y_posE[-1], label='Jorden', color='blue')
plt.scatter(x_posJ[-1], y_posJ[-1], label='Jupiter', color='orange')
plt.scatter(x_posS[-1], y_posS[-1], label='Solen', color='yellow')
plt.scatter(x_posShip[-1], y_posShip[-1], label='Skepp', color='black')
plt.legend(loc='upper right')

plt.figure(3)
plt.title('Hastighet Skepp')
plt.ylabel('Hastighet')
plt.xlabel('tid')
plt.plot(vel_Ship)

plt.show()

