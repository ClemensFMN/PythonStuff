import logging


def f1(x):
    logging.info("inside the f1(x) function")
    logging.info("called with x = {}".format(x))
    return(x+1)
                 


logging.basicConfig(format='%(asctime)-15s - %(filename)s:%(lineno)d - %(funcName)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.warning('This will get logged as warning')

logging.info('This will get logged as info')

f1(4)
