import datetime
utc = datetime.timezone.utc
timePassed = int((datetime.datetime.now().astimezone(utc) - datetime.datetime(2021, 11, 17, 18, 59, 0, tzinfo=utc)).total_seconds())
datetimeList = [0, 0, 0, 0, 0, 0]
timesDone = 0
while timePassed >= 1:
    timePassed = str(timePassed / 100).split('.')
    datetimeList[timesDone] = timePassed[1]
    timePassed = int(timePassed[0])
    timesDone += 1
print(f"{str(datetime.datetime.now()).split('.')[0]} in Galactic Time is:\n{datetimeList[5]}/{datetimeList[4]}/{datetimeList[3]}   {datetimeList[2]}:{datetimeList[1]}:{datetimeList[0]}")
