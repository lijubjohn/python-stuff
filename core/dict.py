thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

# iterate keys
for key in thisdict:
    print(key)

# iterate ket & value
for key, value in thisdict.items():
    print(key, value)

# Check if Key Exists

if "model" in thisdict:
    print("yes")

# dict length
print(len(thisdict))

# Accessing Items
print(thisdict["model"])
print(thisdict['model'])
print(thisdict.get("model"))

# Change Values
thisdict["year"] = 2018

# Adding Items
thisdict["color"] = "red"
print(thisdict)

# Removing Items
thisdict.pop("model")
print(thisdict)
# Remove last inserted item
thisdict.popitem()

# delete item with specific key
thisdict["model"] = "Mustang"
del thisdict["model"]
print(thisdict)

# delete dict
del thisdict

# empty dict
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.clear()
print(thisdict)

# Copy a Dictionary
mydict = thisdict.copy()
print(mydict)
print(id(mydict), id(thisdict))
# Copy alternative
mydict2 = dict(thisdict)

# The dict() Constructor
thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)
