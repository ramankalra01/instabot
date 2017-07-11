import urllib
from instabot import start_bot
from termcolor import colored

print colored('Checking Instagram server status','red',attrs=['bold'])

code = urllib.urlopen('https://www.instagram.com/').getcode()

if code == 200:
    print colored('Instagram servers are working\n'
                  'Starting InstaBot','red',attrs=['bold'])
    start_bot()
else:
    print colored('Instagram servers are down\n'
                  'Try again later', 'red', attrs=['bold'])