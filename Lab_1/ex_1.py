import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 0.03, 0.0005)

x = lambda t : np.sin(520*np.pi*t + np.pi / 3)
y = lambda t : np.cos(280 * np.pi*t - np.pi / 3)
z = lambda t : np.cos(120*np.pi*t + np.pi / 3)

t = np.arange(0, 0.1, 1/200)
fig, axs = plt.subplots(3)
axs[0].stem(t, x(t))
axs[0].plot(np.arange(0, 0.1, 0.0005), x(np.arange(0, 0.1, 0.0005)))
axs[1].stem(t, y(t))
axs[1].plot(np.arange(0, 0.1, 0.0005), y(np.arange(0, 0.1, 0.0005)))
axs[2].stem(t, z(t))
axs[2].plot(np.arange(0, 0.1, 0.0005), z(np.arange(0, 0.1, 0.0005)))

plt.show()