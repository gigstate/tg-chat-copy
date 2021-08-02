import logging
from environs import Env

logging.basicConfig(level=logging.INFO)

env = Env()
env.read_env()