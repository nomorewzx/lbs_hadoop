#-*- coding:utf-8 -*-
import MySQLdb
import re
import resultToMySQL
__author__ = 'WangZhenXuan'
if __name__ == '__main__':
	f = open('scores.txt','a')
	try:
		conn = MySQLdb.connect(host = 'localhost', user = 'root', passwd ='123', db = 'view', charset='utf8')
		cur = conn.cursor()
		query = 'select * from score'
		cur.execute(query)
		scores = cur.fetchall()
		cur.close()
		conn.close()
	except MySQLdb.Error,e:
		 print "Mysql Error %d: %s" % (e.args[0], e.args[1])
	for score in scores:
		f.write(str(score))
		f.write('\n')
	f.close()
	# delete quotes, brackets and commas
	f = open('scores.txt','r')
	files = open('scores','a')
	reObj = re.compile(r'\'|u|\(|\)|\s')
	scoresFile = f.readlines()
	for line in scoresFile:
		line = reObj.sub('',line)
		files.write(line)
		files.write('\n')
	f.close()
	files.close()
###################run next step
	resultToMySQL.run()
	

	
