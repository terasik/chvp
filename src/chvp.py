"""
modul with main main class
"""
import logging
from .optsargs import cliparser
from .yavault import VaultData
from .utils import ask_vault_id_passwd, gen_secrets

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

  def handle_vault_data(self):
    """ read old vault paswords from stdin
    if '-g' option provided generate new vault passwds
    else read new passwords from stdin
    """ 
    # asking for old passwords
    for vid in self.vault_id:
      p=ask_vault_id_passwd(vid)
      VaultData.data.update({vid: p})
    # generate new passwords
    if self.gen_passwd is not None:
      ps=gen_secrets(length=self.gen_passwd, count=len(self.vault_id))
      for c,vid in enumerate(self.vault_id):
        VaultData.data_new.update({vid: ps[c]})
    else:
      for vid in self.vault_id:
        # type new password
        p1=ask_vault_id_passwd(vid, False)
        # retype new password
        p2=ask_vault_id_passwd(vid, False, True)
        if p1!=p2:
          raise ValueError("different passwords for the same vault_id")
        VaultData.data_new.update({vid: p1})
        

  def run(self):
    logging.info("run forest run...")
    logging.info("about me: %s", self) 
    #self.handle_vault_data()
    VaultData.show()


    
    
