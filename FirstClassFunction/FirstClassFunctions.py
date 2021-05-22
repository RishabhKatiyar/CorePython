def square(x):
    return x * x

def my_map(func, arg_list):
    results = []

    for arg in arg_list:
        results.append(func(arg))

    return results


squares = my_map(square, [1,2,3,4,5])

for square in squares:
    print(square)