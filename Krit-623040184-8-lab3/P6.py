months = ("January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October",
          "November", "December")
num_days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
month_dict = {}

for n in range(len(months)):
    month_dict.update({months[n]: num_days[n]})
print(month_dict.items())
months_name = str(input("Enter mouth: "))
print("Number of days in", months_name, "is", month_dict[months_name])
