import matplotlib.pyplot as plt

x = [1,2,3]
xticks = ['v173', 'v135', 'v141']
y = [13, 15, 1]
x2 = [1,2,3]
x2ticks = ['v123173', 'v135', 'v141']
y2 = [11, 11, 11]
plt.xticks(x,xticks)
plt.scatter(x, y,800, marker='o', alpha=0.5, color='blue')
plt.scatter(x2, y2, 800, marker='o', alpha=0.5, color='green')
plt.show()
