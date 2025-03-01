import matplotlib.pyplot as plt
import numpy as np

apoints = np.array([0,6])
bpoints = np.array([0,250])

plt.plot(apoints,bpoints,'o')
plt.plot(apoints,'*:r')

plt.show()

