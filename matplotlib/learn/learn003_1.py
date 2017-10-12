from pylab import *

subplot(2, 1, 1)
xticks([]), yticks([])
text(0.5, 0.5, 'subplot(2,1,1)', ha='center', va='center', size=24, alpha=.5)

subplot(2, 1, 2)
xticks([]), yticks([])
text(0.5, 0.5, 'subplot(2,1,2)', ha='center', va='center', size=24, alpha=.5)

savefig("./figures/learn003_1.png", dpi=72)

show()