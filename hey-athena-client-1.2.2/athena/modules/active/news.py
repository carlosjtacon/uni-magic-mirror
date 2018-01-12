"""
    Finds and returns the latest bitcoin price

    Usage Examples:
        - "What is the price of bitcoin?"
        - "How much is a bitcoin worth?"
"""

from athena.classes.module import Module
from athena.classes.task import ActiveTask

import requests
import json


class GetValueTask(ActiveTask):

    def __init__(self):
        super().__init__(words=['news'])

    def action(self, text):
        payload = {'status': 5}
        requests.post("http://localhost:8000/athena", json=json.dumps(payload))
        self.speak("There are some important anouncements about catalonia")


class News(Module):

    def __init__(self):
        tasks = [GetValueTask()]
        super().__init__('news', tasks, priority=2)
