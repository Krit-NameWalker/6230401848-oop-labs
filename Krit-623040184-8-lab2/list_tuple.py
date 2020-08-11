A = [(1, ), (2, 2), (3, 3, 3)]
B = [list(range(0, 10)), list(range(10, 20)), list(range(20, 30)), list(range(30, 40))]
Count_A1 = 0
Count_A2 = 0
Count_B = 0

for x in A:
    Count_A1 += 1
    if Count_A1 == 2:
        for y in x:
            Count_A2 += 1
            if Count_A2 == 2:
                print(y)

for x in B:
    Count_B += 1
    if Count_B == 1:
        print([x[-2], x[-1]])
