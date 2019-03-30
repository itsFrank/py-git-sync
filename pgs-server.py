import subprocess
import os
from datetime import datetime
from subprocess import PIPE

p_pull = subprocess.run(["git", "pull", "sync", "frank-dev"], stdout=PIPE, stderr=PIPE, universal_newlines=True)
found = p_pull.stdout.find("Already up-to-date.")

if (found == -1):
    subprocess.run(["make"])