humanYears = float(input('Enter age:'))
dYears = humanYears * 7
dMonths = dYears % 1
dYears = dYears - dMonths
dMonths = dMonths * 12
dDays = dMonths % 1
dMonths = dMonths - dDays
dDays = dDays * 30
d = dDays % 1
dDays = dDays - d



print(f'your age in dog years is {dYears:.0f} years {dMonths:.0f} months {dDays:.0f} days')

cYears = humanYears / 9
cMonths = cYears % 1
cYears = cYears - cMonths
cMonths = cMonths * 12
cDays = cMonths % 1
cMonths = cMonths - cDays
cDays = cDays * 30
c = cDays % 1
cDays = cDays - c


print(f'your age in cat years is {cYears:.0f} years {cMonths:.0f} months {cDays:.0f} days')

hYears = 3 * ((((humanYears ** 2) - 47)/7)+12)
hMonths = hYears % 1
hYears = hYears - hMonths
hMonths = hMonths * 12
hDays = hMonths % 1
hMonths = hMonths - hDays
hDays = hDays * 30
h = hDays % 1
hDays = hDays - h

print(f'your age in horse years is {hYears:.0f} years {hMonths:.0f} months {hDays:.0f} days')