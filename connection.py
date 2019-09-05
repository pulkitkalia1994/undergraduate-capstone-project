import urllib
import time

def connected(host='http://google.com'):
    try:
        urllib.urlopen(host)
        return True
    except:
        return False

# test
print( 'connected' if connected() else 'no internet!' )
if connected():
	execfile("/home/pi/myemail.py")
else:
	time.sleep(2)
	execfile("/home/pi/connection.py")