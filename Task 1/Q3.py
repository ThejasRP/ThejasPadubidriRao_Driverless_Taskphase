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
class Searching:
    @staticmethod
    def Q2(arr, strg):
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == strg:
                return True
            elif arr[mid] < strg:
                low = mid + 1
            else:
                high = mid - 1
        return False
n = int(input("Binary Search\nEnter number of elements in array: "))
Q1 = list()
for i in range(n):
    inp = input(f"Element {i+1}: ")
    Q1.append(inp)
Q1 = Sorting().selection(Q1)

strn = input("Enter string to search: ")
res = Searching.Q2(Q1, strn)

print("\nSorted Array is:", Q1)
print("String found:", res)



