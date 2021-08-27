import unittest
from src.Models.AfterNoonBufferTime import AfterNoonBufferTime


class TestQuery(unittest.TestCase):

    def test_morning_buffer_time(self):
        bufferTime = AfterNoonBufferTime()

        self.assertEqual(str(bufferTime.StartTime), "13:15")
        self.assertEqual(str(bufferTime.EndTime), "13:45")


if __name__ == '__main__':
    unittest.main()