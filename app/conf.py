import logging
from environs import Env

logging.basicConfig(
    format=u"%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s",
    level=logging.ERROR,
)

env = Env()
env.read_env()