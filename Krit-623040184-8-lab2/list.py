WD = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
WE = ['Saturday', 'Sunday']

D7 = WD + WE
D7S = WD + WE
D7S.sort()
D7R = WD + WE
D7R.reverse()
L = WD + WE

print("Weekday are", WD)
print("Weekend are", WE)
print("Days are", D7)
print("Sorted are", D7S)
print("Reverse days are", D7R)
print("The last two days of the list day are", L[-2:])
