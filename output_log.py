import logging
import logging.handlers
import test
from logger import handler 


# шкала уровеней по приоритетам
'''

NOTSET - 0
DEBUG - 10
INFO - 20
WARNING - 30
ERROR - 40
CRITICAL - 50

''' 

file_log = logging.FileHandler('Log.txt')
console_out = logging.StreamHandler()

logging.basicConfig(handlers=(file_log, console_out), 
                    format='[%(asctime)s | %(levelname)s]: %(message)s', 
                    datefmt='%m.%d.%Y %H:%M:%S',
                    level=logging.DEBUG)

logging.debug('Info message??))')


