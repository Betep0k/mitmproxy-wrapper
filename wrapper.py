#!/usr/bin/python3
import requests
import os
import re

class Wrapper:
    def __init__(self):
        self.s = requests.Session()
        self.token = None
        self.sessid = None

    def getData(self):
        result = ''
        return result
        # response = self.s.get('http://192.168.1.1:8080/')
        # m = re.search('\"request_token\":\"([0-9a-zA-Z]+)\"', response.text)
        # self.token = m.group(1)
        # self.sessid = response.cookies['roundcube_sessid']
        # return (self.token, self.sessid)