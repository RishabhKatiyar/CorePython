from src.Services.SeasarCipher import SeasarCipher
from src.Models.Kingdom import Kingdom
from collections import Counter


class Ally:
    def __init__(self) -> None:
        pass
        
    @staticmethod
    def IsAlly(kingdom: Kingdom):
        plainTextMessage = SeasarCipher(kingdom.EncryptedMessage, len(kingdom.Emblem)).DecryptedMessage
        return Ally.IsEmblemInPlainText(Counter(kingdom.Emblem.upper()), Counter(plainTextMessage))

    @staticmethod
    def IsEmblemInPlainText(emblemCounter: dict, plainTextCounter: dict) -> bool:
        for key in emblemCounter:
            if key in plainTextCounter:
                if plainTextCounter[key] < emblemCounter[key]:
                    return False
            else:
                return False
        return True

