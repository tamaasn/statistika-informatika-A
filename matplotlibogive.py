import numpy as np
import matplotlib.pyplot as plt


data = np.array([1,1,1,2,2,3,4,4,5])
unique , counts = np.unique(data , return_counts=True)
cumulative = []
cumulative_temp = 0
for i in range(len(counts)):
    cumulative_temp += counts[i]
    cumulative.append(cumulative_temp)

plt.plot(unique,cumulative, color='black' , marker='o' , linestyle='-')
plt.show()
