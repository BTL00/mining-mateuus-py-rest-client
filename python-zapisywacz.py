import subprocess
import sys
import requests
from datetime import datetime
import re

patternTrex = ".*\[\sOK\s\].*"
patternGminer = ".*Accepted.*"

def doPOST(id):
	url = 'https://mining.mateu.us/share?id='+str(id)
	x = requests.post(url, data = {})
	if(x.status_code == 200):
		print("Send POST -> Ok!")
	else:
		print("Send POST -> "+ str(x.status_code))


if __name__ == "__main__":
	if (len(sys.argv) < 3 or sys.argv[1] == "--help"):
		print("args: command user_id")
		exit()
	datestring = datetime.today().strftime('%Y-%m-%d-%H%M%S')
	with open(datestring+'.log', 'wb') as f:  # replace 'w' with 'wb' for Python 3
		process = subprocess.Popen(sys.argv[1], stdout=subprocess.PIPE)
		for line in process.stdout:  # replace '' with b'' for Python 3
			if (re.match(patternTrex, str(line)) or re.match(patternGminer, str(line))):
				doPOST(sys.argv[2])
			print(line)
			f.write(line)
