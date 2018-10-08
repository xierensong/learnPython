#coding=utf-8

import logging
from pathlib import Path

current_path = Path('.')

log_file = current_path / '..' / 'log' / 'xxx.log'
logging.basicConfig(filename=str(log_file), filemode='w', level=logging.DEBUG)
logging.debug('debuging')