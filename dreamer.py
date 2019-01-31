#!/usr/bin/env python3

import itertools
import calendar
import copy
days_per_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]

""" I Feel Like tis one is a bit too straight forward of a solution, maybe a shortcut I'm missing """


for _ in range(int(input())):
    day, month, year = map(list, input().split())
    all_digits = day + month + year # list of strings
    years = set(itertools.permutations(all_digits, 4)) # set of tuples of characters
    mini_date = ["99","99","9999"]
    dates = [] # list of lists of strings
    for y in years:
        potiential_date = ["","",""] # list of formatted strings
        int_year = int("".join(yi for yi in y)) # int representation of year
        if int_year >= 2000:
            potiential_date[2] = "".join(yi for yi in y)
            month_pool = list(all_digits)
            for a in y:
                month_pool.remove(a)
            months = set(itertools.permutations(month_pool, 2)) # set of tuples of characters
            for m in months:
                int_month = int("".join(mi for mi in m)) # int representation of month
                if int_month > 0 and int_month < 13:
                    potiential_date[1] = "".join(mi for mi in m)
                    day_pool = list(month_pool)
                    for a in m:
                        day_pool.remove(a)
                    days = set(itertools.permutations(day_pool, 2))
                    for d in days:
                        #print(mini_date)
                        int_day = int("".join(di for di in d)) # int representation of day
                        if int_day > 0:
                            if int_day <= days_per_month[int_month] or (calendar.isleap(int_year) and int_month == 2 and int_day <= 29):
                                potiential_date[0] = "".join(di for di in d)
                                dates.append(potiential_date)
                                # find the mini_date
                                #print(potiential_date,mini_date)

                                if int(potiential_date[2]) < int(mini_date[2]):
                                    #print("0", potiential_date[2], mini_date[2])
                                    mini_date = copy.deepcopy(potiential_date)
                                elif int(potiential_date[2]) == int(mini_date[2]):
                                    if int(potiential_date[1]) < int(mini_date[1]):
                                        #print("1", potiential_date[1], mini_date[1])
                                        mini_date = copy.deepcopy(potiential_date)
                                    elif int(potiential_date[1]) == int(mini_date[1]):
                                        if int(potiential_date[0]) < int(mini_date[0]):
                                            #print("2", potiential_date[0], mini_date[0])
                                            mini_date = copy.deepcopy(potiential_date)
    print(len(dates), end = "") 
    if len(dates) > 0:
        print("",mini_date[0], mini_date[1], mini_date[2])
    else:
        print()





    