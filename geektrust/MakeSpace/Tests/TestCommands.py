import unittest
from src.Models.Commands import Commands


class TestQuery(unittest.TestCase):

    def test_commands_format(self):
        self.assertTrue(type(Commands.BOOK.name) is str)
        self.assertTrue(type(Commands.BOOK.value) is int)


if __name__ == '__main__':
    unittest.main()