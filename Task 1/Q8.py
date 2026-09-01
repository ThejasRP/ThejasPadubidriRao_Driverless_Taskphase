import csv
import math
def sorter(p, colour):
    sl = p.copy() 
    cl = list()
    for i in range(len(sl)):
        min_i = i
        min_d = math.sqrt(float(sl[min_i][1])**2+float(sl[min_i][2])**2)
        for j in range(i + 1, len(sl)):
            j_d = math.sqrt(float(sl[j][1])**2+float(sl[j][2])**2)
            if j_d < min_d:
                min_i = j
                min_d = j_d
        sl[i], sl[min_i] = sl[min_i], sl[i]
    for el in sl:
        if el[3].strip().lower() == colour.lower():
            cl.append(el)
    return cl

d = list()
with open("cones.csv", "r", newline="") as f:
    c = csv.reader(f)
    for r in c:
        if r: 
            d.append(r)
bl = sorter(d, "blue")
yl = sorter(d, "yellow")
with open("blue_cone.csv", "w", newline="") as f:
    c = csv.writer(f)
    c.writerows(bl)
with open("yellow_cone.csv", "w", newline="") as f:
    c = csv.writer(f)
    c.writerows(yl)

m = []
for rb in bl:
    ld = float('inf') 
    lp = 0
    for i in range(len(yl)):
        ry = yl[i]
        dist = math.sqrt((float(ry[1])-float(rb[1]))**2+(float(ry[2])-float(rb[2]))**2)
        if dist < ld:
            ld = dist
            lp = i
    if len(yl) > 0:
        mid_x = (float(rb[1])+float(yl[lp][1]))/2
        mid_y = (float(rb[2])+float(yl[lp][2]))/2
        m.append([mid_x, mid_y])
with open("centreline.csv", "w", newline="") as f:
    c = csv.writer(f)
    c.writerows(m)
    
print("Cones Sorter\n\nExecuted Successfully")






