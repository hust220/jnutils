import sys
import math

def get_xyz(pdb):
    xyz = []
    for line in open(pdb):
        if (line[0:4] == "ATOM"):
            tmp = line.strip().split()
#            print tmp
            atom = tmp[2]
            if atom == "P":
#                x,y,z = float(tmp[6]), float(tmp[7]), float(tmp[8])
#                xyz.append((x,y,z))
                xyz.append(tmp)
    return xyz

tmp = get_xyz(sys.argv[1])
for i in tmp:
    for j in tmp:
        dx=float(i[6])-float(j[6])
        dy=float(i[7])-float(j[7])
        dz=float(i[8])-float(j[8])
        dist=dx**2+dy**2+dz**2
        dist = math.sqrt(dist)
        print '%s-%s_%s-%s %f' % (i[5], j[5], i[3], j[3], dist)


