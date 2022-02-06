def outer_func():
     name = "Hrishi"

     def inner_func():
        print("Hello {}".format(name))

     return inner_func() #executes and returns NONE

a = outer_func()
print("What's returned? : {} ".format(a))
print(type(a))

def outer_func():
    name = "Hrishi"

    def inner_func():
        print("Hello {}".format(name))

    return inner_func  # returns the function without executing


myfunc = outer_func
print(myfunc.__name__)
print(myfunc)
a = myfunc() #a is
print(a.__name__)
a()

my_func = outer_func() #my_func is a variable that stores function object returned by outer_func()
my_func()
my_func()
my_func()

#closure advanced example
import logging
logging.basicConfig(filename = "LoggingExample.log", level = logging.INFO)

def logger(func):
    def log_func(*args):
        logging.info('Running "{}" with {} arguments'.format(func.__name__, args))
        print(func(*args))
    return log_func

def add2(x,y):
    return x+y

def add3(x,y,z):
    return x+y+z

def sub(x,y):
    return x-y

add2_logger = logger(add2)
add3_logger = logger(add3)
sub_logger = logger(sub)

add2_logger(2,4)
add3_logger(2,4,1)
sub_logger(6,1)

