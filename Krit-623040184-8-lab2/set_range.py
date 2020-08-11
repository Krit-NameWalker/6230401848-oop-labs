A = {1, 2, 3, 4}
B = {1, 3, 5, 7}
C = A | B
D = A - B
aa = []
ab = []
ac = []

print("A is", A)
print("B is", B)
print("A | B is", C)
print("A - B is", D)

for n in range(20):
    aa.append(n)
print(aa)

x = range(3, 13)
for n in x:
    ab.append(n)
print(ab)

y = range(2, 51, 3)
for n in y:
    ac.append(n)
print(ac)
