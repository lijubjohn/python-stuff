# These iterables are handy because you can read them as much as you wish,
# but you store all the values in memory and this is not always what you want when you have a lot of values.

# Iterables
mylist = [x * x for x in range(3)]  # mylist is an iterable, Everything you can use "for... in..." on is an iterable; lists, strings, files...
for i in mylist:
    print(i)


# Generators
# Generators are iterators, a kind of iterable you can only iterate over once. Generators do not store all the values in memory, they generate the values on the fly:
# It is just the same except you used () instead of []. BUT, you cannot perform for i in mygenerator a second time since generators can only be used once: they calculate 0, then forget about it and calculate 1, and end calculating 4, one by one.
mygenerator = (x*x for x in range(3))
for i in mygenerator:
    print(i)

for i in mygenerator:
    print(i)