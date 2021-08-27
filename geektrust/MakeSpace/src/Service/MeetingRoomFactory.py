from typing import List
from src.Models.MorningBufferTime import MorningBufferTime
from src.Models.AfterNoonBufferTime import AfterNoonBufferTime
from src.Models.EveningBufferTime import EveningBufferTime
from src.Models.MeetingRoom import MeetingRoom
from src.Controllers.MeetingRoomsController import MeetingRoomsController


class MeetingRoomFactory:
    def __init__(self) -> None:
         pass

    def CreateMeetingRooms(self) -> List:
        meetingRooms = []
        
        meetingRoomsData = MeetingRoomsController().GetMeetingRoomData()

        for meetingRoomData in meetingRoomsData:
            buffers = []

            if meetingRoomData[2] == "Default":
                buffers.append(MorningBufferTime())
                buffers.append(AfterNoonBufferTime())
                buffers.append(EveningBufferTime())

            meetingRooms.append(MeetingRoom(meetingRoomData[0], meetingRoomData[1], buffers))

        return meetingRooms