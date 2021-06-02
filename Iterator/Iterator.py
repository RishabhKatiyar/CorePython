ls = [1,2,3,4]
# converting list to tuple
ls = tuple(i for i in ls)
# converting tuple to list
ls = [i for i in ls]

class My_Iterator:
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value > self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


def my_iter(start = 1, step = 1):
    while True:
        yield start
        start = start + step

if __name__ == "__main__":
    myiter = my_iter(start = 1, step = -1)
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))

    nums = My_Iterator(1,5)

    for num in nums:
        print(num)