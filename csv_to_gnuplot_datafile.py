#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

inputfolder = 'output/ru-chp'
inputfile = 'posts.csv'
valueseparator = ','
needed_columns = [2, 5, 6]

input = open(inputfolder + '/'+inputfile,'r')


for line in input.readlines():
    # print line
    l_prev = ''
    l = ''
    line_s = []
    istags = 0

    line_cont = [x for x in line.split(',')]
    for l in line_cont:
        if '[' in l:
    		if ']' in l:
    			#ok, no ',' in tags
    			line_s.append(l)
    		else:
    			#tag opening found
    			l_prev = l
    			istags = 1
    	else:
    		#this is not tag or tag
    		if ']' in l:
    			#this is final tag value
    			#concatenting this and prev value - this is a tag
    			l_prev = l_prev + '_,' + l
    			line_s.append(l_prev)
    			istags = 0
 	
    		else:
    			#looking on the istags value
    			if istags == 1:
    				#concatenting this and prev value - this is a part of tags
    				l_prev = l_prev + '_' + l
    				# line_s.append(l_prev)
    			else:
    				#this is normal content
    				line_s.append(l)
    
    i = 0
    line = ''
    for l_ in line_s:
        i = i + 1
        for j in needed_columns:
            if i == j:
                # print l.decode('UTF-8'),'\t',
                if j == needed_columns[0]:
                    line = l_
                else:
                	line = line + '\t' + l_
    print line,