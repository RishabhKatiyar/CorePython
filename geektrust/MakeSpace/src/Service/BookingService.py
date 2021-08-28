from src.Service.BaseService import BaseService
from src.Models.MeetingRoom import MeetingRoom
from src.Models.Query import Query
from typing import List


class BookingService(BaseService):
    def __init__(self) -> None:
        pass

    def BookRoom(self, query: Query , meetingRooms: List[MeetingRoom]) -> str:
        vacantRoom = self.GetVacantRoom(query, meetingRooms) 

        if not vacantRoom is None:
            vacantRoom.SlotsBooked.append([str(query.StartTime), str(query.EndTime)])
            return vacantRoom.Name
        else:
            return "NO_VACANT_ROOM"