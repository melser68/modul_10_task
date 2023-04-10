
from datetime import date, datetime, timedelta
import locale
locale.setlocale(locale.LC_ALL, "")

users = [{'name': 'John', 'birthday': '1999-04-11'}, {
    'name': 'Mike', 'birthday': '2001-04-12'},
    {'name': 'Dilan', 'birthday': '1995-04-13'},
    {'name': 'Robert', 'birthday': '1997-02-21'}]

dict_birth_in_week = dict()


def now_days():
    now_date = datetime.now()
    return now_date


def delta_dates(now_day):
    delta_dates = timedelta(7)
    date_end = now_day + delta_dates
    return date_end


def anniversaries_in_the_week(now_day, date_end):

    for kards in users:
        for keys, value in kards.items():
            if keys == 'name':
                name = value
            else:
                date_birth = now_day.strftime('%Y') + '-' + value.split('-')[1] + '-' + value.split('-')[2]
                date_birth = datetime.strptime(date_birth, '%Y-%m-%d')

                if  datetime.isoweekday(date_birth) == 6:
                    date_birth += timedelta(2)
                elif datetime.isoweekday(date_birth) == 7:
                    date_birth += timedelta(1)

                day_in_week = date_birth.strftime('%A')

                if 'birthday' in keys and now_day <= date_birth <= date_end:

                    rez = dict_birth_in_week.get(day_in_week)
                    if rez == None:
                        dict_birth_in_week.update({day_in_week:[name]})
                    else:
                        rez.append(name)
                        dict_birth_in_week.update({day_in_week:rez})

    return dict_birth_in_week



def print_result(res_jubilars):
    
    for key, value in res_jubilars.items():
        a = (',  ').join(value)
        print(key, ' : ', a)