import unittest
from src.Models.MeetingRoom import MeetingRoom
from src.Models.MorningBufferTime import MorningBufferTime


class TestQuery(unittest.TestCase):

    def test_commands_format(self):
        buffers = []    
        buffers.append(MorningBufferTime())
        meetingRoom = MeetingRoom("C Cave", 5, buffers)

        self.assertEqual(meetingRoom.Name, "C Cave")
        self.assertEqual(meetingRoom.Capacity, 5)
        self.assertEqual(meetingRoom.Buffers, buffers)

        self.assertEqual(str(meetingRoom), "C Cave")
        
        
if __name__ == '__main__':
    unittest.main()