#Document in : http://jasonrbriggs.github.io/stomp.py/quickstart.html#installation

import sys
import stomp
import json
import uuid
import time
import numpy as np


class MyListener(stomp.ConnectionListener):

    def on_error(self, headers, message):
        print('received an error "%s"' % message)

    def on_message(self, headers, message):
        print('received a message "%s"' % message)


conn = stomp.Connection12()
conn.set_listener('', MyListener())
conn.connect('admin', 'password', wait=True)

import json

# some JSON:
# Send 10 queue
for i in np.arange(1,11):
    x =  { 'name':'John', 'age':30, 'city':'New York'}
    x['requestID'] = int(i)
    # requestID={'requestID': int(i)}  # Convert the id to a regular int
    # x.append(requestID)
    body_json = json.dumps(x)
    conn.send(destination='/queue/MLRequest',body=body_json,content_type=json)

conn.disconnect()
 