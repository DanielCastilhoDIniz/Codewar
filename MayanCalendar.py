"""
Mayan Calendar
The Mayan civilisation used three different calendars. In their long count calendar there were 20 days (called kins) in a uinal, 18 uinals in a tun, 20 tuns in a katun and 20 katuns in a baktun. In our calendar, we specify a date by giving the day, then month, and finally the year. The Maya specified dates in reverse, giving the baktun (1-20), then katun (1-20), then tun (1-20), then uinal (1-18) and finally the kin (1-20).

The Mayan date 13 20 7 16 3 corresponds to the date 1 January 2000 (which was a Saturday).

Write a program which, given a Mayan date (between 13 20 7 16 3 and 14 1 15 12 3 inclusive), outputs the corresponding date in our calendar. You should output the month as a number.

Example:
13 20 9 2 9  # Mayan date 22 March 2001
22 3 2001  # Gregorian date 22 March 2001
You are reminded that, in our calendar, the number of days in each month is:

1    January    31
2    February    28 / 29 (leap year)
3    March    31
4    April    30
5    May    31
6    June    30
7    July    31
8    August    31
9    September    30
10    October    31
11    November    30
12    December    31
Input/Output
[input] string representing the Mayan date in the form baktun katun tun uinal kin
[output] string representing the Gregorian date in the form dd mm yyyy
"""

# 13 20 7 16 3 usar para alinhar

def convert_mayan(datee):
    from datetime import date, timedelta
    baktun, katun, tun, uinal, kin = [int(x) for x in datee.split()]
    total_days = (kin-3) + ((uinal-16) * 20) + (360*(tun - 7)) + \
        (7200*(katun - 20)) + (144000*(baktun - 13))

    gregorian_date = date(2000, 1, 1) + timedelta(days=total_days)

    dia = gregorian_date.day
    mes = gregorian_date.month
    ano = gregorian_date.year

    return f"{dia} {mes} {ano}"


print(convert_mayan("13 20 7 16 3"))
print(convert_mayan("13 20 7 16 4"))
print(convert_mayan("13 20 9 2 9"))


def convert_mayan1(datee):
    from datetime import date
    reference_day = 2018843
    baktun, katun, tun, uinal, kin = [int(x) for x in datee.split()]
    days = kin + uinal * 20 + 360*tun + 7200*katun + 144000*baktun
    start = 730120
    diference_days = (days - reference_day)

    dia = (date.fromordinal(start+int(diference_days))).day
    mes = (date.fromordinal(start+int(diference_days))).month
    ano = (date.fromordinal(start+int(diference_days))).year

    return f"{dia} {mes} {ano}"


print(convert_mayan1("13 20 7 16 3"))
print(convert_mayan1("13 20 7 16 4"))
print(convert_mayan1("13 20 9 2 9"))


# pythonico
from datetime import datetime, timedelta
REF = datetime(2000, 1, 1)

def convert_mayan(date):
    baktun, katun, tun, uinal, kin = [int(x) for x in date.split()]
    return (REF + timedelta(days = kin+20*(uinal+18*(tun+20*(katun+20*baktun))) - 2018843)).strftime('%-d %-m %Y')
