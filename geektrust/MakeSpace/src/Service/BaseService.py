from src.Models.Query import Query
from src.Models.MeetingRoom import MeetingRoom
from src.Models.Time import Time
from typing import List
import sys


class BaseService:
    def __init__(self) -> None:
        pass
    
    def IsMeetingTimeConflicting(self, startTime1: Time, endTime1: Time, startTime2: Time, endTime2: Time) -> bool:
        if startTime1 > startTime2 and startTime1 < endTime2 or endTime1 > startTime2 and endTime1 < endTime2:
            return True
        if startTime1 == startTime2:
            return True
        if endTime1 == endTime2:
            return True

        return False

    def IsBookingTimeInBuffers(self, meetingRoomBuffers, meetingStartTime: Time, meetingEndTime: Time) -> bool:
        for buffer in meetingRoomBuffers:
            if self.IsMeetingTimeConflicting(meetingStartTime, meetingEndTime, buffer.StartTime, buffer.EndTime):
                return True
        return False

    def IsRoomOccupied(self, meetingRoom: MeetingRoom, startTime: Time, endTime: Time) -> bool:
        for slotBooked in meetingRoom.SlotsBooked:
            slotStartTime = Time(slotBooked[0])
            slotEndTime = Time(slotBooked[1])
            if self.IsMeetingTimeConflicting(startTime, endTime, slotStartTime,slotEndTime):
                return True
        return False

    def GetVacantRoom(self, query: Query , meetingRooms : List[MeetingRoom], requiredCapacity: int) -> MeetingRoom:
        vacantRoom = None
        minCapacity = sys.maxsize

        for meetingRoom in meetingRooms:
            roomOccupied = self.IsRoomOccupied(meetingRoom, query.StartTime, query.EndTime)          
            
            if not roomOccupied and not self.IsBookingTimeInBuffers(meetingRoom.Buffers, query.StartTime, query.EndTime):
                if meetingRoom.Capacity >= requiredCapacity and minCapacity > meetingRoom.Capacity:
                    vacantRoom = meetingRoom
                    minCapacity = meetingRoom.Capacity   

        return vacantRoom

    def GetVacantRooms(self, query: Query , meetingRooms : List[MeetingRoom]) -> List[MeetingRoom]:
        vacantRooms = []

        for meetingRoom in meetingRooms:
            roomOccupied = self.IsRoomOccupied(meetingRoom, query.StartTime, query.EndTime)

            if not roomOccupied and not self.IsBookingTimeInBuffers(meetingRoom.Buffers, query.StartTime, query.EndTime):
                vacantRooms.append(meetingRoom)

        return vacantRooms
