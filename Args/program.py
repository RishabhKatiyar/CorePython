
def func1(item, *args, **kwargs):

    print(item)

    if args:
        print("Printing args")
        for item in args:
            print(item)

    if kwargs:
        print("Printing kwargs")
        for item in kwargs:
            print(item, end = "\t")
            print(kwargs[item])



if __name__ == "__main__":
    #func110) <- works fine
    #func1(11, [1,2,3], 1, a = {"a","b"}, b = {"c", "d"}, [1,2]) # error
    #func1(11, [1,2,3], 1, a = {"a","b"}, b = {"c", "d"}, 1) # error
    #func1(11, [1,2,3], 1, a = {"a","b"}, b = {"c", "d"})
    func1(11, 12, [1,2,3], 1, a = {"a","b"}, b = {"c", "d"})
