# some logging to stdout
"""
old_factory = logging.getLogRecordFactory()

def record_factory(*args, **kwargs):
    record = old_factory(*args, **kwargs)
    record.custom_attribute = 0xdecafbad
    return record

logging.setLogRecordFactory(record_factory)
"""
import logging
import os
from .defs import read_vach_cfg

LOG_DIR=os.path.expanduser('~/log')
LOG_FILE=f"{LOG_DIR}/vach.log"

try:
  os.mkdir(LOG_DIR)
except FileExistsError:
  pass
except Exception as exc:
  print(f"ERROR [__init__.py] can't create log directory '{LOG_DIR}': ({type(exc).__name__}) {exc}")
  pass

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s [%(process)d %(module)s %(lineno)d %(funcName)s] %(message)s", filename=LOG_FILE) 
console=logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(logging.Formatter("%(levelname)s [%(module)s %(funcName)s] %(message)s"))
logging.getLogger('').addHandler(console)
read_vach_cfg()
