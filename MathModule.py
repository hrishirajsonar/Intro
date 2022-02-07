import math

print(math.ceil(3.8)) #ceiling
print(math.floor(3.8)) #floor
print(math.sqrt(8)) #square root
print(math.sin(11)**2+math.cos(11)**2)
print(math.sin(math.pi/2))
print(math.degrees(math.pi)) #radian to degree
print(math.radians(180)) #degrees to radians
print(math.sin(math.radians(90)))
print(math.sin(math.pi))
print(math.sin(math.radians(180)))
print(pow(5,6))
print(math.pow(5,6)) #power
print(abs(-6))
print(math.fabs(-6)) #this is also absolute value
print(math.comb(5,2)) #combination
print(math.perm(5,2)) #permutation
print(math.dist([2,3],[3,4])) #Euclidean distance
print(math.factorial(4))
print(math.exp(0)) #exponential i.e. e^x
print(math.isfinite(1))
print(math.isfinite(float("inf")))
print(math.isfinite(math.inf)) #math.inf
print(-math.inf)
print(float("inf")) #other strings cannot be converted to float
print(float("-inf"))
print(math.prod([4,6,7,8])) #products of all num in iterable
print(math.prod((5,7,8,2)))
print(math.prod(range(2,4)))
a = range(5,51,5)
for x in a:
    print(x)
print(math.fsum([1,6,4,6,7,2])) #sum of all numbers in iterable
print(math.fsum(range(1,11,2))) #range(start, end *not included*, step)
print(math.fmod(25,11)) #modular division
print("math.remainder(31/11): {}".format(math.remainder(31,11))) #return diff between x and closest integer of y
print(math.trunc(3.8)) #not ceil or floor, simply removes the decimal part
print(math.trunc(-1.56))
print("Gamma of 4: {}".format(math.gamma(4)))
