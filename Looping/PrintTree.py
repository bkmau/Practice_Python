import unittest


class TreePrinter:
    def __init__(self, graphic):
        self._graphic = graphic

    def print_tree(self, height):
        if height == 0:
            return ""
        else:
            leafs = ""
            leaf = 1
            root = self._draw(" ", (height - 1)) + self._graphic
            while height > 0:
                leafs += self._draw(" ", (height - 1)) + self._draw(self._graphic, leaf) + "\n"
                height -= 1
                leaf += 2
            return leafs + root

    def _draw(self, graphic, times):
        result = ""
        for i in range(times):
            result += graphic
        return result


class TreePrinterTest(unittest.TestCase):
    def setUp(self):
        self.printer = TreePrinter()

    def test_print_with_height_equal_to_zero(self):
        self.assertEquals(self.printer.print_tree(0), "")

    def test_print_with_height_equal_to_one(self):
        self.assertEquals(self.printer.print_tree(1), "*\n*")

    def test_print_with_height_equal_to_two(self):
        self.assertEquals(self.printer.print_tree(2), " *\n***\n *")

    def test_print_with_height_equal_to_three(self):
        self.assertEquals(self.printer.print_tree(3), "  *\n ***\n*****\n  *")

    def test_print_with_height_equal_to_five(self):
        self.assertEquals(self.printer.print_tree(5), "    *\n   ***\n  *****\n *******\n*********\n    *")
