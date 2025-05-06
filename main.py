from enum import Enum

class Status(Enum):
    DELIVERED = "Delivered"
    RECEIVED = "Received"
    ON_THE_WAY = "On the way"


class Package:
    def __init__(self, sender: str, recipient: str, weight: float, status: Status):
        self._sender = sender
        self._recipient = recipient
        self._weight = weight
        if status not in Status:
            raise ValueError("Status must be either 'Delivered' or 'Received' or 'On the way'")
        self._status = status
        self._delivered = self._status == Status.DELIVERED

    @property
    def delivered(self):
        return self._delivered

    @property
    def sender(self):
        return self._sender

    @sender.setter
    def sender(self, sender):
        self._sender = sender

    @property
    def recipient(self):
        return self._recipient

    @recipient.setter
    def recipient(self, recipient):
        self._recipient = recipient

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        self._weight = weight

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status
        self._delivered = self._status == Status.DELIVERED

    def __str__(self):
        return f"{self._sender} | {self._recipient} | {self._weight} Kg | {self._status}"

pack_1 = Package("Vasyl", "John", 23.45, Status.ON_THE_WAY)
pack_2 = Package("Piter", "John", 23.45, Status.RECEIVED)
pack_1.status = Status.DELIVERED
print(pack_1.delivered)
print(pack_2.delivered)

