from enum import Enum


#Add the kingdom name (in capital letters) with the desired emblem value
class KingdomEnum(str, Enum):
    SPACE = "Gorilla"
    LAND = "Panda"
    WATER = "Octopus"
    ICE = "Mammoth"
    AIR = "Owl"
    FIRE = "Dragon"