nums = (2, 10, 11, 3)
print("{:30}{}".format("input filenames are", nums))

list = []
for n in nums:
    filel_num = "filel_:{:04}".format(n)
    list.append(filel_num)
print("{:30}{}".format("zero padded filenames", list))

sort = list.sort()
print("{:30}{}".format("sorted filenames are", list))