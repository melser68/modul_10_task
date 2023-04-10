
import func_birthday as basic

def __main__():

    now_day = basic.now_days()

    date_end = basic.delta_dates(now_day)

    res_jubilars = basic.anniversaries_in_the_week(now_day, date_end)

    basic.print_result(res_jubilars)


__main__()

#Виходив з того Що потрібно рахувати "тиждень наперед" 
# це наприклад від понеділка до понеділка включно.