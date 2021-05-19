class Event:
    def __init__(self, user_id, timestamp, type, data):
        self.user_id = user_id
        self.timestamp = timestamp
        self.type = type
        self.data = data
