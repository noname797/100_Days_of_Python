# Argurments with default values

def my_func(a=1,b=2,c=3):
    # func 1
    # func 2
    pass

my_func(b=5)

def foo(a, b=4, c=6):
    print(a, b, c)

foo(4, 9)  # Output = 4 9 6



# Unlimited arguments


def add(n1,n2):
    return n1+n2

def add(*args):
    for n in args:  # args are in form of tuple
        print(n)

## Unlimited arbitraty key word arguements

def calculate(n, **kwargs): # kwards are in the form of dictionary
    for key, value in kwargs.items():
        print(key, value)

    print(kwargs['add'])

    n +=kwargs['add']
    n *= kwargs['multiply']


class Car:
    def __init__(self,**kwargs):
        self.make = kwargs.get('make') # similar to kwargs['make'] but ouptuts 'None' if there's no value present
        self.model = kwargs.get('model')
        self.colour = kwargs.get('colour')
        self.seats = kwargs.get('seats')


my_car = Car(make='Nissan', model='Skyline')



def all_aboard(a, *args, **kw):
    print(a, args, kw)

all_aboard(4, 7, 3, 0, x=10, y=64)

# output 4 (7, 3, 0) {'x': 10, 'y': 64}
