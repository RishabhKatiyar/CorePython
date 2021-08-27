# cat input.txt | python main.py
from Models.Commands import Commands
from Validators.InputValidator import InputValidator
from Service.MeetingRoomFactory import MeetingRoomFactory
from Service.BookingService import BookingService
from Service.VacancyService import VacancyService


if __name__ == '__main__':
    meetingRoomFactory = MeetingRoomFactory()
    meetingRooms = meetingRoomFactory.CreateMeetingRooms()
    
    bookingService = BookingService()
    vacancyService = VacancyService()

    commands = Commands()

    try:
        while str:
            str = input()
            _input = InputValidator(str)
            if _input.IsValid:
                # execute the user request
                if _input.Query.Command == commands.COMMANDS[0][0]:
                    if bookingService.BookRoom(_input.Query, meetingRooms):
                        print(bookingService.Result)
                    else:
                        print("NO_VACANT_ROOM")
                    
                elif _input.Query.Command == commands.COMMANDS[1][0]:
                    if vacancyService.GetVacancy(_input.Query, meetingRooms):
                        print(vacancyService.Result)
                    else:
                        print("NO_VACANT_ROOM")
                else:
                    print("Fatal Error")
                    exit()
                pass
            else:
                print("INCORRECT_INPUT")
        
    except EOFError:
        pass

