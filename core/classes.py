# __init__ (constructor)
class BookStore:
    def __init__(self):
        print("__init__() constructor gets called...")

B1 = BookStore()

# The instance attributes
class BookStore:
    instances = 0
    def __init__(self, attrib1, attrib2):
        self.attrib1 = attrib1
        self.attrib2 = attrib2
        BookStore.instances += 1

b1 = BookStore("", "")
b2 = BookStore("", "")

print("BookStore.instances:", BookStore.instances)