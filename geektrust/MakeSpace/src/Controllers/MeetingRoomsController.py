from typing import List


class MeetingRoomsController:
    def __init__(self) -> None:
        pass

    def GetMeetingRoomData(self, FloorNumber = "Default", BuildingName = "Default") -> List:
        if FloorNumber == "Default" and BuildingName == "Default":
            return [("C-Cave", 3, "Default"),("D-Tower", 7, "Default"),("G-Mansion", 20, "Default")]