import json
from typing import Dict

class DDSpan(object):
    trace_id: int = 0
    span_id: int = 0
    parent_id: int = 0
    service: str = ''
    name: str = ''
    resource: str = ''
    start: int = 0
    duration: int = 0
    meta: Dict[str, str] = {}
    type: int = ''

class DDSpanEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__
