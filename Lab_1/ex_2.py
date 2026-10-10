import numpy as np
import matplotlib.pyplot as plt

 

x = lambda t : np.sin(800*np.pi*t)
y = lambda t : np.sin(1600*np.pi*t)
z = lambda t : 2 * np.mod(t * 240, 1) -1
w = lambda t : np.sign(np.sin(2 * np.pi * 300 * t))
s = np.random.uniform(0, 1, (128, 128))
f = np.zeros((128, 128))
for i in range(128):
    for j in range(128):
        if i <= j : 
            f[i, j] = np.sin(2 * np.pi + j / 128)
        else : 
            f[i, j] = np.sin(2 * np.pi + i / 128)




fig, axs = plt.subplots(3, 2)
axs[0, 0].plot(np.arange (0, 0.05, 0.05/1600), x(np.arange (0, 0.05, 0.05/1600)))
axs[0, 1].plot(np.arange (0, 3, 1/10000), y(np.arange (0, 3, 1/10000)))
axs[1, 0].plot(np.arange (0, 0.05, 0.05/1600), z(np.arange (0, 0.05, 0.05/1600)))
axs[1, 1].plot(np.arange (0, 0.05, 0.05/1600), w(np.arange (0, 0.05, 0.05/1600)))
axs[2, 0].imshow(s)
axs[2, 1].imshow(f)


plt.show()