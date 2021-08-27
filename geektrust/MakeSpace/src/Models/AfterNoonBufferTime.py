from src.Models.Time import Time
from src.Models.BufferTime import BufferTime


class AfterNoonBufferTime(BufferTime):
    def __init__(self) -> None:
        # 13:15 - 13:45
        self.StartTime = Time("13:15")
        self.EndTime = Time("13:45")
        pass