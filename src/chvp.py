"""
modul with main main class
"""
import logging
from .optsargs import cliparser
from .yavault import VaultData

class ChangeVaultPasswd():
  """ class for changing vault passworsi
  """
  def __init__(self):
    logging.info("start of the starts")
    self.cliargs=cliparser.parse_args()
    self._set_cliargs_to_myself()

  def __str__(self):
    s=("cliargs", "run")
    l=[f"{k}={v}" for k,v in self.__dict__.items() if (not  k.startswith("_")) and (k not in s) ]
    return "\n".join(l)   

  def _set_cliargs_to_myself(self):
    for k,v in vars(self.cliargs).items():
      self.__dict__.update({k:v})


  def run(self):
    logging.info("run forest run...")
    logging.info("about me: %s", self) 


    
    
