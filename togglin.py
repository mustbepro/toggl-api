#!/usr/bin/python3
from random import randint
import calendar
from collections import defaultdict

array = [1, 2 ,3 ,4, 5]
week = []

#for i in array:
#     week.append(randint(4,7))

total_time = 20
count = 0

#while (count < total_time):
#    entry = randint(4,7)
#
#    if((entry + count) < total_time):
#        week.append(entry)
#        count += entry
#
#    elif((count + 4) >= total_time):
#        week.append((total_time - count))
#        break


def populate_hours(total_time=None):
    if total_time != None:
        count = 0
        week = []
        while count < total_time:
            entry = randint(4,7)
            if (entry + count) < total_time:
                    week.append(entry)
                    count += entry
            elif (count + 4) >= total_time:
                week.append(total_time - count)
                break
        if len(week) < 5:
            week.append(0)
    return week


#x = populate_hours(20)

#print (x)
def populate_days(name=None, task_num=None, total_time=None):

    output = {}
    #output = []

    #task_name = name
    output['task_name'] = name
    #test_name = name
    hours = populate_hours(total_time)
    count = 0
    output[task_num] = hours
#    for item in hours:
#        count += 1
#        output[count] = item

    #output['hours'] = hours
    #mylist.append(output)

    return output
#

task_list = []
task_list.append(populate_days("task_1", 1, 20))
task_list.append(populate_days("task_2", 2, 20))

#y = len(x)
print (task_list)

tyd = [{'task': '1', 'hour': '[1, 2, 7]'}, {'task': '2', 'hour': '[3, 4, 0]'}]
entry = [{'task_1': '1', 'task_2': '2', 'task_3': '7'}]

for item in tyd:
    print (item)
#print ("dict len: ", y)

#array_len = len(x)
count = 0


#all_hours = [{1: [1, 2, 7]}, {2: [3, 4, 0]}, {3: [5, 6, 0]}]
all_hours = [[1, 2, 7], [3, 4, 0], [5, 6, 0]]

#def gen_hour_entries(all_hours=[])

count = 0
all_hours_len = len(all_hours)
day_hours = 8
day_limit = 0
day_count = 1
#entries = defaultdict(list)
entries = {}
list_entries = []

while True:
    for item in all_hours:
            array_len = len(item)-1
            if item[count] != 0:
                if (day_limit + item[count]) <= day_hours:
                    day_limit += item[count]
                    entries[day_count].append(item[count])
                    #entries['task'].append(day_count)
                    #print ("day count: {} hour: {}".format(day_count, item[count]))
                elif (day_limit + item[count]) > day_hours:
                    remainder = day_hours - day_limit
                    carry_over = item[count] - remainder
                    entries[day_count] = remainder
                    #print ("day count: {} hour: {}".format(day_count, remainder))
                    day_count += 1
                    day_limit = carry_over
                    #print ("day count: {} hour: {}".format(day_count, carry_over))
                    entries[day_count] = carry_over
    list_entries.append(entries)

    count += 1
    if count > array_len:
        break
print ("entries: ", list_entries)
# -- backup code ------------------------------------------------------------------

#while True:
#    for item in all_hours:
#            array_len = len(item)-1
#            if item[count] != 0:
#                if (day_limit + item[count]) <= day_hours:
#                    day_limit += item[count]
#                    entries[day_count].append([item[count]])
#                    #entries['task'].append(day_count)
#                    #print ("day count: {} hour: {}".format(day_count, item[count]))
#                elif (day_limit + item[count]) > day_hours:
#                    remainder = day_hours - day_limit
#                    carry_over = item[count] - remainder
#                    entries[day_count].append([remainder])
#                    #print ("day count: {} hour: {}".format(day_count, remainder))
#                    day_count += 1
#                    day_limit = carry_over
#                    #print ("day count: {} hour: {}".format(day_count, carry_over))
#                    entries[day_count].append([carry_over])
#    count += 1
#    if count > array_len:
#        break
#print ("entries: ", entries)

# ^- backup code ------------------------------------------------------------------


#2013-03-05T07:00:00.000Z
#def date_list(start_month=None, start_day=None, end_month=None, end_day=None):

def date_list(start_date=[], end_date=[]):

        start_year = start_date[0]
        start_month = start_date[1]
        start_day = start_date[2]

        end_year = end_date[0]
        end_month = end_date[1]
        end_day = end_date[2]

        day_start = 9
        day_end = 5


        if start_month == end_month:
            for item in range(start_day, end_day+1):
                dow = calendar.weekday(start_year, start_month, item)
                if dow in range(0, 5):
                    #print ("This is a week day: ", dow)
                    print ("{}-{}-{}T".format(start_year, start_month, item))
                else:
                    #print ("This is NOT a week day: ", dow)
                    print ()


date_list([2017, 12, 15], [2017, 12, 20])

