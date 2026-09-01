n = int(input("Open Hashing\nEnter no of integers to input: "))
ht = [[] for i in range(10)]

for i in range(n):
    num = int(input(f"Enter number to hash ({i+1}): "))
    j = num % 10
    ht[j].append(num)

print("\nHash Table:-")
for i in range(10):
    print(i, ":", ht[i])



