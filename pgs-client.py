import subprocess
import os
from datetime import datetime
from subprocess import PIPE

p_diff = subprocess.run(["git", "diff", "--numstat"], stdout=PIPE, stderr=PIPE, universal_newlines=True)

message = []
message.append("Py Git Sync auto-commit - " + datetime.now().strftime("%Y-%m-%d %H:%M"))
for line in p_diff.stdout.split(os.linesep):
    if (line == ''):
        break
    ch = line.split("\t")
    message.append("[" + ch[0] + "-" + ch[1] + "] " + ch[2])

subprocess.run(["git", "add", "--all"])

commit_cmd = ["git", "commit"]
for line in message:
    commit_cmd.append("-m")
    commit_cmd.append(line)

subprocess.run(commit_cmd)
subprocess.run(["git", "push", "sync", "frank-dev"])
