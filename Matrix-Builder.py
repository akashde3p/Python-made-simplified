# FOLLOWING IS THE METHOD OF CREATING MATRICES "X", "Y" AND "Z" IN WHICH WE ARE ALLOWING THE USER TO INPUT VALUES
x = []
y = []
z = []
rowx = int(input("enter number of rows of X matrix"))
colx = int(input("enter number of columns of X matrix"))
rowy = int(input("enter number of rows of Y matrix"))
coly = int(input("enter number of columns of Y matrix"))

for m in range(0, rowx):
    x.append([])
    for n in range(0, colx):
        a = int(input("enter number in X matrix"))
        x[m].insert(n, a)
print(x)
for q in range(0, rowy):
    y.append([])
    for t in range(0, coly):
        b = int(input("enter number in Y matrix"))
        y[q].insert(t, b)
print(y)
for p in range(0, rowx):
    z.append([])
    for h in range(0, coly):
        z[p].insert(h, 0)
print(z)

# NOW COMES THE MULTIPLICATION PART
print("X=", x)
print("Y=", y)
for i in range(0, len(x)):
    for j in range(0, len(y[0])):
        for k in range(0, len(y)):
            z[i][j] = z[i][j] + x[i][k] * y[k][j]
print("Z=", z)
