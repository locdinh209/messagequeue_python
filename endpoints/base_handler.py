import asyncio
import time
from common.logger import _info_log, _debug_log, _error_log
from common.activemq_sender import StompSender

class BaseHandler():
    async def start(df):
        await ModelTest(df)

# Example handler
async def ModelTest(df):
    _debug_log.debug(f"Begin handle message requestID={df['requestID'][0]}")
    await asyncio.sleep(1)
    _debug_log.debug(f"End handle message requestID={df['requestID'][0]} complete !")
    df['responseMessage'] = 'yes'
    response_message = StompSender()
    response_message.send(df.to_json(orient='records'))



