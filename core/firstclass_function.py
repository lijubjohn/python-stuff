def f1(x): return x ** 2


def f2(x): return lambda y: x + y

x = f2

x = [f1, f2]
print(x[0](3))

# float , int ,str, list, dict, tuple, boolean,object

print(type(x))


print(f1(2))

f2(2)
print(f2(2)(3))
