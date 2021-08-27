from src.Models.Commands import Commands
from src.Validators.InputValidator import InputValidator
from src.Service.MeetingRoomFactory import MeetingRoomFactory
from src.Service.BookingService import BookingService
from src.Service.VacancyService import VacancyService
import sys 


def main():
    input_file = sys.argv[1]
    file = open(input_file, 'r')
    lines = file.readlines()
    
    meetingRoomFactory = MeetingRoomFactory()
    meetingRooms = meetingRoomFactory.CreateMeetingRooms()
    
    bookingService = BookingService()
    vacancyService = VacancyService()
    
    # These are the hard code representation of the various commands that can be 
    # extended when required
    commands = Commands()
    
    try:
        for line in lines:
            # Validate the incoming request
            _input = InputValidator(line)
            if _input.IsValid:
                # execute the request
                if _input.Query.Command == commands.COMMANDS[0][0]:
                    # if booking service returns true that means booking is made successfully
                    # and its result are available to us
                    if bookingService.BookRoom(_input.Query, meetingRooms):
                        print(bookingService.Result)
                    else:
                        print("NO_VACANT_ROOM")
                    
                elif _input.Query.Command == commands.COMMANDS[1][0]:
                    # if vacancy service returns true that means our query has some results to display
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
        
    except Exception:
        pass


if __name__ == "__main__":
    main()
    
