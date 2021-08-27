from Models.Time import Time


class BufferTime:
    StartTime = None
    EndTime = None
    
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return str(self.StartTime) + "-" + str(self.EndTime)





