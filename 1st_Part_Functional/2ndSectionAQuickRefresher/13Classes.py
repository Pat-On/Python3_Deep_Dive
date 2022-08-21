class Rectangle:
    # first is new that create object and then __init__ step
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def get_width(self):
        return self._width

    def set_width(self, width):
        if width <= 0:
            raise ValueError("Width must be positive")
        else:
            self._width = width

    def get_height(self):
        return self._height

    def set_width(self, height):
        if height <= 0:
            raise ValueError("Width must be positive")
        else:
            self._height = height

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return 2 * (self._width + self._height)

    def to_string(self):
        return "Rectangle: width={0} Height: {1}".format(self._width, self._height)

    # overwriting built into the object methods (built into python)
    def __str__(self):
        return "Rectangle: width={0} Height: {1}".format(self._width, self._height)

    # different env so it does not work in my console like it
    def __repr__(self):
        print("got here?")
        return "Rectangle({0}, {1}".format(self._width, self._height)

    def __eq__(self, otherRect):
        # isinstance work with subclasses
        if isinstance(otherRect, Rectangle):
            return self._width == otherRect._width and self._height == otherRect._height
        else:
            return False

    def __lt__(self, otherRect):
        if isinstance(otherRect, Rectangle):
            return self.area() < otherRect.area()
        else:
            return NotImplemented


r1 = Rectangle(10, 20)
r2 = Rectangle(10, 20)
r3 = Rectangle(10, 200)
# python is passing r1 as a parameter
r1.area()

print(r1.to_string())

# __str__(self):
print(str(r1))

# __repr__(self):
print(r1)

# __eq__
print(r1 is not r2)
print(r1 == r2)
print(r1 == 100)

print(r1 < r3)


# MONKEY PATCHING - adding or changing properties in object
r1.width = 100
print(r1.width)
print(r1.get_height())

# ---------------------------------------------------------------------------------------------------------
# ------------------------------------------------ Pythonic way


class RectanglePythonic:
    # first is new that create object and then __init__ step
    def __init__(self, width, height):
        # reusing getters and setters to control initialization process for free nice!
        self.width = width
        self.height = height

    # overwriting built into the object methods (built into python)
    def __str__(self):
        return "Rectangle: width={0} Height: {1}".format(self.width, self.height)

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        else:
            self._width = value

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError("Width must be positive")
        else:
            self._height = height

    # different env so it does not work in my console like it

    def __repr__(self):
        print("got here?")
        return "Rectangle({0}, {1}".format(self.width, self.height)

    def __eq__(self, otherRect):
        # isinstance work with subclasses
        if isinstance(otherRect, Rectangle):
            return self.width == otherRect.width and self.height == otherRect.height
        else:
            return False


print("-" * 40)
r1 = RectanglePythonic(10, 20)
print(r1.width)
print(r1.height)
r1.width = 100000
print(r1.width)


r3 = RectanglePythonic(-100, 10)
