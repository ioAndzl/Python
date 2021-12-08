import os
import sys
import logging
from sys import path
from root_logging import create_logger, exception

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, dir_path)
LOGS = False
# Create Logger for debug mode in local
if LOGS:
    logs_filename = os.path.join(dir_path, 'exc_logs.log')
    logger = create_logger(logs_filename=logs_filename)
else:
    logger = None
   

# while not content:
#     if time() - start > timeout:
#         break
#     sleep(1)
    
if __name__=='__main__':
    print('there')
    logger = create_logger('main', debug=True)
    DEBUG=True
    @exception(logger, DEBUG)
    def test_logger(a):
        return a/0
    test_logger(2)
    logger.debug('¤¤¤This is a debug message¤¤¤')