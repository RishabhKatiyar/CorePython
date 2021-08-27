import unittest
from src.Models.BufferTime import BufferTime


class TestQuery(unittest.TestCase):

    def test_buffer_time(self):
        bufferTime = BufferTime()
        bufferTime.StartTime = "12:00"
        bufferTime.EndTime = "13:00"

        self.assertEqual(str(bufferTime), "12:00-13:00")


if __name__ == '__main__':
    unittest.main()