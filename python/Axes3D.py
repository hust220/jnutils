#! /home/wangjian/programs/Anaconda-2.1.0/bin/python

import sys
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

a = np.loadtxt(sys.argv[1])
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
lim = int(sys.argv[2])
ax.set_xlim([-lim, lim])
ax.set_xlabel('x')
ax.set_ylim([-lim, lim])
ax.set_ylabel('y')
ax.set_zlim([-lim, lim])
ax.set_zlabel('z')
ax.scatter(a.T[0], a.T[1], a.T[2])
ax.plot(a.T[0], a.T[1], a.T[2])
plt.show()
