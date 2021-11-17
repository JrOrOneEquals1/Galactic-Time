import datetime
import time
utc = datetime.timezone.utc
startDate = datetime.datetime(2021, 11, 17, 18, 59, 0, tzinfo=utc)
timePassed = int((datetime.datetime.now().astimezone(utc) - startDate).total_seconds())
datetimeList = [0, 0, 0, 0, 0, 0]
timesDone = 0
while timePassed >= 1:
    datetimeList[timesDone] = int(str(timePassed)[-2:])
    try:
        timePassed = int(str(timePassed)[:-2])
    except ValueError:
        break
    timesDone += 1
datetimeString = f"{datetimeList[5]}/{datetimeList[4]}/{datetimeList[3]}   {datetimeList[2]}:{datetimeList[1]}:{datetimeList[0]}"
print(f"{str(datetime.datetime.now()).split('.')[0]} in Galactic Time is:")
print(datetimeString)
print('\n')

if input('Loop? [y/n]\n>^< ').startswith('y'):
    while True:
        timePassed = str((datetime.datetime.now().astimezone(utc) - startDate).total_seconds())
        datetimeList = [0, 0, 0, 0, 0, 0]
        timesDone = 0
        while int(timePassed) >= 1:
            datetimeList[timesDone] = timePassed[-2:]
            try:
                timePassed = timePassed[:-2]
            except ValueError:
                break
            timesDone += 1
        datetimeString = f"{datetimeList[5]}/{datetimeList[4]}/{datetimeList[3]}   {datetimeList[2]}:{datetimeList[1]}:{datetimeList[0]}"
        print(' '*20 + '\b'*(len(list(datetimeString)) + 30), end=datetimeString + '\033[?25l')
        time.sleep(0.001)