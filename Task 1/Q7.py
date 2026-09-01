import math

def coordSorter(p, ref):
    sl = p.copy()
    for i in range(len(sl)):
        min_i = i
        min_d = math.sqrt((float(sl[min_i][0])-float(ref[0]))**2+(float(sl[min_i][1])-float(ref[1]))**2)
        for j in range(i + 1, len(sl)):
            j_dist = math.sqrt((float(sl[j][0])-float(ref[0]))**2+(float(sl[j][1])-float(ref[1]))**2)
            if j_dist < min_d:
                min_i = j
                min_d = j_dist
        sl[i], sl[min_i] = sl[min_i], sl[i]
    return sl

cl = [(0,1), (0,3), (1,2)]
print("Coordinates Sorter")
x = float(input("Enter coordinates for reference point:-\nX: "))
y = float(input("Y: "))
ref = (x, y)

sorted_cl = coordSorter(cl, ref)
print("\nSorted Coordinates as per proximity to reference:-\n", sorted_cl)




