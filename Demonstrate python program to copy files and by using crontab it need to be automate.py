#Demonstrate python program to copy files and by using crontab it need to be automate.
import schedule
import time
import os

import shutil
from shutil import copyfile


def job():
    dst='tmp2'
    src = os.listdir("tmp")
    if os.path.exists(dst):
         for files in src:
            if files.endswith(".txt"):
                shutil.copy(files,dst)
    else:
        os.makedirs(dst)
        for files in src:
            if files.endswith(".txt"):
                shutil.copy(files,dst) 
      

#by using crontab it can be automated in following way

#setting up executable python environment
#!/usr/bin/env python3

#Make the script executable by:
#chmod u+x C:/CODING TEST/p6.py

#Open your cron table by
#crontab -e 

#Add the following cron entry:
#*/10 * * * *   C:/CODING TEST/p6.py#running cronjob for every 10 minutes



