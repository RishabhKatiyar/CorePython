class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function
    
    def __call__(self, *args, **kwargs):
        print('Class method executed this before {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)

@decorator_class
def display3():
    print("Hello")
display3()

@decorator_class
def display4(name, age):
    print(f'Name = {name}, Age = {age}')
display4('Rishabh', 29)