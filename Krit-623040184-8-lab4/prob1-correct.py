product = 1
for i in range(1, 10):
    product *= i
print("product is {}".format(product))

sum_squares = 0
for i in range(10):
    i_sq = i ** 2
    sum_squares += i_sq
print("sum_squares is {}".format(sum_squares))

nums = 0
for num in range(10):
    nums += num
print("nums is {}".format(nums))
