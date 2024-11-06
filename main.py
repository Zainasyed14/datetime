import datetime
x=datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%d") + " " + x.strftime("%B") + " " + x.strftime("%Y"))