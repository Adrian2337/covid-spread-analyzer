from sys import stderr
from datetime import datetime


class LogService:

    @staticmethod
    def log(calling_class, message, error=False):
        if not error:
            print(datetime.now(), " ", calling_class.__name__, ": ", message, sep="")
        else:
            LogService.__print_error(datetime.now(), " ", calling_class.__name__, ": ", message, sep="")

    @staticmethod
    def __print_error(*args, **kwargs):
        print(*args, file=stderr, **kwargs)
