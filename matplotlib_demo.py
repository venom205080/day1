import matplotlib.pyplot as plt
import numpy as np

# --------Line Graph in Matplotlib--------
# x = [3, 1, 3] 
# y = [3, 2, 1] 

# plt.plot(x, y)
# plt.title("Line Chart")
# plt.legend(["Line"])
# plt.show()

# -----------Stem Plot in Matplotlib---------
# x = np.linspace(0.1, 2 * np.pi, 41) 
# y = np.exp(np.sin(x)) 

# plt.stem(x, y) 
# plt.show() 


# ---------Bar chart in Matplotlib---------
x = [3, 1, 3, 12, 2, 8, 4] 
y = [3, 2, 1, 4, 5, 10, 7] 

# This will plot a simple bar chart
plt.bar(x, y)

# Title to the plot
plt.title("Bar Chart")

# Adding the legends
plt.legend(["bar"])
plt.show()