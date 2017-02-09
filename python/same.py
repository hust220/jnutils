import sys
import re

a = []
for line in open(sys.argv[1]):
    arr = re.split('\s+', line.strip())
    a.append([int(arr[0]), int(arr[1])])

n = 0
for line in open(sys.argv[2]):
    arr = re.split('\s+', line.strip())
    arr = [int(arr[0]), int(arr[2])]
    if n > 0:
        for l in a:
            if arr[0] == l[0] and arr[1] == l[1] or \
               arr[0] == l[1] and arr[1] == l[0]:
                print line,
    else:
        print line,
    n += 1
