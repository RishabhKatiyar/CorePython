from src.Models.Kingdom import Kingdom
from src.Models.KingdomEnum import KingdomEnum


class InputValidator:    
    def __init__(self, input) -> None:
        kingdom = None
        tokens = input.strip().upper().split(' ')
        try:
            attributes = getattr(KingdomEnum, tokens[0])
            kingdom = Kingdom(attributes.name, attributes.value, " ".join(tokens[1:]))
        except AttributeError:
            pass
        
        self.Kingdom: Kingdom = kingdom
        
    @property
    def IsValid(self):
        if self.Kingdom is None:    
            return False
        return True
