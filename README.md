# Changing vault passwords
Project for automatic changing ansible vault passwords in files with ansible vault strings

# Usage
```
chvp [-w WORK_DIR] [-g [LENGTH]] VAULT_ID [VAULT_ID ..]
```
search in *WORK_DIR* for yaml files with ansible vault strings and change vault passsword. if *-g* is provided generate new passwords with default length or LENGTH.
