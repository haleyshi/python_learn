from pylab import *

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)

plot(X, C)
plot(X, S)

savefig("./figures/learn001.png",dpi=64)

show()