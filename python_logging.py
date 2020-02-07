class CustomLogger():

    def __init__(self, log_level="WARNING"):
        self.log_level = log_level
    
    def start_logging(self, log_level, message):

        import datetime

        self.log_level = log_level
        self.message = message
        
        if self.log_level == None:
            return None
        else:
            dt = str(datetime.datetime.now()).replace(" ","T")
            _datetimeformat = f"[{dt}] : "
            print(_datetimeformat + self.log_level + " : " + message)
            return _datetimeformat + self.log_level + " : " + message

    def start_json_logging(self, log_level, message):

        import datetime, json

        self.log_level = log_level
        self.message = message

        if self.log_level == None:
            return None
        else:
            logs = {
                "Level" : log_level,
                "DateTime" : str(datetime.datetime.now()),
                "Message" : message
            }
            log_json = json.dumps(logs)
            print(log_json)
            return log_json

my_log = CustomLogger()
my_log.start_logging("INFO", "This is an information message!")
my_log.start_json_logging("INFO", "This is an information message!")
