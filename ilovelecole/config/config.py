import os
from shutil import copyfile

BASE_DIR = os.path.dirname(os.path.dirname(__file__))






config = {
    'dev': DevelopmentConfig,
    'production': ProductionConfig,
}