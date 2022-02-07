num = [1,2,534,64,2,47,46,24,78,21,21]

odd = list(filter(lambda x: x%2!=0, num))
for x in odd:
    print(x)


print("Here's the list of odd numbers: {}".format(odd))

even = list(filter(lambda x: x%2 == 0, num))
print("Here's the list of even numbers: {}".format(even))

letters = ['a','b','l','o','w','t']
vowels = ['a','e','i','o','u']
filteredVowels = list(filter(lambda x: x in vowels, letters))
print(filteredVowels)
filteredConsonants = list(filter(lambda x: x not in vowels, letters))
print(filteredConsonants)


string = "Hello World."
vowels = ['a','e','i','o','u']
filteredVowels = list(filter(lambda x: x in vowels, string))
print("Vowels in {} : {}".format(string, filteredVowels))
filteredConsonants = list(filter(lambda x: x not in vowels, string))
filteredConsonants = list(filter(lambda x: x != " ",filteredConsonants))
print("Consonants in {} : {}".format(string, filteredConsonants))

#MAP FUNCTION
seq1 = (1,2,3)
seq2 = [4,5,9]
print(list(map(lambda x: x**2, seq1)))
print(list(map(lambda x: x**2, seq2)))


flag ='y'
while(flag =='y'):
    def power(n):
        return lambda x: x**n

    value = power(int(input("Power: ")))
    print(value(int(input("Base: "))))

    flag = input("Again? (press y for yes): ")