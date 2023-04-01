import matplotlib.pyplot as plt
import numpy as np


y = np.array([22.2, 17.6, 8.8, 8, 7.7, 6.7])
mylabels = ["Java", "Python", "PHP", "JavaScript","C#","C++"]


plt.pie(y,labels=mylabels, shadow=True,explode=(0.1, 0, 0, 0,0,0), autopct='%1.2f%%')

plt.show()
