# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 16:58:22 2016

@author: Brandon
"""

import numpy as np
np.random.seed(123)

random_walk = [0]

for x in range(100):
    step = random_walk[x]
    dice = np.random.randint(1,7)
    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step += 1
    else:
        step += np.random.randint(1,7)
    
    random_walk.append(step)

    
print(random_walk)

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Plot random_walk
plt.plot(random_walk)

# Show the plot
plt.show()