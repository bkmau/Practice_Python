import unittest


class TreePrinter:
    @staticmethod
    def print_tree(height):
        root = ""
        leafs = ""
        leaf_count = 1
        if height != 0:
            for space in range(height - 1):
                root += " "
            root += "*"
        while height > 0:
            for space in range(height - 1):
                leafs += " "
            for leaf in range(leaf_count):
                leafs += "*"
            leafs += "\n"
            height -= 1
            leaf_count += 2
        return leafs + root


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
