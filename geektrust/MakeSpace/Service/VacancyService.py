from Service.BaseService import BaseService
from Models.MeetingRoom import MeetingRoom
from Models.Query import Query
from typing import List


class VacancyService(BaseService):
    def __init__(self) -> None:
        pass

    def GetVacancy(self, query:Query , meetingRooms : List[MeetingRoom]) -> bool:
        self.Result = ''
        vacantRooms = self.GetVacantRooms(query, meetingRooms)

        for vacantRoom in vacantRooms[0]:
            self.Result += vacantRoom.Name + " "
        
        return len(vacantRooms[0]) > 0