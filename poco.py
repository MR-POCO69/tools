import os, sys, platform
os.system('git pull')
bit = platform.architecture()[0]
if bit == '64bit':
    import FXX
else:
    sys.exit("32 bit not work")
