#help(RuntimeError)

#ord() and chr()
print(ord('A'))
print(chr(83))

class A:
    def __init__(self):
        print("Hello World")
class B(A):
    def __init__(self):
        super().__init__()
        A.__init__(self) #both are similar
#a = A()
b = B()

#partition()
print("Hello Ram I have a news about crypto".partition("news"))
print("hello world".capitalize())

#max() in dictionaries
dict = {1:4,2:11,-2:1,-5:-8,8:3}
print(max(dict)) #MAXIMUM KEY
print(max(dict, key = lambda x: dict[x])) #KEY WITH MAXIMUM VALUE
print("Maximum value: {}".format(dict[max(dict, key = lambda x: dict[x])])) #MAXIMUM VALUE



import math
#filter out perfect squares
num =int(input("How far do you want to search for perfect squares?: "))
a = []
for x in range(1,num+1):
    a.append(x)
print(list(filter(lambda x:math.sqrt(x)/math.sqrt(x).__ceil__()==1,a)))

#print(int('0b100', base=0))

a = [1,2,3,4]
for i in range(2):
    print(a.pop(1))


a = input("Enter a binary number: ")
for x in a:
    if x=='0' or x=='1':
        pass
    else:
        print("Invalid entry")
        break
print("{} in decimal: {}".format(a,int(a, base=2)))

