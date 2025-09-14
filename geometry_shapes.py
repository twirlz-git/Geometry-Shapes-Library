import math
import abc
from typing import List, Union


class Shape(abc.ABC):
    """Abstract base class for all geometric shapes."""

    @abc.abstractmethod
    def area(self) -> float:
        """Calculate the area of the shape."""
        pass

    @abc.abstractmethod
    def __str__(self) -> str:
        """String representation of the shape."""
        pass


class Circle(Shape):
    """Circle shape implementation."""

    def __init__(self, radius: float):
        """Initialize a circle with given radius.

        Args:
            radius: The radius of the circle (must be positive)

        Raises:
            ValueError: If radius is not positive
        """
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    def area(self) -> float:
        """Calculate the area of the circle using π * r²."""
        return math.pi * self.radius ** 2

    def __str__(self) -> str:
        return f"Circle(radius={self.radius})"


class Triangle(Shape):
    """Triangle shape implementation using Heron's formula."""

    def __init__(self, side1: float, side2: float, side3: float):
        """Initialize a triangle with three sides.

        Args:
            side1, side2, side3: The three sides of the triangle (must be positive)

        Raises:
            ValueError: If sides don't form a valid triangle
        """
        if not all(side > 0 for side in [side1, side2, side3]):
            raise ValueError("All sides must be positive")

        if (side1 + side2 <= side3 or
                side2 + side3 <= side1 or
                side1 + side3 <= side2):
            raise ValueError("Sides don't form a valid triangle")

        self.sides = sorted([side1, side2, side3])
        self.side1, self.side2, self.side3 = side1, side2, side3

    def area(self) -> float:
        """Calculate the area using Heron's formula."""
        s = sum(self.sides) / 2
        return math.sqrt(s * (s - self.sides[0]) * (s - self.sides[1]) * (s - self.sides[2]))

    def is_right_triangle(self) -> bool:
        """Check if the triangle is a right triangle using Pythagorean theorem.

        Returns:
            True if triangle is right-angled, False otherwise
        """
        a, b, c = self.sides
        return abs(a ** 2 + b ** 2 - c ** 2) < 1e-10

    def __str__(self) -> str:
        return f"Triangle(sides={self.side1}, {self.side2}, {self.side3})"


class ShapeCalculator:
    """Calculator that can work with any shape without knowing its type at compile time."""

    @staticmethod
    def calculate_area(shape: Shape) -> float:
        """Calculate the area of any shape.

        Args:
            shape: Any object that implements the Shape interface

        Returns:
            The area of the shape

        Raises:
            TypeError: If the object is not a Shape
        """
        if not isinstance(shape, Shape):
            raise TypeError("Object must be a Shape")
        return shape.area()

    @staticmethod
    def calculate_total_area(shapes: List[Shape]) -> float:
        """Calculate the total area of multiple shapes.

        Args:
            shapes: List of Shape objects

        Returns:
            The sum of all shapes' areas
        """
        return sum(shape.area() for shape in shapes)

    @staticmethod
    def get_shape_info(shape: Shape) -> dict:
        """Get information about a shape including area and special properties.

        Args:
            shape: Any Shape object

        Returns:
            Dictionary with shape information
        """
        info = {
            'type': type(shape).__name__,
            'area': shape.area(),
            'description': str(shape)
        }

        if isinstance(shape, Triangle):
            info['is_right_triangle'] = shape.is_right_triangle()
        elif isinstance(shape, Circle):
            info['radius'] = shape.radius
            info['circumference'] = 2 * math.pi * shape.radius

        return info


class Rectangle(Shape):
    """Rectangle shape implementation to demonstrate extensibility."""

    def __init__(self, width: float, height: float):
        """Initialize a rectangle with width and height.

        Args:
            width: The width of the rectangle (must be positive)
            height: The height of the rectangle (must be positive)

        Raises:
            ValueError: If width or height is not positive
        """
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")
        self.width = width
        self.height = height

    def area(self) -> float:
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def is_square(self) -> bool:
        """Check if the rectangle is a square."""
        return abs(self.width - self.height) < 1e-10

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"


if __name__ == "__main__":
    # create shapes
    circle = Circle(5)
    triangle = Triangle(3, 4, 5)
    rectangle = Rectangle(4, 6)

    # create calculator
    calculator = ShapeCalculator()

    # calculate individual areas
    print(f"Circle area: {calculator.calculate_area(circle):.4f}")
    print(f"Triangle area: {calculator.calculate_area(triangle):.4f}")
    print(f"Rectangle area: {calculator.calculate_area(rectangle):.4f}")

    # check if triangle is right-angled
    print(f"Triangle is right-angled: {triangle.is_right_triangle()}")

    # ccalculate total area
    shapes = [circle, triangle, rectangle]
    total_area = calculator.calculate_total_area(shapes)
    print(f"Total area: {total_area:.4f}")

    # get detailed shape information
    for shape in shapes:
        info = calculator.get_shape_info(shape)
        print(f"\n{info['description']} - Area: {info['area']:.4f}")
