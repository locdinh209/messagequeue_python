import asyncio
from endpoints.base_handler import BaseHandler
from aiostomp import AioStomp
import pandas as pd
import json
from common.logger import _info_log, _debug_log, _error_log
from common.singleton import singleton

class StompConnection():
    async def create_connection():
        client = AioStomp('localhost', 61613, error_handler=StompListener.on_error)
        client.subscribe('/queue/MLRequest', handler=StompListener.on_message)
        await client.connect()
        _info_log.info(f"Subscribe message pool successful")

class StompListener():
    async def on_message(frame, message):
        request_json = json.loads(message.decode("utf-8"))
        request_df = pd.DataFrame([dict(request_json)])
        _debug_log.debug(f"Receive message with requestID: {request_df['requestID'][0]}")
        await BaseHandler.start(request_df)
        return True

    async def on_error(error):
        _error_log.error(f'Receive error: {error}')

@singleton
class StompSender():
    pass
    async def __init__(self):
        self.client = AioStomp('localhost', 61613, error_handler=StompListener.on_error)
        await self.client.connect()
        _info_log.info('Create connection for sending successful')

    def send(self, body, headers=None):
        self.client.send('/queue/MLResponse', body, headers)
        _debug_log.debug('Send message success')
        


