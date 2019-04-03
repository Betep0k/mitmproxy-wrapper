import sys

sys.path.append('/usr/local/lib/python3.7/site-packages')

from mitmproxy import ctx
import time
from wrapper import Wrapper
import importlib
import os
import platform
import re

class PWN:
    def __init__(self):
        pass

    def request(self, flow):
        if "Wrapper" in flow.request.headers and flow.request.headers['Wrapper'] == '1':
            wrapper = Wrapper()
            result = wrapper.getData()
            # (token, sessid) = wrapper.getData()
            # flow.request.text = re.sub(r'_token=[a-zA-Z0-9]+', '_token=%s' % token, flow.request.text)
            # flow.request.cookies['roundcube_sessid'] = sessid
            del flow.request.headers['Wrapper']
            ctx.log.info('Wrapper No1 done!')


addons = [
    PWN()
]