from src.common.constants import CUSTOM_EXCEPTIONS


class CustomException(Exception):
    def __init__(self, message, name):
        super().__init__()
        self.message = message
        self.name = name


class NotAFileException(CustomException):
    def __init__(
        self,
        message: str = CUSTOM_EXCEPTIONS.MESSAGES.NOT_A_FILE_EXCEPTION
    ):
        super().__init__(message, CUSTOM_EXCEPTIONS.NAMES.NOT_A_FILE)
