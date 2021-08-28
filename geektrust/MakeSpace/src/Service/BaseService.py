from src.Models.Query import Query
from src.Models.MeetingRoom import MeetingRoom
from src.Models.Time import Time
from typing import List
import sys


class BaseService:
    def __init__(self) -> None:
        pass
    
    def __isMeetingTimeConflicting(self, startTime1: Time, endTime1: Time, startTime2: Time, endTime2: Time) -> bool:
        if startTime1 > startTime2 and startTime1 < endTime2 or endTime1 > startTime2 and endTime1 < endTime2:
            return True
        if startTime1 == startTime2:
            return True
        if endTime1 == endTime2:
            return True

        return False

    def __isBookingTimeInBuffers(self, meetingRoomBuffers, meetingStartTime: Time, meetingEndTime: Time) -> bool:
        for buffer in meetingRoomBuffers:
            if self.__isMeetingTimeConflicting(meetingStartTime, meetingEndTime, buffer.StartTime, buffer.EndTime):
                return True
        return False

    def __isRoomOccupied(self, meetingRoom: MeetingRoom, startTime: Time, endTime: Time) -> bool:
        for slotBooked in meetingRoom.SlotsBooked:
            slotStartTime = Time(slotBooked[0])
            slotEndTime = Time(slotBooked[1])
            if self.__isMeetingTimeConflicting(startTime, endTime, slotStartTime,slotEndTime):
                return True
        return False

    def GetVacantRoom(self, query: Query , meetingRooms : List[MeetingRoom]) -> MeetingRoom:
        vacantRoom = None
        minCapacity = sys.maxsize

        for meetingRoom in meetingRooms:
            roomOccupied = self.__isRoomOccupied(meetingRoom, query.StartTime, query.EndTime)          
            
            if not roomOccupied and not self.__isBookingTimeInBuffers(meetingRoom.Buffers, query.StartTime, query.EndTime):
                if meetingRoom.Capacity >= query.PersonCapacity and minCapacity > meetingRoom.Capacity:
                    vacantRoom = meetingRoom
                    minCapacity = meetingRoom.Capacity   

        return vacantRoom

    def GetVacantRooms(self, query: Query , meetingRooms : List[MeetingRoom]) -> List[MeetingRoom]:
        vacantRooms = []

        for meetingRoom in meetingRooms:
            roomOccupied = self.__isRoomOccupied(meetingRoom, query.StartTime, query.EndTime)

            if not roomOccupied and not self.__isBookingTimeInBuffers(meetingRoom.Buffers, query.StartTime, query.EndTime):
                vacantRooms.append(meetingRoom)

        return vacantRooms
