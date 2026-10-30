import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math


f = 3  
fs = 100 
t = np.arange(0, 1, 1/fs)
x = np.sin(2 * np.pi * f * t)


omegas = [1, 3, 5, 7]


fig2, axes2 = plt.subplots(2, 2, figsize=(10, 10))
fig2.suptitle('Înfășurarea semnalului în planul complex')
axes_flat = axes2.flatten()

for idx, omega in enumerate(omegas):
    z = x * np.exp(-2j * np.pi * omega * t)
    distanta = np.abs(z) 
    
    ax = axes_flat[idx]
    ax.plot(z.real, z.imag, color='blue', alpha=0.5, label='Traiectoria')
    sc = ax.scatter(z.real, z.imag, c=distanta, cmap='cool', s=15)
    ax.axhline(0, color='black', lw=0.5)
    ax.axvline(0, color='black', lw=0.5)
    ax.set_title(f'\u03c9 = {omega}')
    ax.set_xlim([-1.2, 1.2])
    ax.set_ylim([-1.2, 1.2])
    ax.grid(True, linestyle=':', alpha=0.5)

plt.tight_layout()
plt.savefig('ex2_infasurare_complexa.pdf')
plt.show()


fig_anim, ax_anim = plt.subplots(figsize=(6, 6))
ax_anim.set_xlim(-1.2, 1.2)
ax_anim.set_ylim(-1.2, 1.2)
ax_anim.axhline(0, color='black', lw=0.5)
ax_anim.axvline(0, color='black', lw=0.5)
ax_anim.set_title('Animație în timp real (\u03c9 = 3)')

z_anim = x * np.exp(-2j * np.pi * 3 * t)
dist_anim = np.abs(z_anim)

scat = ax_anim.scatter([], [], c=[], cmap='cool', s=15)
indicator, = ax_anim.plot([], [], 'ro', markersize=8) 

def init():
    scat.set_offsets(np.empty((0, 2)))
    indicator.set_data([], [])
    return scat, indicator

def update(frame):
    current_data = np.c_[z_anim.real[:frame], z_anim.imag[:frame]]
    scat.set_offsets(current_data)
    scat.set_array(dist_anim[:frame])
    
    indicator.set_data([z_anim.real[frame]], [z_anim.imag[frame]])
    return scat, indicator


ani = animation.FuncAnimation(fig_anim, update, frames=len(t), init_func=init, blit=True, interval=50)
plt.show()