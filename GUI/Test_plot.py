import numpy as np
import matplotlib.pyplot as plt
import time
import json


localtime = time.time()
print ("本地时间为 :", localtime)

#plt.xlabel('Coordinate_X')
#plt.ylabel('Coordinate_Y')
with open("./Sigfox_2A0D6F8/Sigfox_2A0D6F8.json", 'r') as f:
    data = json.load(f)
print(data)
 
X, Y = np.meshgrid(np.arange(0, 2 * np.pi, .2), np.arange(0, 2 * np.pi, .2))
U, V = np.cos(X), np.sin(Y)
fig, ax = plt.subplots()

Q = ax.quiver(X[::3, ::3], Y[::3, ::3], U[::3, ::3], V[::3, ::3], units='inches', pivot='mid')
#qk = ax.quiverkey(Q, 0.9, 0.9, 1, r'$1 \frac{m}{s}$', labelpos='E', coordinates='figure')
#ax.scatter(X[::3, ::3], Y[::3, ::3], color='r', s=5)
plt.xlabel('Coordinate_X')
plt.ylabel('Coordinate_Y')
plt.savefig('./Airflow/'+ str(localtime) + '.jpg')
plt.show()