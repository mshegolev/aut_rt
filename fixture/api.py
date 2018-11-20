import requests
from nose.tools import assert_true


class Api:
    def __init__(self, app):
        self.app = app
        self.url = app.base_url + app.v1
        self.session = requests.Session()

    def login(self, creds):
        url = self.url + "/auth/login/"
        data = {"login": creds.username, "password": creds.password}
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=url, json=data, headers=headers, verify=False)
        return r
