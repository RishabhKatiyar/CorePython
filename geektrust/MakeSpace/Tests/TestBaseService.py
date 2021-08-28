import unittest
from src.Service.BaseService import BaseService
from src.Models.Query import Query
from src.Models.Commands import Commands
from src.Models.MeetingRoom import MeetingRoom


class TestBaseService(unittest.TestCase):
    def setUp(self) -> None:
        self.baseService = BaseService()
        self.meetingRooms = []
        meetingRoomsData = [("C-Cave", 3, "Default"),("D-Tower", 7, "Default"),("G-Mansion", 20, "Default")]
        for meetingRoomData in meetingRoomsData:
            self.meetingRooms.append(MeetingRoom(meetingRoomData[0], meetingRoomData[1], []))

    def test_GetVacantRoom(self):
        query = Query()
        query.Command = Commands.BOOK.name
        query.StartTime = "09:30"
        query.EndTime = "10:30"
        query.PersonCapacity = 2
        
        response: MeetingRoom = self.baseService.GetVacantRoom(query, self.meetingRooms)
        self.assertEqual(response.Name, "C-Cave")

    def test_GetVacantRooms(self):
        query = Query()
        query.Command = Commands.VACANCY.name
        query.StartTime = "09:30"
        query.EndTime = "10:30"
        
        response: MeetingRoom = self.baseService.GetVacantRooms(query, self.meetingRooms)
        self.assertEqual(len(response), 3)

 
if __name__ == '__main__':
    unittest.main()