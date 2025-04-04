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
                      metavar='VID',
                      help='vault ids which password should be changed',
                      type=str,
                      # TODO: no default,
                      default=["vid"],
                      # TODO: required=True
                      required=False)
# generate password ?
cliparser.add_argument('-g', '--gen-passwd',
                      dest='gen_passwd',
                      nargs='?',
                      help='generate passwords for new vault ids.\nif no LENGTH ios provided use default length',
                      default=None,
                      const=20,
                      type=int,
                      metavar="LENGTH",
                      choices=list(range(8,64)))
# readonly modus
cliparser.add_argument('-r', '--readonly',
                        help='show only files and variables that will be changed',
                        action='store_true')

# filename regex
cliparser.add_argument('-m', '--match-file',
                        help='handle only files that match REGEX',
                        dest='match_file',
                        default='.+',
                        metavar="REGEX")

# ignore directories 
cliparser.add_argument('-d', '--ignore-dir',
                        dest='ignore_dir',
                        help='ignore directories that match REGEX',
                        default='/?.git/?',
                        metavar="REGEX")

# ignore files
cliparser.add_argument('-f', '--ignore-files',
                        dest='ignore_dir',
                        help='ignore files that match REGEX',
                        default=None,
                        metavar="REGEX")

argcomplete.autocomplete(cliparser)

