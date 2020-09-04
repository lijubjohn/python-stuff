# take a english sentence < 30 len from user - i/p

# if length of sentence contains more than 10 words - show invalid message to use  -> if else

# function to  get count of number of vowels in the sentence - use loop

# function to get vowels in the sentence  - list

# function to get frequency of each vowel - dict

# print vowels - loop
word = "my name is liju"
vowels = ['a', 'e', 'i', 'o', 'u']
found = []
for letter in word:
    if letter in vowels:
        found.append(letter)

print(found)

# if-else  -> check if some condition then do something


# print freq of each - dict


#

# create 3 x 3 matrix and print the sum of diagonal elements

# Give the o/p
#
x = "Hello" + 1 + 2 + 3
print(x)

#
x = "Hello"
x.lower()
print(x)

#
x = '10.5'
print(type(x))

#
x = 10 / 0;
print(x)

#
x = 10 / 3
print(type(x))

#
x = 10 / 2
print(type(x))

#
x = "Hello"
y = x
x = y.lower()
print(x)

#
x = 10 + 2
print(type(x))

#
x = 'Hi' + "Bye"
print(type(x))


#
list_1 = [1, 2, 3, 4]
for i, k in enumerate(list_1):
    if (i == 2):
        list_1.remove(k)
print(list_1)

#
x = "Hello"
y = "Hello"
print(x == y)

#
x = "Hello"
y = "Hello"
print(x is y)

#
x = ["Hello"]
y = ["Hello"]
print(x == y)

#
x = ["Hello"]
y = ["Hello"]
print(x is y)

#
x = 'something' is not None
print(x)

#
x = 'something' is (not None)
print(x)

#
x = -1
for x in range(7):
    if x == 6:
        print(x, ': for x inside loop')
print(x, ': x in global')

#
some_tuple = ("A", "BC", "def", "g")
some_tuple[2] = "xyz"
print(some_tuple)

#
a = 1
def some_func():
    return a
print(some_func())

#
a = 1
def some_func():
    a = a + 1
    return a
print(some_func())


#
def some_func():
    try:
        return 'from_try'
    finally:
        return 'from_finally'
print(some_func())

#
def some_func():
    try:
        raise Exception("Hello")
    finally:
        return 'Bye'
print(some_func())

#
def some_func():
    try:
        raise Exception("Hello")
    except:
        return "Hi"
    finally:
        return 'Bye'
print(some_func())


#
def some_func():
    try:
        raise Exception("Hello")
    except:
        return "Hi"
print(some_func())

#
def some_func():
    try:
        raise Exception("Hello")
    except KeyError:
        return "Hi"
print(some_func())

#
set1 = {1, 2, 3}
set2 = set1.add(4)
print(set2)

#
dictionary1 = {'GFG': 1,
               'Google': 2,
               'GFG': 3
               }
print(dictionary1['GFG']);

#
t = (1, 2, 3, 4)
t.append((5, 6, 7))
print(len(t))

#
tuple = (1, 2, 3)
print(2 * tuple)

#
x = ['ab', 'cd']
for i in x:
    i.upper()
print(x)

#
x = ['ab', 'cd']
for i in x:
    x.append(i.upper())
print(x)

#
data = [x for x in range(5)]
temp = [x for x in range(7) if x in data and x%2==0]
print(temp)


#
nameList = ['Harsh', 'Pratik', 'Bob', 'Dhruv']
print(nameList[1][-1])

#
dictionary = {1:'1', 2:'2', 3:'3'}
del dictionary[1]
dictionary[1] = '10'
del dictionary[2]
print (len(dictionary))