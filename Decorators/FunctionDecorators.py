# function as decorators
def decorator_function(original_function):

    def wrapper_function(*args, **kwargs):
        print('Wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

# this is equal to 
def display1():
    print('display function ran')
decorated_function = decorator_function(display1)
decorated_function()

# this
@decorator_function
def display2(name, age):
    print(f'Name = {name}, Age = {age}')
display2('Rishabh', 29)
