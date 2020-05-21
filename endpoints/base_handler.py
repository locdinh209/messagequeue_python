import asyncio
import time
from common.logger import _info_log, _debug_log, _error_log
from common.activemq_sender import StompSender

# Import models in here
from models import model_test

class BaseHandler():
    async def execute(request_id, model_id, request_df):
        try:
            _debug_log.debug(f"{request_id} - Begin handle message model_id = {model_id}")
            await model_test.Model(request_df)

        except BaseException as exp:
            _error_log.error(f'{request_id} - Execute model got error: {exp}')
            request_df['response_code'] = '05'

        finally:
            send_message = StompSender()
            send_message.send(request_id, request_df.to_json(orient='records')) 
        





