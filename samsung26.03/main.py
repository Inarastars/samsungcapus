# вывести 30
# #list_array = [[10, 20], [30, 40], [50,60]]
#print(list_array[1][0])

#сделать матрицу 4 на 4
#a = []
#num = 1
#for i in range(4):
#    row = []
#    for j in range(4):
#        row.append(num)
#        num += 1
#    a.append(row)
#for row in a:
#    print(*row)

#комп спрашивает у пользователя n и по нему делает матрицу из 0 и 1
#n = int(input("Enter n:"))
#for i in range(n):
#    for j in range(n):
#        print((i +j)% 2, end=" ")
#    print()

#делает матрицу из n
#n = int(input("Enter n: "))
#mat = [[(i * n) + j + 1 for j in range(n)] for i in range(n)]
#a = []
#num = 1
#for i in range(n):
#    row = []
#    for j in range(n):
#        row.append(num)
#        num += 1
#    a.append(row)
#for row in a:
#    print(*row)
#pov = [[mat[n - j - 1][i] for j in range(n)] for i in range(n)]
#for row in pov:
#    print(" ".join(map(str, row)))

#делает матрицу и поворачивает ее
n = int(input("Enter n: "))
a = []
m = 1

for i in range(n):
    row = []
    for j in range(n):
        row.append(m)
        m += 1
    a.append(row)

print("Original matrix:")
for row in a:
    print(*row)

povorot_mat = [[0] * n for h in range(n)]

for i in range(n):
    for j in range(n):
        povorot_mat[j][n - 1 - i] = a[i][j]

print("Rotated matrix:")
for row in povorot_mat:
    print(*row)
