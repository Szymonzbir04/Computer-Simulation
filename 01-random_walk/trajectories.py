import numpy as np
import matplotlib.pyplot as plt

n_particles = 5
n_steps = 10000

increments = np.random.randn(n_particles, n_steps)
positions = np.zeros((n_particles, n_steps+1))
positions[:,1:] = np.cumsum(increments,axis=1)
times = np.arange(n_steps + 1)

for i in range(n_particles):
    plt.plot(times, positions[i], label = f"i = {i}")

plt.title("One-dimensional Gaussian random walk")
plt.xlabel(r'$t$', fontsize = 12)
plt.ylabel(r"$x_i$", fontsize = 12)
plt.legend()
plt.show()