#10.Demonstrate python program to display some information about the OS where the script is running

import os
import sys
import inspect

print(os.name)#it gives information about os name
print(os.path)#it gives information about the current path of the script file
print ("Python " + sys.version)#it gives the version of os
print (os.getcwd())#current working directory
print( os.path.basename(__file__))#filename
print (os.path.abspath(__file__))#absolutepath of file
print (os.path.dirname(__file__))#directory name
