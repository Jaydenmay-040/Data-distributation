import matplotlib.pyplot as plt
import numpy as np
names = ['Andy', 'Martin', 'Zahara', 'Vuyo', 'Ziyaad']
marks = [12,  99, 65, 85, 42]
x_pos = [i for i, _ in enumerate(names)] # labels on the x-axis
# labeling and visuals
plt.bar(x_pos, marks, color='blue')
plt.xlabel("Names")
plt.ylabel("Marks (%)")
plt.title("Python marks for 5 students")
plt.xticks(x_pos, names)
plt.show()
