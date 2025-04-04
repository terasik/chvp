# some logging to stdout
import logging
from .defs import read_vach_cfg
logging.basicConfig(level=logging.INFO, format="%(levelname)s [%(module)s %(funcName)s] %(message)s") 
read_vach_cfg()
