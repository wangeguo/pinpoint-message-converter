import json


class Point(object):
    def __init__(self):
        self.measurement = ''
        self.tags = {}
        self.fields = {}
        self.time = 0

class PointEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__
