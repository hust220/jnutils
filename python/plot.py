import numpy as np
import matplotlib.pyplot as plt
import sys

plt.plot(np.loadtxt(sys.argv[1]))
plt.show()
