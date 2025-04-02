# Changing vault passwords
Project for automatic changing ansible vault passwords in yaml files with ansible vault strings

# Usage
changing vault password 
```
chvp -i VAULT_ID [VAULT_ID ..] [-g [LENGTH]] [-r] [-m REGEX] [-d REGEX] [--debug] DIR_OR_FILE [DIR_OR_FILE ..]
```
positional arguments:
- search in multiple *DIR_OR_FILE* for ansible vault strings and change vault passsword. 
  - Default: *.*. 
  - python `os.walk` used for recursively file search 

options:
- *-i* option used to provide VAULT_IDs. 
  - Option is required. 
- *-g* option generate new passwords with default length or LENGTH for VAULT_IDs. 
  - Default: *none* (read new passwords from stdin)
- *-r* option used for readonly operations and only shows files that will be changed. 
  - Default: *false*
- *-m* use for files regex. read/write only filenames matching the REGEX. 
  - Default: *.+*
- *-d* ignore directories/files matching REGEX. 
  - Default: */?\.git/?*
- *--debug* show also debug statement- *--debug* show also debug statements
