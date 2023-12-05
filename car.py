class Car:
  pass
class Car:
    
    # initializer
    def __init__(self):
        pass
class Car:

    # initializer with instance attributes
    def __init__(self, color, style):
        self.color = color
        self.style = style
class Car:

    # class attribute
    wheels = 4

    # initializer with instance attributes
    def __init__(self, color, style):
        self.color = color
        self.style = style
class Car:

    # class attribute
    wheels = 4

    # initializer with instance attributes
    def __init__(self, color, style):
        self.color = color
        self.style = style

c = Car('Sedan', 'Black')
class Car:

    # class attribute
    wheels = 4

    # initializer with instance attributes
    def __init__(self, color, style):
        self.color = color
        self.style = style

c = Car('Black', 'Sedan')

# Access attributes
print(c.style)
# Prints Sedan
print(c.color)
# Prints Black

# Modify attribute
c.style = 'SUV'
print(c.style)
# Prints SUV
