def multiplyMat(a, b):
    if len(a[0]) != len(b):
        return 0    
    m = list()
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            rsum = 0
            for k in range(len(b)):
                rsum += a[i][k]*b[k][j]
            row.append(rsum)
        m.append(row)
    return m

r1 = int(input("Matrix Multiplication\nEnter no of rows for 1st matrix A: "))
c1 = int(input("Enter no of columns for A: "))
r2 = int(input("Enter no of rows for 2nd matrix B: "))
c2 = int(input("Enter no of columns for B: "))

a = list()
b = list()
for i in range(r1):
    x=list()
    for j in range(c1):
        el = int(input(f"Enter no. for matrix A (R{i+1}, C{j+1}): "))
        x.append(el)
    a.append(x)
for i in range(r2):
    x=list()
    for j in range(c2):
        el = int(input(f"Enter no. for matrix B (R{i+1}, C{j+1}): "))
        x.append(el)
    b.append(x)

m = multiplyMat(a, b)

if m!=0:
    print("\n\nMatrix A = ", a, "\n\nMatrix B =", b, "\n\nA x B = ", m)
else:
    print("Error: Matrices cannot be multiplied. Dimensions mismatch.")