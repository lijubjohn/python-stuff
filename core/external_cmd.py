# The advantage of subprocess vs. system is that it is more flexible
# (you can get the stdout, stderr, the "real" status code, better error handling, etc...).
import subprocess

subprocess.run(["ls", "-l"])

# OR
import os

os.system("ls -ltr")
