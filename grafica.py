import numpy as np
import matplotlib.pyplot as plt

nm, intensidad = np.loadtxt('nm_robot_uvc.txt', skiprows=1, usecols=[0,1], unpack=True)

print(nm,intensidad)

plt.title("Longitud de onda emitida por el robot")
plt.xlabel("Longitud de Onda (nm)")
plt.ylabel("Intensidad (ua)")
plt.rc('axes',labelsize = 25)
plt.grid()


plt.plot(nm,intensidad, "r")
plt.show()
