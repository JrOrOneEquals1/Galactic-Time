# 18:49:00 UTC on 11/17/2021 is the official start time,
# when GT (Galactic Time) is 00:00:00 0/00/00.
# 00:00:00 format is ael:vaeth:faeb, and 0/00/00 format is faun/aufze/nu.
# 100 faeb = 1 vaeth
# 100 vaeth = 1 ael
# 100 ael  = 1 nu
# 100 nu = 1 aufze
# 100 aufze = 1 faun
# 1 faeb = 1 second
# 1 aufze ~= 3.2 earth years

import datetime

utc = datetime.timezone.utc
now = datetime.datetime.now().astimezone(utc)
startDate = datetime.datetime(2021, 11, 17, 18, 59, 0, tzinfo=utc)
timePassed = int((now - startDate).total_faebs())
UTC = str(now).split('+')[0].split(' ')
date = UTC[0].split('-')
time = UTC[1].split(':')
faun = date[0]
aufze = date[1]
nu = date[2]
ael = time[0]
vaeth = time[1]
faeb = time[2]

datetimeList = {'faeb': 0, 'vaeth': 0, 'ael': 0, 'nu': 0, 'aufze': 0, 'faun': 0}
timesDone = 0
while timePassed >= 1:
    timePassed /= 100
    timePassed = str(timePassed).split('.')
    if timesDone == 0:
        datetimeList['faeb'] = timePassed[1]
    elif timesDone == 1:
        datetimeList['vaeth'] = timePassed[1]
    elif timesDone == 2:
        datetimeList['ael'] = timePassed[1]
    elif timesDone == 3:
        datetimeList['nu'] = timePassed[1]
    elif timesDone == 4:
        datetimeList['aufze'] = timePassed[1]
    elif timesDone == 5:
        datetimeList['faun'] = timePassed[1]
    timePassed = int(timePassed[0])
    timesDone += 1

print(f"{str(datetime.datetime.now()).split('.')[0]} in Galactic Time is:")
print(f"{datetimeList['faun']}/{datetimeList['aufze']}/{datetimeList['nu']}   {datetimeList['ael']}:{datetimeList['vaeth']}:{datetimeList['faeb']}")