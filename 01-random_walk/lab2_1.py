import numpy as np
import matplotlib.pyplot as plt

number_of_particle = 5
t = 10000
x = np.random.randn(number_of_particle, t)
x[:,0] = 0
x_sum = np.cumsum(x,axis=1)

times = np.arange(t)

for i in range(number_of_particle):
    plt.plot(times,x_sum[i], label = f"i = {i}")

plt.title("Random walk for several particles")
plt.xlabel(r'$t$')
plt.ylabel(r"$x_i$")
plt.legend()
plt.show()