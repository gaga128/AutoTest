# -*- coding: utf-8 -*-
#****************************************************************
# main.py
# Author     : JIA
# Version    : 1.0
# Date       : 2016-05-30
# Description: 造数据
#****************************************************************




paramJson='{appid:444,passwd:"746749378",method:"pushLogToServer",log:{'
# {appid:5510,
# itemid:"text",
# utype:0,
# clientip:"0.0.0.0",
# itemtype:"7",


# paramJson={appid:444,passwd:"746749378",method:"pushLogToServer",log:{appid:5510,itemid:"text",uid:"201",actionid:15,utype:0,clientip:"0.0.0.0",itemtype:"7",actiontime:1457346708,expand_info:[{"expkey":0,"expvalue":"湖南","exptype":0},{"expkey":1,"expvalue":"长沙","exptype":0},{"expkey":2,"expvalue":"未知","exptype":0},{"expkey":18,"expvalue":"","exptype":0},{"expkey":8,"expvalue":"老王","exptype":0}]}}}

import random, datetime
import time
import datalist

dataCount = 10 * 1 * 1  # 10M.




codeRange = range(ord('a'), ord('z'))
alphaRange = [chr(x) for x in codeRange]
alphaMax = len(alphaRange)
def genRandomUid(UidLength):
	global alphaRange, alphaMax
	length = random.randint(UidLength-1, UidLength)
	uid = ''
	for i in range(length):
		uid += alphaRange[random.randint(0, alphaMax - 1)]
	print uid
	return uid


daysMax = 1464624000
daysMin = 1456848000
def genRandomDay():
	global daysMax, daysMin
	actiontime=random.randint(daysMin, daysMax)
	print actiontime
	return actiontime


def genRandomSex():
	Sex=random.randint(0, 1)
	print Sex
	return Sex


def genRandomactionId():
	Actionid=random.choice(datalist.Actionid())
	print Actionid
	return Actionid


# if __name__ == "__main__":
# 	genRandomactionId()
# 	genRandomDay()
# 	genRandomName(10)
# 	genRandomSex()




def genDataBase1(fileName, dataCount):
	outp = open(fileName, 'w')
	i = 0
	while i < dataCount:
		uid = genRandomUid(25)
		actiontime = genRandomDay()
		sex = genRandomSex()
		Actionid=genRandomactionId()
		mLine = "%i  %s %s %s %d\n" % (i + 1, uid,Actionid, actiontime, sex)
		outp.write(mLine)
		i += 1
	outp.close()

if __name__ == "__main__":
	random.seed()
	start = time.time()
	genDataBase1('db_test.txt', dataCount)
	end = time.time()
	print('use time:%d' % (end - start))
	print('Ok')





# expand_info:
# [{"expkey":0,"expvalue":"湖南","exptype":0},
# {"expkey":1,"expvalue":"长沙","exptype":0},
# {"expkey":2,"expvalue":"未知","exptype":0},
# {"expkey":18,"expvalue":"","exptype":0},
# {"expkey":8,"expvalue":"老王","exptype":0}]}}}