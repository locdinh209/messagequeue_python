import asyncio
from common.logger import _info_log, _debug_log, _error_log

# Example handler
async def Model(request_df):
    await asyncio.sleep(1)

    request_df['response_code'] = '00'
    request_df['predict_value'] = 'Y'