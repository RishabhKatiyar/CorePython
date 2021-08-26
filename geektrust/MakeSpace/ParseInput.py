from Time import Time


class ParseInput:
    # Constants
    COMMANDS = [("BOOK", 3), ("VACANCY", 2)]
    
    def __init__(self, input) -> None:
        self.Command = None
        self.StartTime = None
        self.EndTime = None
        self.PersonCapacity = 0
        self.Reason = None

        tokens = input.split(' ')

        for command in self.COMMANDS:
            if command[0] == tokens[0]:
                self.Command = command[0]
                self.StartTime = Time(tokens[1])
                self.EndTime = Time(tokens[2])
                if command[1] == 3:
                    self.PersonCapacity = int(tokens[3])
    
    @property
    def IsValid(self):
        if self.Command is None:
            self.Reason = "Not a registered Command"
            return False
        if not self.StartTime.IsValid:
            self.Reason = "StartTime is not valid"
            return False
        if not self.EndTime.IsValid:
            self.Reason = "EndTime is not valid"
            return False
        
        # Start Time should be less than End Time
        # Booking should be for the same day, the check for start time to be less than end should be able to handle this
        if self.StartTime.Hour > self.EndTime.Hour:
            self.Reason = "Start Time Hour greater than End Time Hour"
            return False
        elif self.StartTime.Hour == self.EndTime.Hour  and self.StartTime.Minutes > self.EndTime.Minutes:
            self.Reason = "Start Time Minutes greater than End Time Minutes"
            return False
        return True
