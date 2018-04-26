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
      
schedule.every().day.at("18:37").do(job)
#schedule.every().seconds.do(job)
#schedule.every().hour.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1) 
#this code will copy the files every 1 minutes hours , days, time 
