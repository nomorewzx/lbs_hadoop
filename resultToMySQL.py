#-*- coding:utf-8-*-
import MySQLdb
import re
import os
def run():
	os.system('./Mahout.sh')
	f = open('result','r')
	try:
		conn = MySQLdb.connect(host = 'localhost', user = 'root', passwd='123',db='view',charset='utf8')
		cur = conn.cursor()
	except MySQLdb.Error , e:
		print 'MySQL connect error %d:%e' %(e.args[0],e.args[1])
	lines = f.readlines()
	fwrite = open('insert_recommendation','a')
	for line in lines:
		line = str(line)
		#find uid
		reObj = re.compile(r'(.*?)\t')
		uid = reObj.findall(line)
 		uid[0]
 		#find vid and index pairs
 		reView = re.compile(r'[0-9]{3}:[0-9].[0-9]')
		viewIndexPairs = reView.findall(line)
		for viewIndexPair in viewIndexPairs:
			rePairs = re.compile(r':')
			viewInPair = rePairs.sub(',',viewIndexPair)
			record = uid[0] +','+viewInPair
			fwrite.write(record)
			fwrite.write('\n')
	f.close()
	fwrite.close()
	s = "delete from recommendation"
	try:
		cur.execute(s)
	except MySQLdb.Error,e:
		print "delete recommendation error %d:%s"%(e.args[0],e.args[1])
	f = open('insert_recommendation','r')
	lines = f.readlines()
	for line in lines:
		line = line.replace('\n','')
		s = "insert into recommendation values("+line+")"
		try:
			cur.execute(s)
		except MySQLdb.Error,e:
			print"insert error %d:%s" % (e.args[0],e.args[1])
	cur.close()
	conn.close()
	os.system('rm ./result')
	os.system('rm ./insert_recommendation')
	os.system('rm ./scores')
	os.system('rm ./scores.txt')
	print "...complete....."

if __name__ == '__main__':
	run()


