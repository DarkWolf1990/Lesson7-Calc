# подключаем стандартную функцию логирования
import logging
from Interface import Intface
from Inpt import Reader
# задаем базовую конфигурацию и выводим логи в файл(файлик у нас будет
# перезаписываться внося новые данные), также
# добавляем сразу дату и время,
logging.basicConfig(level=logging.DEBUG, filename="log.txt", filemode ="w",
                    format ="%(asctime)s -%(levelname)s - %(message)s")
# получаем логи 
logger = logging.getLogger(__name__)

# настраиваю обработчик, чтобы журнал передавался в файл
handler = logging.FileHandler('test.txt')
# тут форматирую и передаю аргументы 
formatter= logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# вот здесь добавляю обработчик 
logger.addHandler(handler)
#подключаю функцию
logger.debug('^)^')
logger.debug(Reader)
logger.debug(Intface)


# думаю нужно еще сделать обработчик исключений
try:
  1 / 0
except ZeroDivisionError as e:
  logging.exception("ZerodivisionError")




    
   

