import camelcase
from FirstClassFunctions import tag  #this will show everything in FirstClassFunctions executed outside the main

a = tag("<html>")
a("Henry VI")

c = camelcase.CamelCase()
print(type(c))
print(c.hump("hello world"))

x=2.44489
print("I want {0:.2f} kilos of {1} right now. In case you don't have {1}, send {0:.1f} kilos of {2} instead.".format(x**2,c.hump("potatoes"),c.hump("rice")))