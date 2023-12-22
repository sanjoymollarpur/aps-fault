from sensor.logger import logging
from sensor.exception import SensorException
import sys, os 

def test_logger_and_exception():
    try:
        logging.info("Starting test logger")
        r=3
        print(r)
        logging.info("Stop test logger")
    except Exception as e:
        raise SensorException(e, sys)


if __name__=="__main__":
    try:
        test_logger_and_exception()
    except Exception as e:
        print(e)