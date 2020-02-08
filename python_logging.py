"""Custom Logger provides the flexibility of logging any python program
dynamically. This module can be used as it is by instantiating the
CustomLogger class.
"""


class CustomLogger():

    def __init__(self, log_level="WARNING"):
        self.log_level = log_level

    def start_logging(self, log_level, message):
        """Pass the logging level such as INFO, DEBUG
        and the message that have to be logged.
        All the progresses are printed in the console
        and can be divered to a log file.
        """
        import datetime

        self.log_level = log_level
        self.message = message

        if self.log_level == None:
            return None
        else:
            dt = str(datetime.datetime.now()).replace(" ", "T")
            _datetimeformat = f"[{dt}] : "
            print(_datetimeformat + self.log_level + " : " + message)
            return _datetimeformat + self.log_level + " : " + message

    def start_json_logging(self, log_level, message):
        """Pass the logging level such as INFO, DEBUG
        and the message that have to be logged.
        All the progresses are printed in the console
        and can be divered to a log file. The logging
        information are returned and printed in JSON
        format.
        """
        import datetime
        import json

        self.log_level = log_level
        self.message = message

        if self.log_level == None:
            return None
        else:
            logs = {
                "Level": log_level,
                "DateTime": str(datetime.datetime.now()).replace(" ", "T"),
                "Message": message
            }
            log_json = json.dumps(logs)
            print(log_json)
            return log_json


my_log = CustomLogger()
my_log.start_logging("INFO", "This is an information message!")
my_log.start_json_logging("INFO", "This is an information message!")
