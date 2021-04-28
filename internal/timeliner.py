import os

import pendulum
import requests


class Timeliner:
    _client = "af"
    _app = "core"
    _base_url = os.environ["TIMELINER_URI"]

    def __init__(self, user: str, resource: str, resource_id: str, data_previous: dict, data_next: dict, **kwargs):
        scope = os.getenv("SCOPE", "production")

        self.data = {
            "timestamp": pendulum.now().isoformat(),
            "client": self._client,
            "app": self._app,
            "user": user,
            "resource": resource,
            "resource_id": resource_id,
            "previous": data_previous,
            "next": data_next,
            "tags": [f"scope:{scope}"] + kwargs.get("tags", []),
        }

    def send(self):
        resp = requests.post(f"{self._base_url}/", json=self.data)
        return resp
