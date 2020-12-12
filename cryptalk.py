import subprocess
import requests as r
from time import time, sleep
import sys
from codec import *

log = open("log.txt", 'a')
log.write('\n' + str(time()) + '\n')
frontend = subprocess.Popen("./frontend", stdout=log, stderr=log)

other_ip = sys.argv[1]
online = False
while not online:
    try:
        assert r.get("http://" + other_ip).status_code == 200
        online = True
    except (r.exceptions.ConnectionError, AssertionError):
        print("Other side is not responding. Retrying(Ctrl+C to terminate)...")
        sleep(1)

interrupted = False
last = ''

while not interrupted:
    try:
        msg = encode(input())
    except KeyboardInterrupt:
        interrupted = True
        break

    with open("current.txt", 'w') as input_stream:
        input_stream.write(msg)

    new = r.get("http://" + other_ip).text
    if new == last:
        continue
    try: print(decode(new))
    except IndexError: print(last, new)
    last = new

frontend.kill()
