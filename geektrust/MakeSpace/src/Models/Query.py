from src.Models.Time import Time


class Query:
    Command: str = None
    StartTime: Time  = None
    EndTime: Time = None
    PersonCapacity: int = 0
    Reason: str = None