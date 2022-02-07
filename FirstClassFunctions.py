def square():
    def show():
        print("Hello")
    return(show)

a = square()
a()

def square(num):
    def display():
        print(num*num)
    return(display)
a = square(4)
a()

def tag(tag):
    def message(msg):
        print("<{0}>{1}</{0}>".format(tag,msg))
    return(message)

h1 = tag("h1")
h1("Hello World")
h1("Hello Earth")

def printHello():
    print("Hello from a function")

if __name__ == "__main__":
    printHello()