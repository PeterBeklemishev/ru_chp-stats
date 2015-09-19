#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import datetime

input = open('tmp/post_date_commts.txt','r')

day = ''
# day_prev = ''
month = ''
# month_prev = ''
comments_cnt = ''
comm = 0
posts = 0

dow_russian = ['Воскресенье', 'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']
dow_russian_sh = ['Вскр', 'Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб']

comments_per_dow = [0 for x in xrange(0, 7)]
posts_per_dow = [0 for x in xrange(0, 7)]

for line in input.readlines():

    line_cont = [x for x in line.split('\t')]
    date_ = line_cont[1]
    comments_cnt = line_cont[2]

    time_ = date_[11:len(date_)-6]
    date_ = date_[0:10]
    day = date_[8:10]
    month = date_[5:7]
    year = date_[0:4]

    # if day_prev == '':
    #     day_prev = day
    #     month_prev = month
    #     year_prev = year

    comments_cnt = comments_cnt[0:len(comments_cnt)-1]
    if comments_cnt == 'closed':
        comments_cnt = 0

    dow = datetime.date(int(year), int(month), int(day)).strftime("%w")
    # print dow_russian[int(dow)]

    comments_per_dow[int(dow)] = comments_per_dow[int(dow)] + int(comments_cnt)
    posts_per_dow[int(dow)] = posts_per_dow[int(dow)] + 1

    # if not str(day) == str(day_prev):
    #     # if month_prev > 10:
    #         # month_prev = '0'+str(month_prev)
    #     # print date_
    #     print str(year_prev)+'-'+month_prev+'-'+day_prev+','+str(comm)+','+str(posts)+','+str(int(comm)/posts)
    #     # print str(year_prev)+'-'+month_prev+'-01'+'\t'+str(comm)+'\t'+str(posts)
    #     # print
    #     comm = comments_cnt
    #     posts = 1
    # else:
    #     comm = int(comm) + int(comments_cnt)
    #     posts = posts +1

    # day_prev = day
    # month_prev = month
    # year_prev = year
print "dow,dow_russian,comments_count,post_count,average_comments"

for i in range(1,7):
    print str(i)+','+dow_russian_sh[i]+','+str(comments_per_dow[i])+','+str(posts_per_dow[i])+','+str(comments_per_dow[i]/posts_per_dow[i])
i = 0
print str(7)+','+dow_russian_sh[i]+','+str(comments_per_dow[i])+','+str(posts_per_dow[i])+','+str(comments_per_dow[i]/posts_per_dow[i])
# print str(i)+','+dow_russian[i]+','+str(comments_per_dow[i])+','+str(posts_per_dow[i])+','+str(comments_per_dow[i]/posts_per_dow[i])
# print comments_per_dow
# print posts_per_dow