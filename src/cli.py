# PYTHON_ARGCOMPLETE_OK

import logging
import traceback
import argcomplete
#from chvp.optsargs import cliparser
from .chvp import ChangeVaultPasswd as vach

def main():
  #argcomplete.autocomplete(cliparser)
  #opts=cliparser.parse_args()
  #print(opts)
  #print(dict(opts)) 
  try:
    a=vach()
    a.run()
  except Exception as exc:
    logging.error("ups.. exception a la '%s' with message: %s", type(exc).__name__, exc)
    if a.tb:
      print(traceback.format_exc())
    return 1
  return 0
