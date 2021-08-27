import unittest
from src.Models.EveningBufferTime import EveningBufferTime


class TestQuery(unittest.TestCase):

    def test_morning_buffer_time(self):
        bufferTime = EveningBufferTime()

        self.assertEqual(str(bufferTime.StartTime), "18:45")
        self.assertEqual(str(bufferTime.EndTime), "19:0")


if __name__ == '__main__':
    unittest.main()