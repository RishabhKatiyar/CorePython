import unittest
from src.Validators.InputValidator import InputValidator


class TestInputValidator(unittest.TestCase):

    def test_valid_input(self):
        _input = InputValidator("BOOK 09:30 13:15 2")
        self.assertTrue(_input.IsValid)
        
    def test_invalid_command(self):
        _input = InputValidator("CANCEL 09:30 13:15 2")
        self.assertFalse(_input.IsValid)
        self.assertEqual(_input.Query.Reason, "Not a registered Command")

    def test_invalid_start_time(self):
        _input = InputValidator("BOOK 09:01 13:15 2")
        self.assertFalse(_input.IsValid)
        self.assertEqual(_input.Query.Reason, "StartTime is not valid")

    def test_invalid_end_time(self):
        _input = InputValidator("BOOK 09:30 13:16 2")
        self.assertFalse(_input.IsValid)
        self.assertEqual(_input.Query.Reason, "EndTime is not valid")

    def test_start_time_and_end_time_equal(self):
        _input = InputValidator("BOOK 09:30 09:30 2")
        self.assertFalse(_input.IsValid)
        self.assertEqual(_input.Query.Reason, "Start Time and End Time is same")

    def test_start_time_hour_greater_than_end_time_hour(self):
        _input = InputValidator("BOOK 10:30 09:30 2")
        self.assertFalse(_input.IsValid)
        self.assertEqual(_input.Query.Reason, "Start Time Hour greater than End Time Hour")

    def test_start_time_minutes_greater_than_end_time_minutes(self):
        _input = InputValidator("BOOK 10:30 10:15 2")
        self.assertFalse(_input.IsValid)
        self.assertEqual(_input.Query.Reason, "Start Time Minutes greater than End Time Minutes")
    
    def test_invalid_input(self):
        _input = InputValidator("BOOK 09:30 09:00 2")
        self.assertFalse(_input.IsValid)


if __name__ == '__main__':
    unittest.main()

