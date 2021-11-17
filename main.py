import datetime
import time

utc = datetime.timezone.utc
startDate = datetime.datetime(2021, 11, 17, 18, 59, 0, tzinfo=utc)
print('Galactic Time is currently:')

while True:
    timePassed = str(int((datetime.datetime.now().astimezone(utc) - startDate).total_seconds()))
    GTstring = '0'*(14 - len(timePassed)) + timePassed
    datetimeString = f"{GTstring[0:4]}/{GTstring[4:6]}/{GTstring[6:8]}   {GTstring[8:10]}:{GTstring[10:12]}:{GTstring[12:]}"
    print(' '*20 + '\b'*(len(list(datetimeString)) + 30), end=datetimeString + '\033[?25l')
    time.sleep(0.001)