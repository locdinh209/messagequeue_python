from common.activemq_listener import StompConnection
from common.logger import _info_log, _debug_log, _error_log
import asyncio

def main():
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(StompConnection.create_connection())
        loop.run_forever()
    except:
        raise RuntimeError("Could not start service.")
    finally:
        loop.stop()
        _info_log.info("Stop ML message queue service sucessful")

if __name__ == '__main__':
    main()
    _info_log.info("Start ML message queue service sucessful")
