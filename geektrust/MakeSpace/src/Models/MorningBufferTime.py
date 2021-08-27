from src.Models.Time import Time
from src.Models.BufferTime import BufferTime


class MorningBufferTime(BufferTime):
    def __init__(self) -> None:
        # 09:00 - 09:15
        self.StartTime = Time("09:00")
        self.EndTime = Time("09:15")
        pass