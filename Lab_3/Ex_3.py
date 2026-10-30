import numpy as np
import matplotlib.pyplot as plt


f1, f2, f3 = 10, 30, 60
fs = 200 
N = fs
t = np.arange(0, 1, 1/fs)


x_compus = np.cos(2 * np.pi * f1 * t) + 2 * np.cos(2 * np.pi * f2 * t) + 0.5 * np.cos(2 * np.pi * f3 * t)

frecvente = np.fft.fftfreq(N, d=1/fs)
X_omega = np.fft.fft(x_compus)

'''
x_omega = np.zeros(len(frecvente), dtype=complex)
frecvente = np.arange(1, N)


for idx, omega in enumerate(frecvente):
    suma = 0
    for n in range(N):
        suma += x_compus[n] * np.exp(-2j * np.pi * n * omega / N)
    X_omega[idx] = suma

'''



fig3, (ax_timp, ax_freq) = plt.subplots(1, 2, figsize=(14, 5))


ax_timp.plot(t, x_compus)
ax_timp.set_title('Semnalul x(t)')
ax_timp.set_xlabel('Timp (s)')
ax_timp.set_ylabel('Amplitudine')
ax_timp.grid(True, alpha=0.3)


ax_freq.stem(frecvente, np.abs(X_omega))
ax_freq.set_title('Modulul Transformatei Fourier')
ax_freq.set_xlabel('Frecvența (Hz)')
ax_freq.set_ylabel('Amplitudine')
ax_freq.set_xticks([10, 30, 60, 100])
ax_freq.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('ex3.pdf')
plt.show()