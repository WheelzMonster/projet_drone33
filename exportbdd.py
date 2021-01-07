import subprocess

username = 'dronefruuz340'
password = 'K84vk6cDKQyK'
database = 'dronefruuz340'

with open('file.sql','w') as output:
    c = subprocess.Popen(['mysqldump --host=dronefruuz340.mysql.db', '-u',username,'-p%s'%password,database],
                         stdout=output, shell=True)

# mysqldump -u root -p bddtestwp > C:\Users\Louis\Desktop\mysqltest.txt

#mysqldump --host=the.remotedatabase.com -u yourusername -p yourdatabasename > /User/backups/adump.sql