students = ['Ram', 'Sita', 'Dinesh', 'Jessica']
a,b,c,d = students
print(a)

newStudents1 = ['Hrishi', 'Janak', 'Rina', 'Puja']
students1 = students.copy() #copying a list
students1.append(newStudents1) #appending another list
print("Appending another list: {}".format(students1))
newStudents2 = ['Mina', 'Tina']
students2 = students.copy()
students2.extend(newStudents2) #extending another list
print("Extending another list: {}".format(students2))
print("Original list: {}".format(students))
students.append('Rahul') #appending an element to the list
students.append('Rahul')
print(students)

print("Count of \"Rahul\" : {}".format(students.count('Rahul'))) #list allows duplicate elements
students.reverse() #reverse a list DOES NOT RETURN A NEW LIST, JUST CHANGES students
print("Resevsed list: {}".format(students))
print(type(students.reverse()))
students.sort() #sort a list JUST CHANGES students
print(students)

print(students.pop()) #pop the last element
print(students)
students.remove('Rahul') #remove the specified element
print(students)

students.insert(1,'Sajan') #insert element to specified index
print(students)
students.clear() #remove all the elements of the list
print(students)

del students
#print(students)

def returnList(A):
    B = []
    for i in range(len(A)):
        B.append(A.pop())
    print(B)
    return B

print(returnList([1,2,3,4]))

a = [1,2,3,4]
b = []
for i in range(len(a)):
    b.append(a.pop())
print(b)


def rev1(list):
    newList = listA.copy()
    for i in range(len(listA)):
        newList[len(listA)-1-i] = listA[i]
    return(newList)

def rev2(A):
    newA = A.copy()  #otherwise reversed A will be passed to rev3
    newA.reverse()  #just changes 'newA'
    return(newA)

def rev3(A):
    B = []
    for i in range(len(A)):
        B.append(A.pop())
    print(B)
    return B

count = int(input(("How long do you want a list?: ")))
listA = []
for i in range(count):
    listA.append(int(input("Enter num{} : ".format(i+1))))
print(listA)
print(rev1(listA))
print(rev2(listA))
print(rev3(listA))


print("Hi")

