import os, platform,sys,time
def psb(z):

    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.09)


try:
   import requests
except:
   os.system('pip2 install requests')

import requests,time
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('clear')
    psb('\n\n\033[92;1m  AKING BYPASS IN PROGRESS...!')
    time.sleep(2)
    os.system('clear')
    psb('\n\n\n\033[91;1m BYPASS BY SecDet...!')
    time.sleep(5)
    from adnan import readline___Public_Xml
    readline___Public_Xml()
elif bit == '32bit':
    os.system('clear')
    print ('YOUR DEVICE IS 32 BIT')
    print ('')
    print ('UPGRADE YOUR DEVICE AND TRY AGAIN')
