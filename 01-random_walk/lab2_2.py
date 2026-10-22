import numpy as np
import matplotlib.pyplot as plt

number_of_particle = 100000
times = [1, 10, 100]

fig, axes =plt.subplots(1,len(times), figsize=(15,4), sharex=True,sharey=True)

fig.suptitle("Probability distribution")

for i, t in enumerate(times):
    pom = np.random.randn(number_of_particle, t)
    x = np.sum(pom, axis=1)

    x_plot = np.linspace(np.min(x),np.max(x), 100)
    y = 1 / np.sqrt(2 * np.pi * t) * np.exp(-x_plot**2/(2*t))

    axes[i].hist(x, bins = 'auto', density=True)
    axes[i].plot(x_plot, y)
    axes[i].set_xlabel('x')
    axes[i].set_ylabel('probability density')
    axes[i].set_title(f"t = {t}")

plt.show()

