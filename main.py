import datetime

utc = datetime.timezone.utc
now = datetime.datetime.now().astimezone(utc)
startDate = datetime.datetime(2021, 11, 17, 18, 59, 0, tzinfo=utc)
timePassed = int((now - startDate).total_seconds())

datetimeList = [0, 0, 0, 0, 0, 0]
timesDone = 0
while timePassed >= 1:
    timePassed /= 100
    timePassed = str(timePassed).split('.')
    datetimeList[timesDone] = timePassed[1]
    timePassed = int(timePassed[0])
    timesDone += 1

print(f"{str(datetime.datetime.now()).split('.')[0]} in Galactic Time is:")
print(f"{datetimeList[5]}/{datetimeList[4]}/{datetimeList[3]}   {datetimeList[2]}:{datetimeList[1]}:{datetimeList[0]}")