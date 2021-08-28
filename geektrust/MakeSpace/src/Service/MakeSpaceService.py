from src.Service.BookingService import BookingService
from src.Service.VacancyService import VacancyService
from src.Models.Query import Query
from src.Models.Commands import Commands
from src.Service.MeetingRoomFactory import MeetingRoomFactory


class MakeSpaceService:
    def __init__(self) -> None:
        self.BookingService = BookingService()
        self.VacancyService = VacancyService()

        self.MeetingRoomFactory = MeetingRoomFactory()
        self.MeetingRooms = self.MeetingRoomFactory.CreateMeetingRooms()

    def ExecuteRequest(self, query:Query) -> str:
        if query.Command == Commands.BOOK.name:
            response = self.BookingService.BookRoom(query, self.MeetingRooms)
        elif query.Command == Commands.VACANCY.name:
            response = self.VacancyService.GetVacancy(query, self.MeetingRooms)

        return response