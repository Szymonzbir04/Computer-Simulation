import numpy as np
import matplotlib.pyplot as plt

number_of_particle = 1000
t = 100
x = np.random.randn(number_of_particle, t)
x[:,0] = 0
x_sum = np.cumsum(x,axis=1)

times = np.arange(t)

msd = np.mean(x_sum**2, axis = 0)

plt.plot(times,msd, label = 'Simulated MSD(t)')
plt.plot(times,times, label = f'MSD(t) = t')
plt.xlabel(r'$t$')
plt.ylabel('MSD(t)')
plt.legend()
plt.show()