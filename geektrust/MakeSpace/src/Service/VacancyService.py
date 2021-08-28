from src.Service.BaseService import BaseService
from src.Models.MeetingRoom import MeetingRoom
from src.Models.Query import Query
from typing import List


class VacancyService(BaseService):
    def __init__(self) -> None:
        pass

    def GetVacancy(self, query:Query , meetingRooms : List[MeetingRoom]) -> str:
        vacantRoomsList = ''
        
        vacantRooms = self.GetVacantRooms(query, meetingRooms)

        for vacantRoom in vacantRooms:
            vacantRoomsList += vacantRoom.Name + " "
                
        if len(vacantRooms) > 0:
            return vacantRoomsList.strip()
        else:
            return "NO_VACANT_ROOM"