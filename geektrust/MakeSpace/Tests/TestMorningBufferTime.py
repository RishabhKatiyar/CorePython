import unittest
from src.Models.MorningBufferTime import MorningBufferTime


class TestQuery(unittest.TestCase):

    def test_morning_buffer_time(self):
        bufferTime = MorningBufferTime()

        self.assertEqual(str(bufferTime.StartTime), "9:0")
        self.assertEqual(str(bufferTime.EndTime), "9:15")


if __name__ == '__main__':
    unittest.main()