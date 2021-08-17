from dotenv import load_dotenv
import subprocess
import sys
load_dotenv()
def install():
 subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
packagesoption = input('Warning this is about to install a bunch of packages, continue? (y/n) ')
if packagesoption == 'y':
 install()
if packagesoption == 'n':
 exit()
token = input('Provide your discord bot token: ')
reddityesno = input('Do you want reddit? (y/n)')
if reddityesno == 'y':
 clientid = input('\n\n\n\nProvide your client_id: ')
 clientsecret = input('Provide your client_secret: ')
 username = input('Provide your application username: ')
 password = input('Provide your application password: ')
weatheryesno = input('Do you want the weather command? (y/n)')
if weatheryesno == 'y':
 api_key= input('Go to openweathermap.org and obtain the Current Weather Data api key. Provide that key here: ')
with open(".env", "a") as f:
 f.write(f"TOKEN={token}\n")
 if reddityesno == 'y':
  f.write(f"client_id={clientid}\n")
  f.write(f"client_secret={clientsecret}\n")
  f.write(f"username={username}\n")
  f.write(f"password={password}\n")
 if weatheryesno == 'y':
  f.write(f"api_key={api_key}")