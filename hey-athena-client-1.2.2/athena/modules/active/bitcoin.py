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
        super().__init__(words=['bitcoin'])

    def action(self, text):
        payload = {'status': 6}
        requests.post("http://localhost:8000/athena", json=json.dumps(payload))
        self.speak("This is the bitcoin chart")


class Bitcoin(Module):
    
    def __init__(self):
        tasks = [GetValueTask()]
        super().__init__('bitcoin', tasks, priority=2)
