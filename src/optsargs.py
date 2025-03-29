"""
parse command line arguments

chvp [-g [LENGTH]] -i VAULT_ID [VAULT_ID ..] 

"""

import argparse
#import argcomplete
#from .yavault import VaultData

cliparser=argparse.ArgumentParser(
                    prog='chvp',
                    description='change vault password in yaml files with ansible vault strings',
                    epilog='be carefull with this prog. make backup bevor changing or track your changes with some version control prog')
# positional arguments files or directories
cliparser.add_argument('src',
                      nargs='*',
                      default=['.'])
# provide vault ids
cliparser.add_argument('-i', '--vault-id',
                      action='append',
                      type=str,
                      required=True)
# generate password ?
cliparser.add_argument('-g', '--generate', '--gen-passwd', '--generate-password',
                      dest='gen_passwd',
                      nargs='?',
                      default=None,
                      const=20,
                      type=int,
                      choices=list(range(8,64)))



