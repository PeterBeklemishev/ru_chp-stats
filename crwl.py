#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import urllib2
import time

soo = 'ru-chp'
outputfolder = 'output/'+soo
# startdate = '2012/02/20/'
startdate = '2011/01/30/'
# для тестов
crawl_delay = 5
iferror_delay = 5
max_page_crawl = 30000
# postcount = 2465
# tagscount = 9102
postcount = 0
tagscount = 0

print "Это кравлер по тэгам сообщества",soo
print "\nРезультат будет в папке",outputfolder

def process_page(page_content):
	global postcount
	global tagscount
	# print 'i get page with length ' + `len(page_content)` + '\n'
	# print 'get ' + `len(page_content)`
	page = BeautifulSoup(page_content)
	posts = page.findAll('dl', {'class' : 'entry hentry'})
	posts_c = 0
	for post in posts:
		posts_c = posts_c +1
		# print "\nnext_post\n"

		# post author
		post_autor__ = post.find('a', {'class' : 'i-ljuser-username'})
		post_autor = post_autor__.find('b').string + ' (' + post_autor__['href'] + ')'
		# post date
		post_date = post.find('dd', {'class' : 'entry-date'}).find('abbr')['title']
		# post id
		post_id = post.find('a', {'class' : 'subj-link'})['href']
		post_id = post_id[len('http://'+soo+'.livejournal.com/'):len(post_id)-len('.html')]
		# comments_count
		comments_count = post.find('a', {'class' : 'btn btn-comments'})
		if comments_count is not None:
			comments_count = comments_count.find('span').find('span').find('span').string
		else:
			comments_count = 'closed'
		# tags list
		tags_arr = post.findAll('a', {'rel' : 'tag'})
		# print tags_arr
		tags_list = []
		for tag in tags_arr:
			# print tag.string
			tags_list.append(tag.string)
		#кодировка ломается
		# print '    тут кодировка ломается'
		# print (tags_list)
		result_tags = ''
		for tag_ in tags_list:
			result_tags += tag_.string + ","
			# line_id,post_id,date,tag,comment_count
			tagscount +=1
			output_tags.write(`tagscount`+','+post_id+','+post_date.encode('utf-8')+','+tag_.string.encode('utf-8')+','+comments_count.encode('utf-8')+'\n')

		result_tags = result_tags[0:len(result_tags)-1]
		result_tags = '[' + result_tags + ']'

		# print 'saving grabbed shit to file'
		# print(i+','+post_id+','+'post_autor'+','+result_tags+','+comments_count+'\n')
		# global postcount
		# postcount = postcount + 1
		postcount +=1;
		print 'post',postcount,'(',post_id,')'
		output_posts.write(`postcount`+','+post_id+','+post_autor.encode('utf-8')+','+result_tags.encode("utf-8")+','+post_date.encode('utf-8')+','+comments_count.encode('utf-8')+'\n')
		# output.write((`1`+','+post_id+','+`post_autor`+','+`tags_list`+','+comments_count+'\n').decode('utf-8').encode('utf-8'))#.encode('utf-8'))

		
		# print 'this is post with id',post_id,'$username'
		# post_id = post_parsed.find('dl', align=re.compile('^b.*'))['id']
	return posts_c
	# print 'next page'

def getfilename(whichof):
	if whichof == 'posts':
		return outputfolder + '/posts.csv'
	elif whichof == 'tags':
		return outputfolder + '/tags.csv'
	else:
		return outputfolder + '/bytag/' + whichof +'.csv'

	return outputfolder + '/posts.csv'

output_posts = open(getfilename('posts'),'a+')
output_tags = open(getfilename('tags'),'a+')
output_posts.write('\n------\n')
output_tags.write('\n------\n')

page_crawled_count = 0
request_string_blank = 'http://'+soo+'.livejournal.com/'+startdate
request_string = request_string_blank
request_string_prev = ''
notend = True

notgood = 0
while notend:
	# print "     ..."
	req = urllib2.Request(request_string)

	try:
		response = urllib2.urlopen(req)
	except urllib2.HTTPError as e:
		print e.code
		notgood = 1
		# print e.read() 
	# response = urllib2.urlopen(req)
	if response is not None:
		the_page = response.read()
	else:
		notgood = 1

	if notgood == 0:
		print 'loaded',request_string
		pricessed_c = process_page(the_page)
		if pricessed_c > 0:
			print 'crawled',pricessed_c,'posts on loaded page'
			page_crawled_count +=1
		else:
			print 'no posts found on page',request_string
		# page_crawled_count +=1
		request_string = BeautifulSoup(the_page).find('li', {'class':'next'}).find('a', {'class':'item'})['href']
		if request_string == request_string_prev:
			notend = False
			print request_string,'not changed!!!'
		else:
			request_string_prev = request_string
			time.sleep(crawl_delay)
		if page_crawled_count >= max_page_crawl:
			notend = False
	else:
		# If smth go wrong
		# request_string not changed, try again
		# but wait
		time.sleep(iferror_delay)
		notgood = 0


	


