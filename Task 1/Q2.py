class Sorting:
    @staticmethod
    def selection(arr):
        n = len(arr)
        for i in range(n - 1):
            min_i = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_i]:
                    min_i = j
            arr[i], arr[min_i] = arr[min_i], arr[i]
        return arr
n = int(input("Array Selection Sort\nEnter number of elements in array: "))
ar = list()
for i in range(n):
    inp = input(f"Element {i+1}: ")
    ar.append(inp)
res = Sorting().selection(ar)

print("\nSorted Array is:", res)

