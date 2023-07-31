import json


class Point(object):
    def __init__(self):
        self.measurement = ''
        self.fields = {}
        self.tags = {}
        self.timestamp = 0

class PointEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__
