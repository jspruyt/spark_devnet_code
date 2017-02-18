import logging
import random

logger = logging.getLogger('Test')
# change this to logging.ERROR for silence
logger.setLevel(logging.INFO)
FORMAT = '%(asctime)s %(funcName)s(): %(message)s'
logging.basicConfig(format=FORMAT, datefmt='%Y-%m-%d %H:%M:%S')

logger.info("Picking a random number")
rand_num = random.randint(0,100)

if rand_num <= random.randint(0,100):
    logger.info("Picked number is smaller or equal to the newly generated random number...")
    print(rand_num)
else:
    logger.info("Picked number was greater than newly generated random number...")
    print(0)