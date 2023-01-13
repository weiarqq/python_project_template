import cat


class XxxService:
    def __init__(self):
        pass

    @cat.transaction("Service", "process")
    def process(self):
        pass