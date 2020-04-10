from datetime import date, timedelta
from datetime import datetime

def get_dates(s_year,s_month,s_date,e_year,e_month,e_date):
    startDate = date(s_year, s_month, s_date)
    endDate = date(e_year, e_month, e_date)
    delta = endDate - startDate
    date_list = []
    for i in range(delta.days + 1):
        day = startDate + timedelta(days=i)
        date_list.append(day.strftime("%Y-%m-%d"))
    return date_list

dates = get_dates(2007,1,1,2008,1,1)
print(dates)
