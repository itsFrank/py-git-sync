import subprocess
import os
from datetime import datetime
from subprocess import PIPE
import sys
import time

timeout_s = 3
if (len(sys.argv)>1):
    timeout_s = int(sys.argv[1])

while True:
    p_pull = subprocess.run(["git", "pull", "sync", "frank-dev"], stdout=PIPE, stderr=PIPE, universal_newlines=True)
    found = p_pull.stdout.find("Already up-to-date.")

    if (found == -1):
        subprocess.run(["make"])
        print("--- Make Complete ---")
    
    time.sleep(timeout_s)