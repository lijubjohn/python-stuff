int_list = [1, 2, 3, 4, 5, 6]
sum = 0
for iter in int_list:
    sum += iter
print("Sum =", sum)
print("Avg =", sum / len(int_list))

# range
for iter in range(0, 3):
    print("iter: %d" % (iter))

books = ['C', 'C++', 'Java', 'Python']
for index in range(len(books)):
    print('Book (%d):' % index, books[index])

# break
birds = ['Belle', 'Coco', 'Juniper', 'Lilly', 'Snow']
ignoreElse = False
for theBird in birds:
    print(theBird)
    if ignoreElse and theBird is 'Snow':
        break
else:
    print("No birds left.")


# while with else
def while_else_demo():
    count = 0
    while count < 5 :
        num = int(input("Enter number between 0-100?"))
        if (num < 0) or (num > 100):
            print("Aborted while: You've entered an invalid number.")
            break
        count += 1
    else:
        print("While loop ended gracefully.")

while_else_demo()