#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
# import time
# import datetime

input = open('post_date_commts.txt','r')

month = ''
month_prev = ''
comments_cnt = ''
comm = 0
posts = 0

top_elem_cnt = 100
top = [9-y for y in xrange(1,top_elem_cnt)]
top_link = ["" for y in xrange(1,top_elem_cnt)]
# print top

for line in input.readlines():
    
    line_cont = [x for x in line.split('\t')]
    # date_ = line_cont[0]
    post = line_cont[0]
    comments_cnt = line_cont[2]

    # time_ = date_[11:len(date_)-6]
    # date_ = date_[0:10]
    # date = date_[8:10]
    # month = date_[5:7]
    # year = date_[0:4]

    # if month_prev == '':
    #     month_prev = month
    #     year_prev = year

    comments_cnt = comments_cnt[0:len(comments_cnt)-1]
    if comments_cnt == 'closed':
        comments_cnt = 0

    # if not month == month_prev:
    #     # if month_prev > 10:
    #         # month_prev = '0'+str(month_prev)
    #     # print date_
    #     #print str(year_prev)+'-'+month_prev+'-01'+'\t'+str(comm)+'\t'+str(posts)
    #     # print
    #     comm = 0
    #     posts = 0
    # else:
    #     comm = comm + int(comments_cnt)
    #     posts = posts +1

    for x in xrange(0,len(top)):
        if top[x] > int(comments_cnt):
            pass
        else:
            top[x] = int(comments_cnt)
            top_link[x] = 'http://ru-chp.livejournal.com/'+post+'.html'
            break


print "№,comm_cnt,link"
for x in xrange(0,len(top)):
    print `x+1`+','+`top[x]`+','+top_link[x]
    # print x+1,'\t',top[x],'--',top_link[x]

    # month_prev = month
    # year_prev = year
