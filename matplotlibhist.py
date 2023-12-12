import matplotlib.pyplot as plt

data = [2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 7, 8, 8, 8, 8, 8]
plt.hist(data, color='blue', edgecolor='black' , bins=7)

plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram Example')
plt.show()

