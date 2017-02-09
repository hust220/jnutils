import sys
import re

a = []
for line in open(sys.argv[1]):
    arr = re.split('\s+', line.strip())
    d = float(arr[5])
    if d > 0.04:
        a.append([int(arr[0]), int(arr[2]), float(arr[5])])

b = []
for i in a:
    if not i[0] in b:
        b.append(i[0])
    if not i[1] in b:
        b.append(i[1])
b.sort()

c = []
for line in open(sys.argv[2]):
    arr = re.split('\s+', line.strip())
    if len(arr) >= 2:
        i = int(arr[1])
        if not i in c:
            c.append(i)
c.sort()

print 'nodedef> name VARCHAR,label VARCHAR,color VARCHAR'
for i in b:
    if i in c:
        print '%d,%d,%s' % (i, i, "'255,255,0'")
    else:
        print '%d,%d,%s' % (i, i, "'255,255,255'")

print 'edgedef> node1,node2,weight DOUBLE'
for i in a:
    print '%d,%d,%f' % (i[0],i[1],i[2])

