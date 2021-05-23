def square_numbers(nums):
    for num in nums:
        yield num * num # yield it the keyword 
                        # that makes it a generator

print("From Generator :: ")

print("While Loop:")
my_nums = square_numbers([1, 2, 3, 4, 5])
while True:
    try:
        print(next(my_nums))
    except:
        break

print('For Loop:')
my_nums = square_numbers([1, 2, 3, 4, 5])
for num in my_nums:
    print(num)

print("From Comprehension :: ")

print("While Loop:")
my_nums = [x*x for x in [1, 2, 3, 4, 5]]
while True:                 # nothing is printed
    try:
        print(next(my_nums))
    except:
        break

print('For Loop:')
my_nums = [x*x for x in [1, 2, 3, 4, 5]]
for num in my_nums:
    print(num)