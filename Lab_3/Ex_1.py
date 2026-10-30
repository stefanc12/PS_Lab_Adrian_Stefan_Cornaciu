import numpy as np
import matplotlib.pyplot as plt
import math

N = 8
n = np.arange(N)
k = n.reshape((N, 1))
F = math.e**(-2j * np.pi * k * n / N)

print(F)

F_H = F.conj().T
produs = np.dot(F_H, F)
este_unitara = np.allclose(produs, N * np.eye(N))
print(este_unitara)


fig, axes = plt.subplots(N, 2, figsize=(12, 16))

for i in range(N):

    axes[i, 0].stem(n, F[i, :].real)
    axes[i, 0].set_ylabel(f'Linia {i}')
    if i == 0:
        axes[i, 0].set_title('Partea Reală')
    
    axes[i, 1].stem(n, F[i, :].imag)
    if i == 0:
        axes[i, 1].set_title('Partea Imaginară')

plt.tight_layout(rect=[0, 0.03, 1, 0.97])
plt.savefig('ex1.pdf')
plt.show()