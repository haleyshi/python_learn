import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10, 0.005)
y = np.exp(-x/2.) * np.sin(2*np.pi*x)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y)
ax.set_xlim(0, 10)
ax.set_ylim(-1, 1)

disp = ax.transData.transform([(5, 0), (1,2)])
inv = ax.transData.inverted()
data = inv.transform(disp)
print disp, data

plt.savefig("./figures/learn004_12.png", dpi=64)
plt.show()