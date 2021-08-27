class Time:
    # offset is added to avoid false detection of overlap when meeting just start after one ends or vica versa
    def __init__(self, time_input) -> None:
        time = time_input.split(":")
        self.Hour = int(time[0])
        self.Minutes = int(time[1])
        self.IntervalsInMinutes = 15
        self.Reason = None
    
    def __str__(self) -> str:
        return str(self.Hour) + ":" + str(self.Minutes)
        
    def __eq__(self, other):
        selfVal = (self.Hour * 60) + self.Minutes
        otherVal = (other.Hour * 60) + other.Minutes
        return selfVal == otherVal 

    def __ge__(self, other):
        selfVal = (self.Hour * 60) + self.Minutes
        otherVal = (other.Hour * 60) + other.Minutes
        return selfVal >= otherVal 

    def __le__(self, other):
        selfVal = (self.Hour * 60) + self.Minutes
        otherVal = (other.Hour * 60) + other.Minutes
        return selfVal <= otherVal 
        
    def __gt__(self, other):
        selfVal = (self.Hour * 60) + self.Minutes
        otherVal = (other.Hour * 60) + other.Minutes
        return selfVal > otherVal 

    def __lt__(self, other):
        selfVal = (self.Hour * 60) + self.Minutes
        otherVal = (other.Hour * 60) + other.Minutes
        return selfVal < otherVal 

    @property
    def IsValid(self):
        # Basic checks on our Time object i.e hour,  
        # minutes and interval (that can be easily changed with self.IntervalsInMinutes)
        if self.Hour < 0 or self.Hour > 23:
            self.Reason = "Hour should be between 0 and 23"
            return False
        
        if self.Minutes < 0 or self.Minutes > 59:
            self.Reason = "Minutes should be between 0 and 59"
            return False
        
        if self.Minutes % self.IntervalsInMinutes != 0:
            self.Reason = "Minutes should follow the IntervalInMinutesRule"
            return False
        
        return True