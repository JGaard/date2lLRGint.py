import datetime, time

def dateTimetoLargeInt(date):
    seconds_in_year = 31556900
    epoch_time_no_subseconds = int(date)
    current_time = (seconds_in_year * (1969 - 1600) + epoch_time_no_subseconds) * 10000000

    print current_time

date = datetime.date(1988,03,21)
date = time.mktime(date.timetuple())

dateTimetoLargeInt(date)

