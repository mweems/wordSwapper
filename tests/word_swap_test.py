import unittest


def swap_description(content, variable):
    return content


class TestVariableSwapping(unittest.TestCase):
    def test_should_replace_variable_with_content(self):
        content = "{variable} is blonde"
        self.assertEqual(swap_description(content, "blond"), "blond is blond")
