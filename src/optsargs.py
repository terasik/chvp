"""
parse command line arguments

chvp [-g [LENGTH]] -i VAULT_ID [VAULT_ID ..] 

"""

import argparse
import argcomplete
#from .yavault import VaultData
from .defs import VachDefs, PASSWD_LEN_MIN, PASSWD_LEN_MAX

cliparser=argparse.ArgumentParser(
                    prog='chvp',
                    description='change vault password in yaml files with ansible vault strings',
                    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                    epilog='be carefull with this prog. make backup bevor changing or track your changes with some version control prog')

# positional arguments files or directories
cliparser.add_argument('wpath',
                      nargs='*',
                      metavar="PATH",
                      # TODO. default=['.']
                      default=VachDefs.wpath)
# provide vault ids
cliparser.add_argument('-i', '--vault-id',
                      action='append',
                      dest='vault_id',
                      metavar='VID',
                      help='vault ids which password should be changed',
                      type=str,
                      # TODO: no default,
                      default=VachDefs.vault_id,
                      # TODO: required=True
                      required=False)
# generate password ?
cliparser.add_argument('-g', '--gen-passwd',
                      dest='gen_passwd',
                      nargs='?',
                      help='generate passwords for new vault ids.\nif no LENGTH ios provided use default length',
                      default=None,
                      const=VachDefs.passwd_length,
                      type=int,
                      metavar="LENGTH",
                      choices=list(range(PASSWD_LEN_MIN, PASSWD_LEN_MAX)))
# readonly modus
cliparser.add_argument('-r', '--readonly',
                        help='show only files and variables that will be changed',
                        action='store_true')

cliparser.add_argument('--tb',
                        help='show traceback on exceptions',
                        action='store_true')

# filename regex
cliparser.add_argument('-m', '--match-file',
                        help='handle only files that match REGEX',
                        dest='match_file_rgx',
                        default=VachDefs.match_file_regex,
                        metavar="REGEX")

# ignore directories 
cliparser.add_argument('-d', '--ignore-dir',
                        dest='ign_dir_rgx',
                        help='ignore directories that match REGEX',
                        default=VachDefs.ignore_dir_regex,
                        metavar="REGEX")

# ignore files
cliparser.add_argument('-f', '--ignore-files',
                        dest='ign_file_rgx',
                        help='ignore files that match REGEX',
                        default=VachDefs.ignore_file_regex,
                        metavar="REGEX")

argcomplete.autocomplete(cliparser)

