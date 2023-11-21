import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatting = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatting)
logger.addHandler(stream_handler)

file_handler = logging.FileHandler('sample.log')
file_handler.setFormatter(formatting)
logger.addHandler(file_handler)


def my_func():
    logger.info('실행 로그')


my_func()
