import numpy as np

import matplotlib.pyplot as plt

# Create data points
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create the plot
plt.plot(x, y, 'b-', label='sine wave')
plt.title('Simple Sine Wave Plot')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.grid(True)
plt.legend()

# Display the plot
plt.show()