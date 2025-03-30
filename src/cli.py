# PYTHON_ARGCOMPLETE_OK

import argcomplete
#from chvp.optsargs import cliparser
from .chvp import ChangeVaultPasswd as vach

def main():
  #argcomplete.autocomplete(cliparser)
  #opts=cliparser.parse_args()
  #print(opts)
  #print(dict(opts)) 
  a=vach()
  a.run()
