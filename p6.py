#Demonstrate python program to copy files and by using crontab it need to be automate.
import shutil
from shutil import copyfile


shutil.copyfile('file1.txt', 'file2.txt',follow_symlinks=True)




#by using crontab it can be automated in following way



#Make the script executable by:

#chmod u+x C:/CODING TEST/p6.py

#setting up executable python environment
#!/usr/bin/env python3


#Open your cron table by
#crontab -e 

#Add the following cron entry:
#*/10 * * * *   C:/CODING TEST/p6.py#running cronjob for every 10 minutes



