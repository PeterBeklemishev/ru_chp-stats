#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
# import time
# import datetime
from dateutil.parser import parse
#date, comnts_cnt

input = open('../post_date_commts.txt','r')

month = ''
month_prev = ''
comments_cnt = ''
comm = 0
posts = 0

for line in input.readlines():

    line_cont = [x for x in line.split('\t')]
    date_ = line_cont[1]
    comments_cnt = line_cont[2]

    time_ = date_[11:len(date_)-6]
    date_ = date_[0:10]
    date = date_[8:10]
    month = date_[5:7]
    year = date_[0:4]

    if month_prev == '':
        month_prev = month
        year_prev = year

    comments_cnt = comments_cnt[0:len(comments_cnt)-1]
    if comments_cnt == 'closed':
        comments_cnt = 0

    if not month == month_prev:
        # if month_prev > 10:
            # month_prev = '0'+str(month_prev)
        # print date_
        print str(year_prev)+'-'+month_prev+'-01'+'\t'+str(comm)+'\t'+str(posts)
        # print
        comm = 0
        posts = 0
    else:
        comm = comm + int(comments_cnt)
        posts = posts +1



    month_prev = month
    year_prev = year
