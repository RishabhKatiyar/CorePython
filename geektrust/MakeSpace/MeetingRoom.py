from Time import Time
from collections import namedtuple


class BufferTime:
    StartTime = None
    EndTime = None
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return str(self.StartTime) + "-" + str(self.EndTime)

class MorningBufferTime(BufferTime):
    def __init__(self) -> None:
        # 09:00 - 09:15
        self.StartTime = Time("09:00")
        self.EndTime = Time("09:15")
        pass

class AfterNoonBufferTime(BufferTime):
    def __init__(self) -> None:
        # 13:15 - 13:45
        self.StartTime = Time("13:15")
        self.EndTime = Time("13:45")
        pass

class EveningBufferTime(BufferTime):
    def __init__(self) -> None:
        # 18:45 - 19:00
        self.StartTime = Time("18:45")
        self.EndTime = Time("19:00")
        pass

class MeetingRoom:
    def __init__(self, name, capacity, *args) -> None:
        self.Name = name
        self.Capacity = capacity
        self.Buffers = args[0]
        # SlotsBooked = [['StartTime', 'EndTime']]
        self.SlotsBooked = []
        pass

    def __str__(self) -> str:
        return self.Name