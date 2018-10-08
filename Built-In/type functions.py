r = range(0, 30)
print(type(r))
print(type(10))
print(type("a"))
print(type("Hi there"))

class Car:
    pass

class Truck(Car):
    pass

c = Car()
t = Truck()
print(type(c))
print(type(t))
print(type(c) == type(t))

print(isinstance(c, Car))
print(isinstance(t, Car))
print(isinstance(t, Truck))
if isinstance(r, range):
    print(list(r))