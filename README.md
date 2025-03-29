# Changing vault passwords
Project for automatic changing ansible vault passwords in files with ansible vault strings

# Usage
changing vault password in directories
```
chvp [-g [LENGTH]] -i VAULT_ID [VAULT_ID ..] -d DIR [DIR ..]
```
Change vault password in files
```
chvp [-g [LENGTH]] -i VAULT_ID [VAULT_ID ..] -f FILE [FILE ..]
```
search in *DIR*, multiple DIRectories or FILEs for ansible vault strings and change vault passsword. if *-g* is provided generate new passwords with default length or LENGTH for vVAULT_IDs. With *-i* Option you must provide VAULT_IDs
