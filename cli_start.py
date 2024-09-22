import argparse as ap
import logging
import sys

def run():
    # setup logging
    logger = logging.getLogger(__name__)
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)
    # test logging
    logger.warning("LKJLJLj")
    logger.info('Started')

    ## setup a parser for command line options
    parser = ap.ArgumentParser()
    # one optional argument of type int
    parser.add_argument("-n", "--num", help="provide an integer value", type=int)
    # one mandatory argument of any type
    parser.add_argument("-t", "--text", help="a string value", required=True)
    args = parser.parse_args()
    logger.info(args.num)
    logger.info(args.text)



if __name__ == "__main__":
    
    run()
