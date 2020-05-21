from common.singleton import singleton
from common.logger import _info_log, _debug_log, _error_log
import stomp

@singleton
class StompSender():
    pass
    def __init__(self):
        # Init connection send to message queue one time
        self.conn = stomp.Connection12()
        self.conn.connect('admin', 'password', wait=True)
        _info_log.info('Create connection for sending successful')

    def send(self, request_id, body, headers=None):
        try:
            self.conn.send('/queue/MLResponse', body, headers)
            _debug_log.debug(f'{request_id} - Send message response success')

        except BaseException as exp:
            _error_log.error(f'{request_id} - Send message got error: {exp}')
            request_df['response_code'] = '05'



