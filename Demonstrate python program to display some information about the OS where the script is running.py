#10.Demonstrate python program to display some information about the OS where the script is running

import os
import sys
import platform

print ('uname:', platform.uname())
print ('os name  :',os.name)
print ('system   :', platform.system())
print ('node     :', platform.node())
print ('release  :', platform.release())
print ('version  :', platform.version())
print ('machine  :', platform.machine())
print ('processor:', platform.processor())
print('python version:', platform.python_version())
