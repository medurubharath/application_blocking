from datetime import datetime
import os,platform
def calucation(startTime, endTime, nowTime):
    if startTime <=nowTime<=endtime:
        return 1
    else:
        return 0
def converttosec(time):
    h, m, s = time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


now = datetime.now()
present=converttosec(now.strftime("%X"))
start=converttosec(now.strftime("00:00:00"))
endtime=converttosec(now.strftime("00:00:00"))
result=calucation(start,endtime,present)
if result==1:
    count=1
    if count==1:
        count+=1
        try:
            a = platform.system().upper()
            b = 'WINDOWS'
            c='LINUX'
            d='MACOS'
            if a == b:
                os.system("taskkill /f /im chrome.exe & ver > nul")
                os.system("taskkill /f /im brave.exe & ver > nul")

            if a == c:
                os.system("taskkill /f /im chrome.exe & ver > nul")
                os.system("taskkill /f /im brave.exe & ver > nul")

            if a == d:
                os.system("taskkill /f /im chrome.exe & ver > nul")

                os.system("taskkill /f /im brave.exe & ver > nul")

        except Exception:
            pass

    if count>=2:
        print("bye")
else:
    print("bye")
