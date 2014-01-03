import datetime, time

def dateTimetoLargeInt(year, month, day):
    seconds_in_year = 31556900
    epoch_time_no_subseconds = int(convertDate(year, month, day))
    LargeIntTime = (seconds_in_year * (1969 - 1600) + (epoch_time_no_subseconds - 22500)) * 10000000

    return LargeIntTime

def convertDate(year, month, day):
    date = datetime.datetime(year, month, day)
    return time.mktime(date.timetuple())
