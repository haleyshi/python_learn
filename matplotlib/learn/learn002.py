import numpy as np
import matplotlib.pyplot as plt

# Create a 8*5 figure, with DPI=80
plt.figure(figsize=(8, 5), dpi=80)

# Create a 1*1 subplot, and draw figure on the 1st block
ax = plt.subplot(111)

# Set the Spines
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

# Get 256 linear values from -pi to pi and the related cos/sin values
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)

# Draw figures
plt.plot(X, C, color="red", linewidth=2.5, linestyle="-", label="cosine")
plt.plot(X, S, color="green",  linewidth=2.5, linestyle="-", label="sine")

# Draw label as the sample, location: upper left, not draw the edge
plt.legend(loc='upper left', frameon=False)

# Set X limitations
#xlim(-4.0, 4.0)
#xlim(X.min() * 1.1, X.max() * 1.1)

# Set X ticks
#xticks(np.linspace(-4, 4, 9, endpoint=True))
#xticks( [-np.pi, -np.pi/2, 0, np.pi/2, np.pi])

# Set Y limitations
#ylim(-1.0, 1.0)
#ylim(C.min() * 1.1, C.max() * 1.1)

# Set Y ticks
#yticks(np.linspace(-1, 1, 5, endpoint=True))
#yticks([-1, 0, +1])

# A better way to set XY limitation and ticks
xmin ,xmax = X.min(), X.max()
ymin, ymax = C.min(), C.max()

dx = (xmax - xmin) * 0.1
dy = (ymax - ymin) * 0.1

plt.xlim(xmin - dx, xmax + dx)
plt.ylim(ymin - dy, ymax + dy)

plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
       [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

plt.yticks([-1, +1],
       [r'$-1$', r'$+1$'])

# Annotate for some special points
t = 2*np.pi/3
plt.plot([t,t],[0,np.cos(t)],
         color ='red',  linewidth=1.5, linestyle="--")
plt.scatter([t,],[np.cos(t),], 50, color ='red')
plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t, np.sin(t)),  xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.plot([t,t],[0,np.sin(t)],
         color ='green',  linewidth=1.5, linestyle="--")
plt.scatter([t,],[np.sin(t),], 50, color ='green')
plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, np.cos(t)),  xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

# Handle the overlap of Spine and ticks
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='lightblue', edgecolor='None', alpha=0.45))

# save picture with dpi=72
plt.savefig("./figures/learn002.png", dpi=72)

# Display on screen
plt.show()