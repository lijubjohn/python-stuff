## list

l1 = []  # empty list
print l1
l2 = [1, 's', "dsd"]
print l2
l3 = list()  # empty list
print l3
l4 = [iter for iter in range(5)]
print l4
listofCountries = ["India", "America", "England", "Germany", "Brazil", "Vietnam"]
firstLetters = [country[0] for country in listofCountries]
print firstLetters

# Creating a multi-dimensional list
init_list = [0] * 3
print(init_list)
two_dim_list = [[0] * 3] * 3
print(two_dim_list)

# create a set of numbers
py_set_num = {3, 3, 7, 11, 15}
print(py_set_num)

# tuples

# create an empty tuple
py_tuple = ()
print("A blank tuple:", py_tuple)

# create a tuple without using round brackets
py_tuple = 33, 55, 77
print("A tuple set without parenthesis:", py_tuple, "type:", type(py_tuple))

# create a tuple of numbers
py_tuple = (33, 55, 77)
print("A tuple of numbers:", py_tuple)

# create a tuple of mixed numbers
# such as integer, float, imaginary
py_tuple = (33, 3.3, 3 + 3j)
print("A tuple of mixed numbers:", py_tuple)

# create a tuple of mixed data types
# such as numbers, strings, lists
py_tuple = (33, "33", [3, 3])
print("A tuple of mixed data types:", py_tuple)

# create a tuple of tuples
# i.e. a nested tuple
py_tuple = (('x', 'y', 'z'), ('X', 'Y', 'Z'))
print("A tuple of tuples:", py_tuple)

# creating a tuple from a set
py_tuple = tuple({33, 55, 77})
type(py_tuple)

py_tuple(33, 77, 55)
# creating a tuple from a list
py_tuple = tuple([33, 55, 77])
type(py_tuple)

py_tuple(33, 55, 77)
