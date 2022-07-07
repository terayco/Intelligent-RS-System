import os
import sys


sys.path.append("PaddleRS")
os.system("git clone https://github.com/PaddleCV-SIG/PaddleRS > /dev/null")
os.system("pip install -r PaddleRS/requirements.txt > /dev/null")
os.system("pip install -e PaddleRS/")
