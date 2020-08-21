def typeOfNum(num): # Function header
    # Function body
    if num % 2 == 0:
        def message():
            print("You entered an even number.")
    else:
        def message():
            print("You entered an odd number.")
    message()
# End of function
typeOfNum(2)  # call the function
typeOfNum(3)  # call the function again

#Polymorphism in Python

def product(x, y) : return x * y
print(product(4, 9)) # function returns 36
print(product('Python!', 2))  # function returns
                              # Python!Python!
#print(product('Python 2 or 3?', '3')) # TypeError occurs


#Immutable vs. Mutable

def test1(a, b) :
    a = 'Garbage' # 'a' receives an immutable object
    b[0] = 'Python' # 'b' receives a list object
                    # list is mutable
                    # it can undergo an in place change
def test2(a, b) :
    a = 'Garbage 2'
    b = 'Python 3' # 'b' now is made to refer to new
                   # object and therefore argument 'y'
                   # is not changed

arg1 = 10
arg2 = [1, 2, 3, 4]
test1(arg1, arg2)
print("After executing test 1 =>", arg1, arg2)
test2(arg1, arg2)
print("After executing test 2 =>", arg1, arg2)

#How to avoid changing the mutable argument
def test1(a, b):
    a = 'Garbage'
    b[0] = 'Python'


arg1 = 10
arg2 = [1, 2, 3, 4]

print("Before test 1 =>", arg1, arg2)
test1(arg1, arg2[:])  # Create an explicit copy of mutable object
# 'y' in the function.
# Now 'b' in test1() refers to a
# different object which was initially a
# copy of 'arg2'

print("After test 1  =>", arg1, arg2)


#Keyword-based arguments
def fn(value):
    print(value)
    return

fn(value=123) # output => 123
fn(value="Python!") # output => Python!


#Arguments with Default Values
def daysInYear(is_leap_year=False):
    if not is_leap_year:
        print("365 days")
    else:
        print("366 days")
    return

daysInYear()
daysInYear(True)


#Variable Arguments
def inventory(category, *items):
    print("%s [items=%d]:" % (category, len(items)), items)
    for item in items:
        print("-", item)
    return

inventory('Electronics', 'tv', 'lcd', 'ac', 'refrigerator', 'heater')
inventory('Books', 'python', 'java', 'c', 'c++')

#Global Variables in a Function
x = 5
y = 55
def fn() :
    global x
    x = [3, 7]
    y = [1, 33, 55]
    # a local 'y' is assigned and created here
    # whereas, 'x' refers to the global name
fn()
print(x, y)


#Name Resolution in a Python Function
'''
Here are a few points you should keep in mind.

The name assignments create or change local names.
The LEGB rule comes in the picture for searching the name reference.
local – L
then enclosing functions (if any) – E
next comes the global – G
and the last one is the built-in – B
'''

var = 5
def fn1() :
   var = [3, 5, 7, 9]
   def fn2() :
      var = (21, 31, 41)
      print(var)
   fn2()
fn1()	# uncomment var assignments one-by-one and check the output
print(var)

# Scope Lookup in Functions

X = 101 # global scope name - unused
def fn1():
   X = 102 # Enclosing def local
   def fn2():
      print(X) # Reference made in nested def
   fn2() # Prints 102: enclosing def local
fn1()

# Return Values from a Python Function

def returnDemo(val1, val2):
    val1 = 'Windows'
    val2 = 'OS X'
    return val1, val2  # return multiple values in a tuple


var1 = 4
var2 = [2, 4, 6, 8]

print("before return =>", var1, var2)
var1, var2 = returnDemo(var1, var2)
print("after return  =>", var1, var2)

# Recursive Function
def calcFact(num) :
    if(num != 1) :
        return num * calcFact(num-1)
    else :
        return 1

print(calcFact(4))


# Python Functions as Objects

# You can assign a function object to any other names.
def testFunc(a, b) : print('testFunc called %s %s' %(a,b))
fn = testFunc
fn(22, 'bb')
# You can even pass the function object to other functions.
def fn1(a, b) : print('testFunc called %s %s' %(a,b))
def fn2(fun, x, y) : fun(x, y)
fn2(fn1, 22, 'bb')


# You can return a function object from another function.
def FuncLair(produce) :
    def fn1() : print('fn1 called')
    def fn2() : print('fn2 called')
    def fn3() : print('fn3 called')
    if produce == 1 : return fn1
    elif produce == 2 : return fn2
    else : return fn3

f = FuncLair(2) ; f()

# Function Attributes

def testFunc():
    print("I'm just a test function.")

testFunc.attr1 = "Hello"
testFunc.attr2 = 5
testFunc()
print(dir(testFunc))

# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.

def myfunction():
  pass

# Arbitrary Arguments, *args

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")