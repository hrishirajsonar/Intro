def decorator_function(original_function):
    def wrapper_function():
        original_function()
    return wrapper_function

def say_Hi():
    print("Hi there")

decorated_hi = decorator_function(say_Hi)
decorated_hi()

name = "Gaudy"
ageVariable = 21
def firstname():
    print(name)
def age():
    print(ageVariable)


def decorator(info):
    def wrapper():
        print("The information you requested i.e. {}".format(info.__name__))
        info()
    return wrapper
display_firstname = decorator(firstname)
display_age = decorator(age)
display_age()
display_firstname()


