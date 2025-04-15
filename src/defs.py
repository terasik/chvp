# file with default values
import logging
import os
import re
import configparser

# config file
CFG_DEFAULT_SECTION='main'
CFG_FILE='vach.cfg'
CFG_DIR=os.path.expanduser('~/.vach/')
CFG_SEARCH_DIRS=('.', os.path.expanduser('~'), CFG_DIR)
PASSWD_LEN_MIN=12
PASSWD_LEN_MAX=64


class VachDefs:
  """ class with default config values
  """
  wpath=['.']
  vault_id=['vid']
  passwd_length=20
  match_file_regex='.+'
  ignore_dir_regex='/?\.git/?'
  ignore_file_regex=None

  @classmethod
  def _show(cls):
    for k,v in cls.__dict__.items():
      if k.startswith('_') :
        continue
      logging.debug("defs: %s=%s", k, v)

  @classmethod
  def _check_wpath(cls, value):
    logging.info("wpath config check..")
    cls.wpath=list(set([p for p in re.split(',\s*', value) if p]))
    if not cls.wpath:
      logging.warning("wpath value in config is empty or make no sense")


  @classmethod
  def _check_vault_id(cls, value):
    logging.info("vault_id config check..")
    cls.vault_id=list(set([v for v in re.split(',\s*', value) if v]))
    if not cls.vault_id:
      logging.warning("vault_id value in config is empty or make no sense")

  @classmethod
  def _check_passwd_length(cls, value):
    try:
      value=int(value)
    except:
      raise TypeError("can't cast passwd_length from config to int. please provide only integers (%s..%s)" % (PASSWD_LEN_MIN,PASSWD_LEN_MAX))
    if isinstance(value, (int)):
      if value<PASSWD_LEN_MIN or value>PASSWD_LEN_MAX:
        #logging.error("wrong passwd_length in config. please provide only integers %s..%s",PASSWD_LEN_MIN,PASSWD_LEN_MAX)
        raise ValueError("passwd_length in config is wrong. please provide only integers %s..%s" % (PASSWD_LEN_MIN,PASSWD_LEN_MAX))
    
    
  


def read_vach_cfg():
  """ read vach config file
  """
  #VachDefs.show()
  def_sec=CFG_DEFAULT_SECTION
  cfg=configparser.ConfigParser()
  cfg.SECTRE=re.compile(r"\[ *(?P<header>[^]]+?) *\]")
  try:
    ff=cfg.read([f"{d}/{CFG_FILE}" for d in reversed(CFG_SEARCH_DIRS)])
  except Exception as exc:
    logging.error("reading config files: %s: %s:", type(exc).__name__, exc)
    return 
  if not ff:
    logging.info("no config files found")
    return
  logging.info("found config files: %s", ff)
  if not cfg.has_section(def_sec):
    logging.warning("no '%s' section found in cfg. ignore cfg", def_sec)
    return
  logging.debug("items in cfg  %s section: %s", def_sec, cfg.items(def_sec))
  for k,v in cfg.items(def_sec):
    if hasattr(VachDefs, f"_check_{k}"):
      check_func=getattr(VachDefs, f"_check_{k}")
      check_func(v)
    else: 
      setattr(VachDefs, k, v)
  VachDefs._show()


  
