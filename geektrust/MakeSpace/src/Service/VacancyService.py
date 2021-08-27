from src.Service.BaseService import BaseService
from src.Models.MeetingRoom import MeetingRoom
from src.Models.Query import Query
from typing import List


class VacancyService(BaseService):
    def __init__(self) -> None:
        pass

    def GetVacancy(self, query:Query , meetingRooms : List[MeetingRoom]) -> bool:
        self.Result = ''
        
        vacantRooms = self.GetVacantRooms(query, meetingRooms)

        for vacantRoom in vacantRooms:
            self.Result += vacantRoom.Name + " "
        
        self.Result = self.Result.strip()
        
        return len(vacantRooms) > 0