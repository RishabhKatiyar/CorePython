# cat input.txt | python main.py
from ParseInput import ParseInput
from MeetingRoomFactory import MeetingRoomFactory
from Commands import Book, Vacancy


if __name__ == '__main__':
    meetingRoomFactory = MeetingRoomFactory()
    meetingRooms = meetingRoomFactory.CreateMeetingRooms()
    
    bookCommand = Book()
    vacancyCommand = Vacancy()

    try:
        while str:
            str = input()
            _input = ParseInput(str)
            if _input.IsValid:
                # execute the user request
                if _input.Command == "BOOK":
                    if bookCommand.BookRoom(_input, meetingRooms):
                        print(bookCommand.Result)
                    else:
                        print("NO_VACANT_ROOM")
                    
                elif _input.Command == "VACANCY":
                    if vacancyCommand.GetVacancy(_input, meetingRooms):
                        print(vacancyCommand.Result)
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

