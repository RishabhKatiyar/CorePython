from Service.BaseService import BaseService
from Models.MeetingRoom import MeetingRoom
from Models.Query import Query
from typing import List


class BookingService(BaseService):
    def __init__(self) -> None:
        pass

    def BookRoom(self, query: Query , meetingRooms: List[MeetingRoom]) -> bool:
        self.Result = ''

        vacantRooms = self.GetVacantRooms(query, meetingRooms, query.PersonCapacity) 
        vacantRoom = vacantRooms[1]

        if not vacantRoom is None:
            self.Result = vacantRoom.Name
            vacantRoom.SlotsBooked.append([str(query.StartTime), str(query.EndTime)])
            return True
        else:
            return False