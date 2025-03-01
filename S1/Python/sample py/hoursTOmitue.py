#18 WAP to convert hours to minute and seconds.

hour = int(input("Enter the hour: "))
minute = int(input("Enter the minute: "))

minute1 = hour * 60
minute = minute1 + minute
second = minute * 60

print(minute,"m",second,"s")


