import datetime
from threading import Thread as t

utc = datetime.timezone.utc
print('GT is currently:')

global globalVars
globalVars = [datetime.datetime(2021, 11, 17, 18, 59, 0, tzinfo=utc), '00000000000000']

def output():
    while True:
        text = globalVars[1]
        text = f"{text[0:4]}/{text[4:6]}/{text[6:8]}   {text[8:10]}:{text[10:12]}:{text[12:]}"
        print(' '*20 + '\b'*(len(text) + 30), end=text + '\033[?25l')

def getPassedTime():
    while True:
        number = str(int((datetime.datetime.now().astimezone(utc) - globalVars[0]).total_seconds()))
        globalVars[1] = '0'*(14-len(number)) + number

def main():
    outputThread = t(target=output)
    outputThread.start()
    passedTimeThread = t(target=getPassedTime)
    passedTimeThread.start()

mainThread = t(target=main)
mainThread.start()