"""
modul with main main class
"""
import logging
from copy import deepcopy
from .optsargs import cliparser
from .yavault import VaultData, YamlVault
from .utils import ask_vault_id_passwd, gen_secrets, load_yaml, dump_yaml

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

  def _create_new_vault_obj(self, old_vobj):
    """ create new vault from old
    """
    new_vobj=YamlVault(use_new=True, vault_id=old_vobj.vault_id, plain_text=old_vobj.plain_text)
    return new_vobj
    

  def _search_for_vault(self, obj, deep=0):
    """ searching recursiv in obj for vaults
    """
    if type(obj)==dict:
      for k,v in obj.items():
        #logging.info("deep=%s obj=dict key=%s value=%s value_type=%s(%s)", deep,k,v,type(v),type(v).__name__)
        if isinstance(v, (list,dict)):
          self._search_for_vault(v, deep+1)
        elif isinstance(v, (YamlVault)):
          logging.info("++++++ found vault in dict: vid=%s plain=%s", v.vault_id, v.plain_text)
          obj[k]=self._create_new_vault_obj(v)
    elif type(obj)==list:
      for c,v in enumerate(obj):
        #logging.info("deep=%s obj=list value=%s value_type=%s(%s)", deep,v,type(v),type(v).__name__)
        if isinstance(v, (list,dict)):
          self._search_for_vault(v, deep+1)
        elif isinstance(v, (YamlVault)):
          logging.info("++++++ found vault in list: vid=%s plain=%s", v.vault_id, v.plain_text)
          obj[c]=self._create_new_vault_obj(v)
    elif isinstance(obj, (YamlVault)):
      logging.info("++++++++++++++++++ juhu. found vault: vid=%s plain=%s", obj.vault_id, obj.plain_text)
      obj=self._create_new_vault_obj(obj)
    else:
      logging.error("something wrong with obj")
    return obj

      
  def _search_for_vault_2(self, obj, deep=0):
    """ searching recursiv in obj for vaults
        variant 2
    """
    if type(obj)==dict:
      _itr=obj.items():
    elif type(obj)==list:
      _itr=enumerate(obj):
        #logging.info("deep=%s obj=dict key=%s value=%s value_type=%s(%s)", deep,k,v,type(v),type(v).__name__)
        if isinstance(v, (list,dict)):
          self._search_for_vault(v, deep+1)
        elif isinstance(v, (YamlVault)):
          logging.info("++++++ found vault in dict: vid=%s plain=%s", v.vault_id, v.plain_text)
          obj[k]=self._create_new_vault_obj(v)
        #logging.info("deep=%s obj=list value=%s value_type=%s(%s)", deep,v,type(v),type(v).__name__)
        if isinstance(v, (list,dict)):
          self._search_for_vault(v, deep+1)
        elif isinstance(v, (YamlVault)):
          logging.info("++++++ found vault in list: vid=%s plain=%s", v.vault_id, v.plain_text)
          obj[c]=self._create_new_vault_obj(v)
    elif isinstance(obj, (YamlVault)):
      logging.info("++++++++++++++++++ juhu. found vault: vid=%s plain=%s", obj.vault_id, obj.plain_text)
      obj=self._create_new_vault_obj(obj)
    else:
      logging.error("something wrong with obj")
    return obj
      

  def run(self):
    logging.info("run forest run...")
    logging.info("about me:%s%s", "\n",self) 
    #self.handle_vault_data()
    VaultData._show()
    for f in self.src:
      logging.info("loading %s", f)
      obj=load_yaml(f)
      logging.info("loaded obj:%s%s", "\n",obj)
      obj_copy=self._search_for_vault(deepcopy(obj))
      logging.info("modified obj:%s%s", "\n",obj_copy)
      dump_yaml(obj_copy,"~/vach_test_file_new.yml")


    
    
