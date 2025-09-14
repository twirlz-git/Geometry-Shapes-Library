import unittest
import math
from geometry_shapes import Shape, Circle, Triangle, Rectangle, ShapeCalculator


class TestCircle(unittest.TestCase):
    """Test cases for Circle class."""

    def test_circle_creation_valid(self):
        """Test valid circle creation."""
        circle = Circle(5.0)
        self.assertEqual(circle.radius, 5.0)

    def test_circle_creation_invalid(self):
        """Test invalid circle creation."""
        with self.assertRaises(ValueError):
            Circle(0)
        with self.assertRaises(ValueError):
            Circle(-1)

    def test_circle_area_calculation(self):
        """Test circle area calculation."""
        circle = Circle(1)
        self.assertAlmostEqual(circle.area(), math.pi, places=10)

        circle = Circle(2)
        self.assertAlmostEqual(circle.area(), 4 * math.pi, places=10)

        circle = Circle(0.5)
        self.assertAlmostEqual(circle.area(), 0.25 * math.pi, places=10)

    def test_circle_string_representation(self):
        """Test circle string representation."""
        circle = Circle(3.14)
        self.assertEqual(str(circle), "Circle(radius=3.14)")


class TestTriangle(unittest.TestCase):
    """Test cases for Triangle class."""

    def test_triangle_creation_valid(self):
        """Test valid triangle creation."""
        triangle = Triangle(3, 4, 5)
        self.assertEqual({triangle.side1, triangle.side2, triangle.side3}, {3, 4, 5})

    def test_triangle_creation_invalid_sides(self):
        """Test invalid triangle creation."""
        with self.assertRaises(ValueError):
            Triangle(0, 4, 5)
        with self.assertRaises(ValueError):
            Triangle(-1, 4, 5)

        with self.assertRaises(ValueError):
            Triangle(1, 1, 3)  # 1 + 1 <= 3
        with self.assertRaises(ValueError):
            Triangle(1, 10, 2)  # 1 + 2 <= 10

    def test_triangle_area_calculation(self):
        """Test triangle area calculation using Heron's formula."""
        # right triangle 3-4-5
        triangle = Triangle(3, 4, 5)
        expected_area = 6.0
        self.assertAlmostEqual(triangle.area(), expected_area, places=10)

        # equilateral triangle with side 2
        triangle = Triangle(2, 2, 2)
        expected_area = math.sqrt(3)
        self.assertAlmostEqual(triangle.area(), expected_area, places=10)

        # scalene triangle
        triangle = Triangle(5, 12, 13)
        expected_area = 30.0
        self.assertAlmostEqual(triangle.area(), expected_area, places=10)

    def test_right_triangle_detection(self):
        """Test right triangle detection."""
        # classic 3-4-5 right triangle
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_triangle())

        # 5-12-13 right triangle
        triangle = Triangle(5, 12, 13)
        self.assertTrue(triangle.is_right_triangle())

        # equilateral triangle (not right)
        triangle = Triangle(2, 2, 2)
        self.assertFalse(triangle.is_right_triangle())

        # random scalene triangle (not right)
        triangle = Triangle(2, 3, 4)
        self.assertFalse(triangle.is_right_triangle())

    def test_triangle_string_representation(self):
        """Test triangle string representation."""
        triangle = Triangle(3, 4, 5)
        self.assertEqual(str(triangle), "Triangle(sides=3, 4, 5)")


