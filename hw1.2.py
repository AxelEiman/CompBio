import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm

K = 1000
r = 0.1
b = 1
N_0 = [1,2,3,10]
tot_steps = 100

# Exact population dynamics
N = np.zeros((4, tot_steps))
for i, N0 in enumerate(N_0):
    N[i, 0] = N0
    for t in range(tot_steps - 1):
        N[i, t + 1] = (r + 1) * N[i, t] / (1 + (N[i, t] / K) ** b)

# Linear approximation around unstable fp
unstable_slope = 1+r

Nlin = np.zeros((4,tot_steps))
for i, N0 in enumerate(N_0):
    Nlin[i, 0] = N0
    for t in range(tot_steps-1):
        Nlin[i, t+1] = unstable_slope*Nlin[i, t]

colors = ['red', 'green', 'black', 'blue']

# Plotting exact population dynamics
for i, row in enumerate(N):
    plt.loglog(row, c=colors[i], label=f'N_0 = {N_0[i]}')

# Plot linear stability analysis
for i, row in enumerate(Nlin):
    plt.loglog(row, c=colors[i], linestyle='dotted')

plt.ylim((1, 200))
plt.ylabel('N')
plt.xlabel('tau')
plt.legend()
plt.show()

# f) Approximation near stable steady state
dN0 = [-10, -3, -2, -1, 1, 2, 3, 10]
Nstar = 100
stable_slope = 1 - b*r/(1+r)
Ns = np.zeros((len(dN0), 100))
for i, N0 in enumerate(dN0):
    Ns[i, 0] = N0
    for t in range(tot_steps-1):
        Ns[i, t+1] = Ns[i,t]*stable_slope
Ns += Nstar

# Exact population dynamics
N_ex = np.zeros((len(dN0), tot_steps))

for i, N0 in enumerate(dN0):
    N_ex[i, 0] = N0 + Nstar
    for t in range(tot_steps - 1):
        N_ex[i, t + 1] = (r + 1) * N_ex[i, t] / (1 + (N_ex[i, t] / K) ** b)

colors = cm.jet(np.linspace(0, 1, len(dN0)))

for i, row in enumerate(Ns):
    plt.loglog(row, c=colors[i], linestyle='dotted')

for i, row in enumerate(N_ex):
    plt.loglog(row, c=colors[i], label=f'$N_0$={dN0[i]}')

plt.legend(loc='upper right')
plt.xlabel('tau')
plt.ylabel('N')
plt.show()

