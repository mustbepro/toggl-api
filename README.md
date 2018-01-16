# README #

my first python attempt. Making a api to automate my toggl. time tracking thing :<

## notes ##

logic:

    read json tasks list containing: the task name, percentage time spend, min hours, max hours

    json example:
        building infra: 50
        support: 30
        other: 20

    generate random entry for tasks percentage of timestamps between 9 and 5 daily, but calucated weekly
    minimum entry: 4.00 hours
    maximum entry: 8.00 hours

    calulate hours per week and percentages:

        hours in week 8*5=40

        50 percent of 40 = 40/100*50 = 20
        30 percent of 40 = 40/100*30 = 12
        20 percent of 40 = 40/100*20 = 8

    devide 20 hours between 5 days, range from 9 to 5:

        gen.random.num between 4 and 8:
        random.num=5
        total_hours=20
        cap_hours= total_hours - task_min_entry
        count=0


        while (count < (task1_week_hours - task1_min_entry) && cap_hours < (count+min_hour))

            random_num = gen.random.num between 4 and 8

            if((random_num+count) < cap_hours)
            save_entry... = random_num
            count += random_num

        save_entry... = total_hours - count


    array must have 5 entries. each task1_save_entry put into array, if gen.random.num is done and array not full, put 0

    task2, task3:
        for i in task1_save_entry[@]

            hours_due = 8 - task1_total_hours
            task2_save_entry.. = hours_due/100*task2_percent
            task3_save_entry.. = hours_due/100*task3_percent

            POST task1




'{"time_entry":{"description":"Haxing","tags":["billed"],"pid":123,"created_with":"curl"}}' \
