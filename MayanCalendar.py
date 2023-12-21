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
