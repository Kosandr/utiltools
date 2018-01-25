from datetime import timedelta, datetime, time
import datetime as dt

def get_day_start(dt):
   '''Given datetime, returns beginning of the day'''
   hour = dt.hour
   second = dt.second
   minute = dt.minute
   microsecond = dt.microsecond

   new_dt = dt - timedelta(hours=hour, seconds=second, minutes=minute, microseconds=microsecond)

   return new_dt

def get_day_end(dt):
   '''Given a date, returns end of day'''
   day_start = get_day_start(dt)
   day_end = day_start + timedelta(hours=23, minutes=59)

   return day_end


def date_to_datetime(date):
   time_to_add = time(0, 0, 0, 0)
   return datetime.combine(date, time_to_add)


def datetime_from_str(str_dt):
   return datetime.strptime(str_dt, '%Y-%m-%d %H:%M:%S.%f')
import time as tm

def datetime_to_unix(d):
   return tm.mktime(d.timetuple())

def unix_to_datetime(x):
   return datetime.fromtimestamp(int(x))



#def datetime_to_utc_tstamp(dt):
#   return datetime_to_unix(dt)

def datetime_now():
   return datetime.now()

def datetime_utc_now():
   return datetime.utcnow()

def tstamp_to_utc_datetime(tstamp):
   return datetime.utcfromtimestamp(tstamp)


