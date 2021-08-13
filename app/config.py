import logging
from environs import Env

date_strftime_format = "%H:%M:%S"

logging.basicConfig(
    format=u"%(filename)s:%(lineno)d [%(levelname)s] [%(asctime)s]  %(message)s",
    datefmt=date_strftime_format,
    level=logging.WARNING,
)

env = Env()
env.read_env()