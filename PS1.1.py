import numpy as np
import matplotlib.pyplot as plt

A = 20
K = 100             # Carrying capacity?
r = 0.1
N0 = 50             # Starting population
dt = 1/1000         # Time step
tmax = 500          # end time
t_0 = int(5/dt)     # Starting time/padding

# Initialize population history N(t)
N = np.zeros((50, int((5+tmax)/dt+1)))
N[:, 0:t_0+1] = N0
Ndot = np.zeros((50, int(tmax/dt)))

T = np.linspace(0.1, 5, 50)

for i, delay in enumerate(T):
    print(f"{i} of {len(T)}")

    for t in range(int(tmax/dt)):
        Ndot[i, t] = r*N[i, t+t_0] * (1 - N[i, t+t_0-int(delay/dt)]/K) * (N[i, t+t_0]/A - 1)
        N[i, t+t_0+1] = N[i, t+t_0] + Ndot[i, t]*dt

for i, row in enumerate(N):
    if i%10 == 0:
        plt.plot(row, label=f'delay: {T[i]} s')

plt.legend()
plt.show()

hej = 1
