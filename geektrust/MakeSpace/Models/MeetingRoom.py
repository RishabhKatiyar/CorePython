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