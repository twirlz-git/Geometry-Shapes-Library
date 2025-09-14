# Geometry Shapes Library
A comprehensive Python library for calculating areas of geometric shapes with runtime polymorphism and extensibility.

## Features
✅ Circle area calculation based on radius using π * r²

✅ Triangle area calculation using Heron's formula based on three sides

✅ Right triangle detection for triangles using Pythagorean theorem

✅ Runtime polymorphism - calculate areas without knowing shape types at compile time

✅ Easy extensibility for adding new shapes

✅ Comprehensive error handling and input validation

✅ Full unit test coverage with 25+ test cases

✅ Production-ready code with proper documentation

## Installation
Simply copy the `geometry_shapes.py` file to your project directory.

## Quick Start

```python
from geometry_shapes import Circle, Triangle, ShapeCalculator

# Create shapes
circle = Circle(5)
triangle = Triangle(3, 4, 5)

# Create calculator for runtime polymorphism
calculator = ShapeCalculator()

# Calculate areas (works without knowing the shape type!)
circle_area = calculator.calculate_area(circle)
triangle_area = calculator.calculate_area(triangle)

print(f"Circle area: {circle_area:.4f}")
print(f"Triangle area: {triangle_area:.4f}")

# Check if triangle is right-angled
is_right = triangle.is_right_triangle()
print(f"Is right triangle: {is_right}")
```
