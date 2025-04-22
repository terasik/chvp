# Changing vault passwords
Project for automatic changing ansible vault passwords in yaml files with ansible vault strings. Use *vach* script wchich will be automatic installed by:
```
pip install vach
```

# Usage

```
vach [-h] [-i VID] [-g [LENGTH]] [-n] [--no-sum-file] [--tb] [-m REGEX] [-d REGEX] [-f REGEX] [-V] [PATH ...]
```
positional arguments:
- search in  *PATH* for ansible vault strings and change vault passsword. 
  - Default: *.*. 
  - python `os.walk` used for recursively file search in direct

options:
```
  -h, --help            show this help message and exit
  -i VID, --vault-id VID
                        vault ids which password should be changed (default:
                        ['vid'])
  -g [LENGTH], --gen-passwd [LENGTH]
                        generate passwords for new vault ids. if no LENGTH ios
                        provided use default length (default: None)
  -n, --no-dry          no dry mode. files will be really written (default:
                        False)
  --no-sum-file         don't write summary json file in $HOME (default:
                        False)
  --tb                  show traceback on exceptions (default: False)
  -m REGEX, --match-file REGEX
                        handle only files that match REGEX (default: .+)
  -d REGEX, --ignore-dir REGEX
                        ignore directories that match REGEX (default:
                        /?\.git/?)
  -f REGEX, --ignore-files REGEX
                        ignore files that match REGEX (default: None)
  -V, --version         show program's version number and exit
```

# Default values/Konfiguration


