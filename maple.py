
import numpy as np
import pylab as pl
import os

data = np.genfromtxt('test.csv')
print(np.shape(data))

pl.rc('font',size=16)
pl.figure(figsize=(10,10))
pl.plot(data[:,1],data[:,2],'b', linewidth=1.0, label='$.$')
pl.title('Van der Pol with $\mu = 0.5$, $x_0(0) = 1$, $x_1(0) = 1$')
pl.legend(loc=4,fancybox=True, shadow=True)
pl.show()