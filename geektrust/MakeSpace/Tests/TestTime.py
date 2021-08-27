import unittest
from src.Models.Time import Time


class TestTime(unittest.TestCase):

    def test_valid_time(self):
        time = Time("12:00")
        self.assertTrue(time.IsValid)

    def test_invalid_time(self):
        time = Time("25:00")
        self.assertFalse(time.IsValid)

    def test_str(self):
        time = Time("12:00")
        self.assertEqual(str(time), "12:0")

    def test_time_eq(self):
        time1 = Time("12:00")
        time2 = Time("12:00")
        self.assertTrue(time1 == time2)

    def test_time_greater_than_or_equal_to(self):
        time1 = Time("12:00")
        time2 = Time("13:00")
        self.assertTrue(time2 >= time1)
        
        time1 = Time("12:00")
        time2 = Time("12:00")
        self.assertTrue(time1 >= time2)

    def test_time_less_than_or_equal_to(self):
        time1 = Time("12:00")
        time2 = Time("13:00")
        self.assertTrue(time1 <= time2)
        
        time1 = Time("12:00")
        time2 = Time("12:00")
        self.assertTrue(time1 <= time2)

    def test_time_greater_than_(self):
        time1 = Time("12:00")
        time2 = Time("13:00")
        self.assertTrue(time2 > time1)

    def test_time_less_than_(self):
        time1 = Time("12:00")
        time2 = Time("13:00")
        self.assertTrue(time1 < time2)

    def test_invalid_hour(self):
        time = Time("-1:00")
        self.assertFalse(time.IsValid)
        self.assertEqual(time.Reason, "Hour should be between 0 and 23")

        time = Time("24:00")
        self.assertFalse(time.IsValid)
        self.assertEqual(time.Reason, "Hour should be between 0 and 23")

    def test_invalid_minutes(self):
        time = Time("12:-1")
        self.assertFalse(time.IsValid)
        self.assertEqual(time.Reason, "Minutes should be between 0 and 59")

        time = Time("12:60")
        self.assertFalse(time.IsValid)
        self.assertEqual(time.Reason, "Minutes should be between 0 and 59")

    def test_time_follow_interval_rule(self):
        time = Time("12:14")
        self.assertFalse(time.IsValid)
        self.assertEqual(time.Reason, "Minutes should follow the IntervalInMinutesRule")


if __name__ == '__main__':
    unittest.main()