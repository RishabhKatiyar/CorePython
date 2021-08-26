from MeetingRoom import MeetingRoom
from ParseInput import ParseInput
from typing import List
from Time import Time
import sys


class Command:
    Result = ''
    def __init__(self) -> None:
        pass
    
    def IsBookingTimeInBuffers(self, _input:ParseInput, meetingRoom: MeetingRoom) -> bool:
        for buffer in meetingRoom.Buffers:
            if _input.StartTime > buffer.StartTime and _input.StartTime < buffer.EndTime or _input.EndTime > buffer.StartTime and _input.EndTime < buffer.EndTime:
                return True
            if _input.StartTime == buffer.EndTime:
                pass
            if _input.EndTime == buffer.StartTime:
                pass
            if _input.StartTime == buffer.StartTime:
                return True
            if _input.EndTime == buffer.EndTime:
                return True

        return False

    # Returns list of meeting rooms available at current time and the room with least capacity that can satisfy the need
    def GetVacantRooms(self, _input:ParseInput , meetingRooms : List[MeetingRoom], requiredCapacity = 0) -> List[MeetingRoom]:
        result = []
        VacantRoomWithLeastCapacity = None
        minCapacity = sys.maxsize
        for meetingRoom in meetingRooms:
            roomVacant = True
            for slotBooked in meetingRoom.SlotsBooked:
                slotStartTime = Time(slotBooked[0])
                slotEndTime = Time(slotBooked[1])
                if _input.StartTime > slotStartTime and _input.StartTime < slotEndTime or _input.EndTime > slotStartTime and _input.EndTime < slotEndTime:
                    roomVacant = False
                    break
                if _input.StartTime == slotEndTime:
                    pass
                if _input.EndTime == slotStartTime:
                    pass
                if _input.StartTime == slotStartTime:
                    roomVacant = False
                    break
                if _input.EndTime == slotEndTime:
                    roomVacant = False
                    break
            if roomVacant and not self.IsBookingTimeInBuffers(_input, meetingRoom):
                if requiredCapacity == 0:
                    result.append(meetingRoom)
                elif meetingRoom.Capacity >= requiredCapacity:
                    result.append(meetingRoom)
                    if minCapacity > meetingRoom.Capacity:
                        VacantRoomWithLeastCapacity = meetingRoom
                        minCapacity = meetingRoom.Capacity   

        return [result, VacantRoomWithLeastCapacity]


class Book(Command):
    def __init__(self) -> None:
        pass

    def BookRoom(self, _input:ParseInput , meetingRooms : List[MeetingRoom]) -> bool:
        self.Result = ''

        vacantRooms = self.GetVacantRooms(_input, meetingRooms, _input.PersonCapacity) 
        vacantRoom = vacantRooms[1]

        if not vacantRoom is None:
            self.Result = vacantRoom.Name
            vacantRoom.SlotsBooked.append([str(_input.StartTime), str(_input.EndTime)])
            return True
        else:
            return False


class Vacancy(Command):
    def __init__(self) -> None:
        pass

    def GetVacancy(self, _input:ParseInput , meetingRooms : List[MeetingRoom]) -> bool:
        self.Result = ''
        vacantRooms = self.GetVacantRooms(_input, meetingRooms)

        for vacantRoom in vacantRooms[0]:
            self.Result += vacantRoom.Name + " "
        
        return len(vacantRooms[0]) > 0