n = int(input("Open Hashing (with Sorting)\nEnter no of integers to input: "))
ht = [[] for i in range(10)]

for i in range(n):
    num = int(input(f"Enter number to hash ({i+1}): "))
    j = num % 10
    l = 0
    h = len(ht[j])
    while l < h:
        m = (l + h) // 2
        if ht[j][m] < num:
            l = m + 1
        else:
            h = m
    ht[j].insert(l, num)

print("\nHash Table (Sorted):-")
for i in range(10):
    print(i, ":", ht[i])





