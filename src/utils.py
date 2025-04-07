
"""
modul with helper functions
- yaml vault dumpers
- generating password
"""
__all__=["dumps_obj", "load_yaml", "dump_yaml", "gen_secrets", "ask_vault_id_passwd"]

import logging
import os
import string
import secrets
from getpass import getpass
import yaml
from .yavault import get_plain_dumper,get_cipher_dumper,get_loader
from .defs import VachDefs

# decorators
def expand_user(f):
  def inner(*args):
    #print("len args %s" % len(args))
    new_args=list(args)
    try:
      #print(new_args)
      new_args[-1]=os.path.expanduser(args[-1])
    except:
      pass
    return f(*new_args)
  return inner

@expand_user
def load_yaml(path):
  """ load yaml file
  params:
    path: str -> path to yaml file
  return:
    y: dict,list -> loaded yaml object
  """
  logging.debug("trying to read %s as yaml", path)
  with open(path) as f:
    y=yaml.load(f, Loader=get_loader())  
  return y
   
def dumps_obj(obj):
  """ return indentet json object
  as string. converting to ascii is disabled

  params: 
    obj: object to dump
  return: 
    s: str -> object as json string
  """
  s=yaml.dump(obj, Dumper=get_plain_dumper(), explicit_end=False, indent=2, default_style='')
  return s

@expand_user
def dump_yaml(obj, path):
  """ write obj to path as yaml
  params:
    obj: yaml -> yaml object to write
    path: str -> path to file where obj will be written
  return: -
  """
  logging.debug("writing yaml object to %s", path)
  with open(path, 'w') as _fw:
    _fw.write(yaml.dump(obj, Dumper=get_cipher_dumper()))

def gen_secrets(**kwargs):
  """ generate password(s)
  or url safe token(s)
  """
  secs=[]
  token=kwargs.get("token", False)
  length=kwargs.get("length", VachDefs.passwd_length)
  count=kwargs.get("count", 1)
  for _ in range(count):
    if not token:
      a = string.ascii_letters + \
          "_" + \
          string.digits
      secs.append(''.join(secrets.choice(a) for i in range(length))) 
    else:
      secs.append(secrets.token_urlsafe())
  return secs

def ask_vault_id_passwd(vid, old=True, retype=False):
  """ function that read vault_id(vid) from stdin
  """
  for _ in range(2):
    try:
      if old:
        p=getpass("old password for vault_id=%s: " % vid)
      else:
        if retype:
          p=getpass("retype new password for vault_id=%s: " % vid)
        else:
          p=getpass("new password for vault_id=%s: " % vid)
    except KeyboardInterrupt:
      logging.info("ctrl-c received")
      continue
    p=p.strip()
    if not p:
      logging.warning("invalid or empty password provided")
      continue
    return p
  raise ValueError("invalid or empty password provided")


class VachContext:
  """ context class for logging
  and general purpose.
  """
  wpath=""

class VachFile:
  def __init__(self, path):
    self.path=path
    self.vault_vars=[]
    self.written=False
    self.error=False
    self.skipped=False

class VachSummary:
  """ class with all informations about
  what file and what variables was written
  """
  def __init__(self):
    self.all_files=[]
    self.cur_file=None

  def add_new_file(self,path)
    if self.cur_file is not None:
      self.all_files.append(self.cur_file)
    self.cur_file=VachFile(path)

