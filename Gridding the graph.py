from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

x=[5,6,7]
y=[10,9,8]

x2=[1,2,4]
y2=[2,6,9]

plt.plot(x,y,label="lineone",linewidth=5)
plt.plot(x2,y2,label="linetwo",linewidth=5)
plt.grid(True)
plt.legend()

plt.show()