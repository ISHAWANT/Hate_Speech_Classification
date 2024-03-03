from hate.logger import logging 
from hate.exception import CustomException 
import os,sys 
logging.info('this is nlp based project')

try:
    a=1/0
    print(a)

except Exception as e:
    # logging.info(e)
    logging.info(CustomException(e,sys))
    raise CustomException(e,sys)