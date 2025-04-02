"""
parse command line arguments

chvp [-g [LENGTH]] -i VAULT_ID [VAULT_ID ..] 

"""

import argparse
import argcomplete
#from .yavault import VaultData

cliparser=argparse.ArgumentParser(
                    prog='chvp',
                    description='change vault password in yaml files with ansible vault strings',
                    epilog='be carefull with this prog. make backup bevor changing or track your changes with some version control prog')
# positional arguments files or directories
cliparser.add_argument('src',
                      nargs='*',
                      # TODO. default=['.']
                      default=['~/vach_test_file.yml'])
# provide vault ids
cliparser.add_argument('-i', '--vault-id',
                      action='append',
                      dest='vault_id',
                      meta="VID",
                      type=str,
                      # TODO: no default,
                      default=["vid"],
                      # TODO: required=True
                      required=False)
# generate password ?
cliparser.add_argument('-g', '--gen-passwd',
                      dest='gen_passwd',
                      nargs='?',
                      default=None,
                      const=20,
                      type=int,
                      meta="LENGTH",
                      choices=list(range(8,64)))
# readonly modus
cliparser.add_argument('-r', '--readonly',
                        action='store_true')

# filename regex
cliparser.add_argument('-m', '--match-file'
                        dest='match_file',
                        meta="REGEX")

# ignore directories 
cliparser.add_argument('-d', '--ignore-dir',
                        dest='ignore_dir',
                        meta="REGEX")

# ignore directories 
cliparser.add_argument('-f', '--ignore-files',
                        dest='ignore_dir',
                        meta="REGEX")

argcomplete.autocomplete(cliparser)

