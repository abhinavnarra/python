import schedule
import time

import shutil
from shutil import copyfile

def job():
    shutil.copyfile('file1.txt', 'file2.txt')
    
#schedule.every(1).minutes.do(job)
#schedule.every().hour.do(job)
schedule.every().day.at("8:48").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1) 
#this code will copy the files every 1 minutes hours , days, time 
