from Models.Time import Time
from Models.BufferTime import BufferTime


class EveningBufferTime(BufferTime):
    def __init__(self) -> None:
        # 18:45 - 19:00
        self.StartTime = Time("18:45")
        self.EndTime = Time("19:00")
        pass