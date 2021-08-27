from src.Models.Query import Query
from src.Models.MeetingRoom import MeetingRoom
from src.Models.Time import Time
from typing import List
import sys


class BaseService:
    Result = ''
    def __init__(self) -> None:
        pass
    
    def IsBookingTimeInBuffers(self, query:Query, meetingRoom: MeetingRoom) -> bool:
        for buffer in meetingRoom.Buffers:
            if query.StartTime > buffer.StartTime and query.StartTime < buffer.EndTime or query.EndTime > buffer.StartTime and query.EndTime < buffer.EndTime:
                return True
            if query.StartTime == buffer.EndTime:
                pass
            if query.EndTime == buffer.StartTime:
                pass
            if query.StartTime == buffer.StartTime:
                return True
            if query.EndTime == buffer.EndTime:
                return True

        return False

    # Returns list of meeting rooms available at current time and the room with least capacity that can satisfy the need
    def GetVacantRooms(self, query: Query , meetingRooms : List[MeetingRoom], requiredCapacity = 0) -> List:
        result = []
        VacantRoomWithLeastCapacity = None
        minCapacity = sys.maxsize

        for meetingRoom in meetingRooms:
            roomVacant = True
            for slotBooked in meetingRoom.SlotsBooked:
                slotStartTime = Time(slotBooked[0])
                slotEndTime = Time(slotBooked[1])
                if query.StartTime > slotStartTime and query.StartTime < slotEndTime or query.EndTime > slotStartTime and query.EndTime < slotEndTime:
                    roomVacant = False
                    break
                if query.StartTime == slotEndTime:
                    pass
                if query.EndTime == slotStartTime:
                    pass
                if query.StartTime == slotStartTime:
                    roomVacant = False
                    break
                if query.EndTime == slotEndTime:
                    roomVacant = False
                    break
            if roomVacant and not self.IsBookingTimeInBuffers(query, meetingRoom):
                if requiredCapacity == 0:
                    result.append(meetingRoom)
                elif meetingRoom.Capacity >= requiredCapacity:
                    result.append(meetingRoom)
                    if minCapacity > meetingRoom.Capacity:
                        VacantRoomWithLeastCapacity = meetingRoom
                        minCapacity = meetingRoom.Capacity   

        return [result, VacantRoomWithLeastCapacity]
