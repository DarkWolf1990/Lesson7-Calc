# подключаем стандартную функцию логирования
import logging
import Calculator
import Interface
# задаем базовую конфигурацию и выводим логи в файл(файлик у нас будет
# перезаписываться внося новые данные), также
# добавляем сразу дату и время,
logging.basicConfig(level=logging.INFO, filename="log.txt", filemode ="w",
                    format ="%(asctime)s -%(levelname)s - %(message)s")
# это уровни журналаб выше в коде также сделана настройка журналов

# Использую канкатинацию, чтобы склеить строки, 
# также передаю в лог подключенные файлы.
logging.info(f"{Calculator}")
logging.debug("info")
logging.warning("warning")
logging.error("error")
logging.critical(f"{Interface}")

