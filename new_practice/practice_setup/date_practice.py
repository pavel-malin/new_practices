import datetime

from dateutil import tz


def utcnow():
    return datetime.datetime.now(tz=tz.tzutc())


print(utcnow())
print(utcnow().isoformat())
