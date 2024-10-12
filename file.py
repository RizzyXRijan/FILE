import os, platform, time, sys
os.system('xdg-open https://chat.whatsapp.com/GKCh3wB9KoU9oDuy0MsZ7v')
try:
 import requests
except:os.system("pip install requests")
print(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m CHECKINF FOR UPDATES..!')
os.system('git pull --quiet ')
bit = platform.architecture()[0]
if bit == "64bit":
 print(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m 64 BIT FOUND..!')
 time.sleep(2)
 from filebyroheet import menu
 menu()
 
 
 
if bit == "32bit":
 print(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m 32 BIT DETECTED..!')
 print(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m 32 BIT NOT SUPPORTED..!')
 time.sleep(2)
 exit()
