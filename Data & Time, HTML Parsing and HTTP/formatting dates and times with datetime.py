# Getting more control over formatting
from datetime import datetime

now = datetime.now()

# %a ==> abbreviated day of week: Mon, Tues, Wed
# %A ==> full name of the day of week: Monday, Tuesday, Wednesday
# %d ==> day of month: number 10 for the 10th of January

print(now.strftime("%a %A %d"))

# %b ==> abbreviated month name: Jan, Feb
# %B ==> full month name: January
# %m ==> month as number: 01 for January

print(now.strftime("%b %B %m"))
print(now.strftime("%a %B %d"))

# %H ==> hours
# %M ==> minutes
# %S ==> seconds
# %p ==> AM or PM

print(now.strftime("%H : %M : %S%p"))

# %y ==> abbreviated year as two numbers: 17
# %Y ==> year as four numbers: 2017

print(now.strftime(" %y %Y"))