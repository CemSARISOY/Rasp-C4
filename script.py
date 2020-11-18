import io
import os
import sys
import time
import json
# execute le fichier

pid = os.fork()
if(pid == 0):
    os.popen("python detection.py")

    while not os.path.exists("tab.txt"):
        time.sleep(0.1)

    with io.open("tab.txt", 'r', encoding='utf8') as f:
        text = f.read()
    time.sleep(0.1)
    os.remove("tab.txt")

    print(json.loads(text))
else:
    os.popen("python main.py")
