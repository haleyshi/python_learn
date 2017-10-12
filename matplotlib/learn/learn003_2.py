from pylab import *

subplot(1, 2, 1)
xticks([]), yticks([])
text(0.5, 0.5, 'subplot(1,2,1)', ha='center', va='center', size=20, alpha=.5)

subplot(1, 2, 2)
xticks([]), yticks([])
text(0.5, 0.5, 'subplot(1,2,2)', ha='center', va='center', size=20, alpha=.5)

savefig("./figures/learn003_2.png", dpi=72)

show()