from src.Service.BaseService import BaseService
from src.Models.MeetingRoom import MeetingRoom
from src.Models.Query import Query
from typing import List


class BookingService(BaseService):
    def __init__(self) -> None:
        pass

    def BookRoom(self, query: Query , meetingRooms: List[MeetingRoom]) -> bool:
        self.Result = ''

        vacantRoom = self.GetVacantRoom(query, meetingRooms, query.PersonCapacity) 

        if not vacantRoom is None:
            self.Result = vacantRoom.Name
            vacantRoom.SlotsBooked.append([str(query.StartTime), str(query.EndTime)])
            return True
        else:
            return False