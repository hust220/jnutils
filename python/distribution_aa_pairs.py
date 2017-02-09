import numpy as np  
import matplotlib.pyplot as plt  
import sys
import re

data = {}
labels = []
pairs = []
for line in open(sys.argv[1]):
    arr = re.split('\s+', line.strip())
    if arr[0] == 'name':
        labels = arr[1:]
        for i in labels:
            data[i] = []
    elif len(arr) > 1:
        pairs.append(arr[0])
        for i in range(0,len(arr)-1):
            data[labels[i]].append(int(arr[i+1]))
 
n_groups = len(pairs)
fig, ax = plt.subplots()  
index = np.arange(n_groups)  
bar_width = 1.0 / (len(pairs)+1)
print bar_width, ' ', n_groups
print labels
print pairs
print data

opacity = 0.4  
n = 0
colors = ['b', 'r', 'g', 'y', 'c', 'm', 'r', 'k', 'b', 'r', 'g', 'y']
for i in labels:
    plt.bar(index, data[i], bar_width,alpha=opacity, color=colors[n],label=i)  
    index = index+bar_width
    n += 1
  
plt.xlabel('Group')  
plt.ylabel('Counts')  
plt.title('Distribution')  
plt.xticks(index-bar_width*(len(labels)/2), pairs, rotation=45)  
plt.ylim(0,40)  
plt.legend()  
  
plt.tight_layout()  
plt.show()
