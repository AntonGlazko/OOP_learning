# we want to create a class describing dogs
class Dog:
    breed = 'german shepherd'
    color = 'brown'
# When we create a class (Dog) we are simultaneously creating a class namespace
# Any variable described inside the class namespace is called a class atribute (breed and color)
# Each instance of the class (bob) has its own namespace. An instance of the class inherits the default class attributes

bob = Dog()

print(f"The bob's namespace contains: {bob.__dict__}") # The bob's namespace (an instance of the class Dog) is empty
print(f"The bob's namespace contains 'breed' attribute: {hasattr(bob, 'breed')}") # but it inherits class attribute

# we can set and change an attribute by directly accessing an instance of the class
# The attribute value will change only in the namespace of the instance, without affecting on the class namespace

bob.breed = 'pitbull'

print(f"The bob's namespace contains: {bob.__dict__}") # now bob's breed is pitbull and we can see it in the namespace
print(f"The Dog's namespace contains: {Dog.breed}") # and the class namespace has no changes

# we can set the class attribute from outside of the class code block using setattr()

setattr(Dog, 'size', 'big')
print(Dog.size)

class SomeClass:
    PROPERTY_1 = 0    # this args related with class
    PROPERTY_2 = 100
    # this method refers to the class directly
    @classmethod
    def check_valid(cls, arg):
        return cls.PROPERTY_1 <= arg <= cls.PROPERTY_2
    # (self) is a reference to an existing instance of the class that we created earlier
    # class invokes method __new__() before instance creating
    def __new__(cls, *args, **kwargs):
        print(f'The __new__ method is called')
        return super().__new__(cls)
    # When a class defines an __init__() method, class instantiation automatically
    # invokes __init__() for the newly created class instance
    def __init__(self, x, y):
        self.x = x
        self.y = y
        pass
    # __del__ is called when an object is garbage collected
    # which happens at some point after all references to the object have been deleted
    def __del__(self):
        pass
    # this method doesn't require references to the instance or class
    @staticmethod
    def do_something_staticly(x, y):
        return (x**x + y**y)
