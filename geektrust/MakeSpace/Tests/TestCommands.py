import unittest
from src.Models.Commands import Commands


class TestQuery(unittest.TestCase):

    def test_commands_format(self):
        commands = Commands()

        for command in commands.COMMANDS:
            self.assertEqual(len(command), 2)
            self.assertTrue(type(command[0]) is str)
            self.assertTrue(type(command[1]) is int)


if __name__ == '__main__':
    unittest.main()