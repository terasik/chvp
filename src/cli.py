# PYTHON_ARGCOMPLETE_OK

import argcomplete
import logging
#from chvp.optsargs import cliparser
from .chvp import ChangeVaultPasswd as vach

def main():
  #argcomplete.autocomplete(cliparser)
  #opts=cliparser.parse_args()
  #print(opts)
  #print(dict(opts)) 
  a=vach()
  try:
    a.run()
  except Exception as exc:
    logging.error("ups exception a la %s with message %s", type(exc).__name__, exc)
