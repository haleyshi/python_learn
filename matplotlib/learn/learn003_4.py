from pylab import *
import matplotlib.gridspec as gridspec

G = gridspec.GridSpec(3, 3)

axes_1 = subplot(G[0, :])
xticks([]), yticks([])
text(0.5,0.5, 'Axes 1 - G[0, :]',ha='center',va='center',size=10,alpha=.5)

axes_2 = subplot(G[1,:-1])
xticks([]), yticks([])
text(0.5,0.5, 'Axes 2 - G[1,:-1]',ha='center',va='center',size=10,alpha=.5)

axes_3 = subplot(G[1:, -1])
xticks([]), yticks([])
text(0.5,0.5, 'Axes 3 - G[1:, -1]',ha='center',va='center',size=10,alpha=.5)

axes_4 = subplot(G[-1,0])
xticks([]), yticks([])
text(0.5,0.5, 'Axes 4 - G[-1,0]',ha='center',va='center',size=10,alpha=.5)

axes_5 = subplot(G[-1,-2])
xticks([]), yticks([])
text(0.5,0.5, 'Axes 5 - G[-1,-2]',ha='center',va='center',size=10,alpha=.5)

savefig("./figures/learn003_4.png", dpi=64)

show()