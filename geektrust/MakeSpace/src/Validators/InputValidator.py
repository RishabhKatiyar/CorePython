from src.Models.Time import Time
from src.Models.Query import Query
from src.Models.Commands import Commands

class InputValidator:    
    def __init__(self, input) -> None:
        # build a query object out of the user request
        self.Query = Query()

        tokens = input.split(' ')

        for command in Commands().COMMANDS:
            if command[0] == tokens[0]:
                self.Query.Command = command[0]
                self.Query.StartTime = Time(tokens[1])
                self.Query.EndTime = Time(tokens[2])
                if command[1] == 3:
                    self.Query.PersonCapacity = int(tokens[3])
    
    @property
    def IsValid(self):
        # basic checks on the input
        if self.Query.Command is None:
            self.Query.Reason = "Not a registered Command"
            return False

        if not self.Query.StartTime.IsValid:
            self.Query.Reason = "StartTime is not valid"
            return False
            
        if not self.Query.EndTime.IsValid:
            self.Query.Reason = "EndTime is not valid"
            return False

        # Start Time should not be equal to end time  
        if self.Query.StartTime == self.Query.EndTime:
            self.Query.Reason = "Start Time and End Time is same"
            return False
        
        # Start Time should be less than End Time
        # Booking should be for the same day, 
        # the check for start time to be less than end should be able to handle this
        if self.Query.StartTime.Hour > self.Query.EndTime.Hour:
            self.Query.Reason = "Start Time Hour greater than End Time Hour"
            return False
        elif self.Query.StartTime.Hour == self.Query.EndTime.Hour  and self.Query.StartTime.Minutes > self.Query.EndTime.Minutes:
            self.Query.Reason = "Start Time Minutes greater than End Time Minutes"
            return False
        return True
