# days = int(input("How many days in a leap year? "))
# if days == 366:
#     print("Congrats!You have cleared the test.")
# else:
#     print("please read and level up")


# If Else in one line - Syntax
num = 2
result = 'Even' if num % 2 == 0 else 'Odd'
print(result)

# Python if-Elif-Else Statement
'''
while True:
    response = input("Which Python data type is an ordered sequence? ").lower()
    print("You entered:", response)

    if response == "list":
        print("You have cleared the test.")
        break
    elif response == "tuple":
        print("You have cleared the test.")
        break
    else:
        print("Your input is wrong. Please try again.")
'''
a = 10
b = 20
if not a > b:
    print("The number %d is less than %d" % (a, b))

X = 0
if not X:
    print("X is not %d" % (X))
else:
    print("X is %d" % (X))

a = 10
b = 20
c = 30
avg = (a + b + c) / 3
print("avg =", avg)
if avg > a and avg > b and avg > c:
    print("%d is higher than %d, %d, %d" % (avg, a, b, c))
elif avg > a and avg > b:
    print("%d is higher than %d, %d" % (avg, a, b))
elif avg > a and avg > c:
    print("%d is higher than %d, %d" % (avg, a, c))
elif avg > b and avg > c:
    print("%d is higher than %d, %d" % (avg, b, c))
elif avg > a:
    print("%d is just higher than %d" % (avg, a))
elif avg > b:
    print("%d is just higher than %d" % (avg, b))
elif avg > c:
    print("%d is just higher than %d" % (avg, c))

# Example of "in" operator with Python If statement

num_list = [1, 10, 2, 20, 3, 30]
for num in num_list:
    if not num in (2, 3):
        print("Allowed Item:", num)

# Find players who play both games
team1 = ["Jake", "Allan", "Nick", "Alex", "Dave"]
team2 = ["David", "John", "Chris", "Alex", "Nick"]
for aplayer in team1:
    if aplayer in team2:
        print("%s also plays for team2." % (aplayer))


#Implement Python Switch Case Statement
def monday():
    return "monday"
def tuesday():
    return "tuesday"
def wednesday():
    return "wednesday"
def thursday():
    return "thursday"
def friday():
    return "friday"
def saturday():
    return "saturday"
def sunday():
    return "sunday"
def default():
    return "Incorrect day"

switcher = {
    1: monday,
    2: tuesday,
    3: wednesday,
    4: thursday,
    5: friday,
    6: saturday,
    7: sunday
    }

def switch(dayOfWeek):
    return switcher.get(dayOfWeek, default)()

print(switch(1))
print(switch(0))


# Implement Python Switch Case Statement using Class
class PythonSwitch:

    def switch(self, dayOfWeek):
        default = "Incorrect day"
        return getattr(self, 'case_' + str(dayOfWeek), lambda: default)()

    def case_1(self):
        return "Monday"

    def case_2(self):
        return "Tuesday"

    def case_3(self):
        return "Wednesday"


s = PythonSwitch()

print(s.switch(1))
print(s.switch(0))