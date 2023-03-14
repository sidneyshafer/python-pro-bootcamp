# Many Keyword Arguments **

def calc(n, **kwargs):
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calc(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        # Use 'get()' so it will not return an error if an arg is not passed
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.year = kw.get("year")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
print(my_car.make)

