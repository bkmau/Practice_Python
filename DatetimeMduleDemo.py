import datetime
import pytz

splitter = "{:+<200}".format("")
print("List available properties and methods of datetime\r\n{}".format(dir(datetime)))
print(splitter)

print("datetime module")
print("{: <65}:{}".format("datetime.date(2017, 7, 12)", datetime.date(2017, 7, 12)))
print("{: <65}:{}".format("datetime.time(12, 61, 60)", datetime.time(12, 23, 56)))
print("{: <65}:{}".format("datetime.datetime(2017, 7, 12, 12, 23, 56)",
                          datetime.datetime(2017, 7, 12, 12, 23, 56)))
print("{: <65}:{}".format("datetime.datetime.fromtimestamp(45456666.79)", datetime.datetime.fromtimestamp(45456666.79)))
print("tday = datetime.date.today()")
tday = datetime.date.today()
print("{: <65}:{}".format("tday", tday))
print("{: <65}:{}".format("tday.year", tday.year))
print("{: <65}:{}".format("tday.weekday()", tday.weekday()))
print("{: <65}:{}".format("tday.isoweekday()", tday.isoweekday()))
print("{: <65}:{}".format("tday.isoweekday()", tday.isoweekday()))
print("tnow = datetime.datetime.now()")
tnow = datetime.datetime.now()
print("{: <65}:{}".format("tnow", tnow))
print("{: <65}:{}".format("tnow.date()", tnow.date()))
print("{: <65}:{}".format("tnow.time()", tnow.time()))
print("{: <65}:{}".format("tnow.timestamp()", tnow.timestamp()))
print("{: <65}:{}".format("tnow.timetz()", tnow.timetz()))
print(splitter)

print("datetime format")
print("tdaynow = datetime.datetime.now()")
tdaynow = datetime.datetime.now()
date_str = tdaynow.strftime("%b %d, %Y %a %H:%M:%S")
print("date_str = {}".format(date_str))
print("{: <65}:{}".format("tdaynow.strftime(\"%b %d, %Y %a\")", tdaynow.strftime("%b %d, %Y %a %H:%M:%S")))
print("{: <65}:{}".format("datetime.datetime.strptime(date_str, \"%b %d, %Y %a %H:%M:%S\")",
                          datetime.datetime.strptime(date_str, "%b %d, %Y %a %H:%M:%S")))
print("{: <65}:{}".format("tdaynow.isoformat()", tdaynow.isoformat()))
print(splitter)

print("datetime.timedelta")
tdelta = datetime.timedelta(days=3, hours=1.5)
print("tdaynow = datetime.datetime.now()")
print("tdelta = datetime.timedelta(days=3, hours=1.5)")
print("{: <65}:{}".format("tdaynow", tdaynow))
print("{: <65}:{}".format("tdaynow + tdelta", tdaynow + tdelta))
print("{: <65}:{}".format("tdaynow - tdelta", tdaynow - tdelta))
print("td1 = datetime.datetime(2017, 10, 28, 18, 49, 20)")
print("td2 = datetime.datetime(2016, 5, 9, 4, 12, 20)")
td1 = datetime.datetime(2017, 10, 28, 18, 49, 20)
td2 = datetime.datetime(2016, 5, 9, 4, 12, 20)
tdelta = td1 - td2
print("{: <65}:{}".format("tdelta = td1 - td2", tdelta))
print(splitter)

print("timezone aware")
# print("Print all timezones in pytz")
# for tz in pytz.all_timezones:
#     print(tz)

print("{: <65}:{}".format("datetime.datetime.today()", datetime.datetime.today()))
print("{: <65}:{}".format("datetime.datetime.now()", datetime.datetime.now()))
print("{: <65}:{}".format("datetime.datetime.utcnow()", datetime.datetime.utcnow()))

print("specify timezone")
print("tzone = pytz.timezone(\"Asia/Taipei\")")
t_zone = pytz.timezone("Asia/Taipei")
print("{: <65}:{}".format("datetime.datetime.today().replace(tzinfo=t_zone)",
                          datetime.datetime.today().replace(tzinfo=t_zone)))
print("{: <65}:{}".format("datetime.datetime.now(tz=t_zone)", datetime.datetime.now(tz=t_zone)))
print("{: <65}:{}".format("datetime.datetime.utcnow().replace(tzinfo=t_zone)",
                          datetime.datetime.utcnow().replace(tzinfo=t_zone)))
print("{: <65}:{}".format("t_zone.localize(datetime.datetime.now())", t_zone.localize(datetime.datetime.now())))

print("Change TimeZone...")
print("utc_now = datetime.datetime.now(tz=pytz.UTC)")
utc_now = datetime.datetime.now(tz=pytz.UTC)
print("{: <65}:{}".format("utc_now", utc_now))
print("{: <65}:{}".format("utc_now.astimezone(tz=t_zone)", utc_now.astimezone(tz=t_zone)))
