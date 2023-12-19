import numpy as np
import matplotlib.pyplot as plt

nm, intensidad = np.loadtxt('250 nm.txt', skiprows=1, usecols=[0,1], unpack=True)

print(nm,intensidad)

plt.title("Longitud de onda emitida por el robot")
plt.xlabel("Longitud de Onda (nm)")
plt.ylabel("Intensidad (ua)")
plt.rc('axes',labelsize = 25)
plt.grid()


plt.plot(nm,intensidad, "r")
plt.show()
