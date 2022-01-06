# PSQL-BACKUP-FILES
All the files needed for the Django-PSQL backup functionality for KWP.

1. getLatestPKs.py is used to get the latest primary keys extracted in a backup. It requires as argument the name of the latest backup file from which PKs are to be extracted.
2. backup.py is used to append the new backup file to the master backup json file using the rules laid out in BACKUP.png. It requires as arguments the names of the master and latest backup files to be provided.
