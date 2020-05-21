import asyncio
from endpoints.base_handler import BaseHandler
from aiostomp import AioStomp
import pandas as pd
import json
from common.logger import _info_log, _debug_log, _error_log

class StompConnection():
    async def create_connection():
        client = AioStomp('localhost', 61613, error_handler=StompListener.on_error)
        client.subscribe('/queue/MLRequest', handler=StompListener.on_message)
        await client.connect()
        _info_log.info(f"Subscribe message pool successful")

class StompListener():
    async def on_message(frame, message):
        try:
            request_json = json.loads(message.decode("utf-8"))
            request_df = pd.DataFrame([dict(request_json)])

            # Create request_id, model_id, body
            request_id = request_df['request_id'][0]
            model_id = request_df['model_id'][0]

        except BaseException as exp:
            _error_log.error(f'Request not have required fields: {exp}')

        else:
            await BaseHandler.execute(request_id, model_id, request_df)
            
        finally:
            return True

    async def on_error(error):
        _error_log.error(f'Receive error: {error}')


        


