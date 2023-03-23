class CreateStatisticException(Exception):
    def __init__(self, message: str):
        self.message = message


class DeleteStatisticException(Exception):
    def __init__(self, message: str):
        self.message = message


class GetStatisticException(Exception):
    def __init__(self, message: str):
        self.message = message
