import matplotlib.pyplot as plt
import random
import numpy as np

data = np.array([1,1,1,1,1,4,4,4,4,5,5,3,3,3,2,2,2])
unique , count = np.unique(data , return_counts=True)
plt.plot(unique , count, color='black' , marker='o' , linestyle='-')
plt.show()
