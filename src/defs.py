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


class VachDefs:
  """ class with default values
  """
  passwd_length=20
  file_match_regex='.+'
  ignore_dir_regex='/?\.git/?'
  ignore_file_regex=''

  @classmethod
  def show(cls):
    for k,v in cls.__dict__.items():
      if k.startswith('_'):
        continue
      logging.info("VachDefs: %s=%s", k, v)
  


def read_vach_cfg():
  """ read vach config file
  """
  VachDefs.show()
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
  logging.info("items in cfg  %s section: %s", def_sec, cfg.items(def_sec))
  for k,v in cfg.items(def_sec):
    setattr(VachDefs, k, v)
  VachDefs.show()


  
