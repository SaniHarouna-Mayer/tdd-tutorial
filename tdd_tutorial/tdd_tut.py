import yaml
from datetime import datetime

# with open('hands_on/currenty_things.yml', 'r') as db:
#     mydby = yaml.full_load(db)

def is_current(dic):
    begin_year = None
    begin_month = None
    begin_day = None
    end_year = None
    end_month = None
    end_day = None
    for key, val in dic.items():
        if key == 'begin_year':
            begin_year = val
        if key == 'begin_month':
            begin_month = val
        if key == 'begin_day':
            begin_day = val
        if key == 'end_year':
            end_year = val
        if key == 'end_month':
            end_month = val
        if key == 'end_day':
            end_day = val
        if key == 'year':
            begin_year = val
            end_year = val
        if key == 'month':
            begin_month = val
            begin_month = val
        if key == 'day':
            begin_day = val
            end_day = val
    present_date = datetime.now()
    if not begin_year:
        begin_year = present_date.year
    if not begin_month:
        begin_month = present_date.month
    if not begin_day:
        begin_day = present_date.day
    if not end_year:
        end_year = present_date.year
    if not end_month:
        end_month = present_date.month
    if not end_day:
        end_day = present_date.day
    # try:
    begin_date = datetime(begin_year, begin_month, begin_day)
    end_date = datetime(end_year, end_month, end_day)
    # except:
    #     return False
    if begin_date <= present_date and end_date >= present_date:
        return True
    else:
        return False

if __name__ == "__main__":
    for key0, val0 in mydby.items():
        for key1, val1 in val0.items():
            if isinstance(val1, list):
                for dic in val1:
                    print(is_current(dic))
            elif isinstance(val1, dict):
                for key2, val2 in val1.items():
                    print(is_current(val2))
