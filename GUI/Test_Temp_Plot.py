import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 
# Plot a heatmap for a numpy array:

uniform_data = [[5,10,15,20,25,30],[35,40,45,50,55,60],[65,70,75,80,85,90],[95,100,105,110,115,120],[125,130,135,140,145,150],[155,160,165,170,175,180]]
#print(uniform_data)
ax = sns.heatmap(uniform_data)
plt.xlabel('Coordinate_X')
plt.ylabel('Coordinate_Y')
plt.show()