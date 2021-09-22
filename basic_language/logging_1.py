import logging

logging.basicConfig(format='%(asctime)-15s - %(filename)s:%(lineno)d - %(funcName)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.warning('This will get logged as warning')

logging.info('This will get logged as info')


