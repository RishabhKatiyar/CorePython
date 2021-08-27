from typing import List
from Models.MorningBufferTime import MorningBufferTime
from Models.AfterNoonBufferTime import AfterNoonBufferTime
from Models.EveningBufferTime import EveningBufferTime
from Models.MeetingRoom import MeetingRoom


class MeetingRoomFactory:
    def __init__(self) -> None:
         pass

    def CreateMeetingRooms(self) -> List:
        meetingRooms = []
        # this data can be gathered from some api giving the office location/building number as one of the input parameter
        # format - Meeting Room, Capacity, BufferTimesType
        meetingRoomsData = [("C-Cave", 3, "Default"),("D-Tower", 7, "Default"),("G-Mansion", 20, "Default")]

        for meetingRoomData in meetingRoomsData:
            buffers = []

            if meetingRoomData[2] == "Default":
                buffers.append(MorningBufferTime())
                buffers.append(AfterNoonBufferTime())
                buffers.append(EveningBufferTime())

            meetingRooms.append(MeetingRoom(meetingRoomData[0], meetingRoomData[1], buffers))

        return meetingRooms