def f1(x): return x ** 2


def f2(x): return lambda y: x + y


print(f1(2))

print(f2(2)(3))
