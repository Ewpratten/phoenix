from .APIRequest import makeRequest


class Device(object):
    """
    Wrapper class for Phoenix-compatible devices
    """

    type: str
    id: int

    def __init__(self, type: str, id: int) -> None:
        self.type = type
        self.id = id

    @staticmethod
    def getAllDevices() -> list:
        pass