class TestShapeCalculator(unittest.TestCase):
    """Test cases for ShapeCalculator class."""

    def setUp(self):
        """Set up test fixtures."""
        self.circle = Circle(2)
        self.triangle = Triangle(3, 4, 5)
        self.calculator = ShapeCalculator()

    def test_calculate_area_single_shape(self):
        """Test area calculation for single shapes."""
        circle_area = self.calculator.calculate_area(self.circle)
        expected_circle_area = 4 * math.pi
        self.assertAlmostEqual(circle_area, expected_circle_area, places=10)

        triangle_area = self.calculator.calculate_area(self.triangle)
        expected_triangle_area = 6.0
        self.assertAlmostEqual(triangle_area, expected_triangle_area, places=10)

    def test_calculate_area_invalid_object(self):
        """Test area calculation with invalid objects."""
        with self.assertRaises(TypeError):
            self.calculator.calculate_area("not a shape")
        with self.assertRaises(TypeError):
            self.calculator.calculate_area(42)

    def test_calculate_total_area(self):
        """Test total area calculation for multiple shapes."""
        shapes = [self.circle, self.triangle, Circle(1), Triangle(1, 1, 1)]

        expected_total = (
                4 * math.pi +
                6.0 +
                math.pi +
                math.sqrt(3) / 4
        )

        total_area = self.calculator.calculate_total_area(shapes)
        self.assertAlmostEqual(total_area, expected_total, places=10)

    def test_get_shape_info_circle(self):
        """Test shape info retrieval for circle."""
        info = self.calculator.get_shape_info(self.circle)

        self.assertEqual(info['type'], 'Circle')
        self.assertAlmostEqual(info['area'], 4 * math.pi, places=10)
        self.assertEqual(info['description'], 'Circle(radius=2)')
        self.assertEqual(info['radius'], 2)
        self.assertAlmostEqual(info['circumference'], 4 * math.pi, places=10)

    def test_get_shape_info_triangle(self):
        """Test shape info retrieval for triangle."""
        info = self.calculator.get_shape_info(self.triangle)

        self.assertEqual(info['type'], 'Triangle')
        self.assertAlmostEqual(info['area'], 6.0, places=10)
        self.assertEqual(info['description'], 'Triangle(sides=3, 4, 5)')
        self.assertTrue(info['is_right_triangle'])


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class to demonstrate extensibility."""

    def test_rectangle_creation_and_area(self):
        """Test rectangle creation and area calculation."""
        rectangle = Rectangle(4, 5)
        self.assertEqual(rectangle.area(), 20.0)

    def test_rectangle_creation_invalid(self):
        """Test invalid rectangle creation."""
        with self.assertRaises(ValueError):
            Rectangle(0, 5)
        with self.assertRaises(ValueError):
            Rectangle(4, -1)

    def test_rectangle_with_calculator(self):
        """Test that new shapes work with existing calculator."""
        rectangle = Rectangle(3, 7)
        calculator = ShapeCalculator()

        area = calculator.calculate_area(rectangle)
        self.assertEqual(area, 21.0)

        shapes = [Circle(1), Triangle(3, 4, 5), rectangle]
        total_area = calculator.calculate_total_area(shapes)
        expected_total = math.pi + 6.0 + 21.0
        self.assertAlmostEqual(total_area, expected_total, places=10)

    def test_square_detection(self):
        """Test square detection functionality."""
        square = Rectangle(5, 5)
        rectangle = Rectangle(3, 7)

        self.assertTrue(square.is_square())
        self.assertFalse(rectangle.is_square())

    def test_rectangle_string_representation(self):
        """Test rectangle string representation."""
        rectangle = Rectangle(3, 4)
        self.assertEqual(str(rectangle), "Rectangle(width=3, height=4)")


class TestExtensibility(unittest.TestCase):
    """Test cases demonstrating library extensibility."""

    def test_mixed_shape_operations(self):
        """Test operations with mixed shape types."""
        shapes = [
            Circle(1),
            Triangle(3, 4, 5),
            Rectangle(2, 3),
            Circle(2),
            Triangle(5, 12, 13)
        ]

        calculator = ShapeCalculator()

        for shape in shapes:
            area = calculator.calculate_area(shape)
            self.assertGreater(area, 0)

        total_area = calculator.calculate_total_area(shapes)
        expected_total = (
                math.pi +
                6.0 +
                6.0 +
                4 * math.pi +
                30.0
        )
        self.assertAlmostEqual(total_area, expected_total, places=10)

    def test_shape_info_for_all_types(self):
        """Test shape info retrieval for all shape types."""
        shapes = [Circle(3), Triangle(3, 4, 5), Rectangle(4, 4)]
        calculator = ShapeCalculator()

        for shape in shapes:
            info = calculator.get_shape_info(shape)
            self.assertIn('type', info)
            self.assertIn('area', info)
            self.assertIn('description', info)
            self.assertGreater(info['area'], 0)


def run_all_tests():
    """Run all unit tests and display results."""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    test_classes = [
        TestCircle,
        TestTriangle,
        TestShapeCalculator,
        TestRectangle,
        TestExtensibility
    ]

    for test_class in test_classes:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")

    if result.wasSuccessful():
        print("100% test completed")
    else:
        print("some tests failed")

    return result


if __name__ == "__main__":
    run_all_tests()
