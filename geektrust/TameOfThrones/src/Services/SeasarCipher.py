class SeasarCipher:
    def __init__(self, encryptedMessage: str, key: int) -> None:
        decryptedMessage = ""
        key %= 26
        encryptedMessage = encryptedMessage.upper()
        for ch in encryptedMessage:
            if ch == " ":
                decryptedMessage += " "
            else:
                decryptedMessage += chr(65 + ((ord(ch) - 65 - key) % 26))
        self.DecryptedMessage = decryptedMessage
