# PYTHON_ARGCOMPLETE_OK

import argcomplete
from chvp.optsargs import cliparser

def main():
  argcomplete.autocomplete(cliparser)
  opts=cliparser.parse_args()
  print(opts)
  
