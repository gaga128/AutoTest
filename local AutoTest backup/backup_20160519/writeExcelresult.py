# -*- coding: utf-8 -*-
#****************************************************************
# getCase.py
# Author     : Jia
# Version    : 1.0
# Date       : 2016-05-06
# Description:
#****************************************************************
import xlrd
import xlutils
from xlutils.copy import copy
import os


######################写入NULL的请求结果########################################
def writeResult(runFirstnullresult,resultpath,sheetname):
	oldE=xlrd.open_workbook(resultpath,formatting_info=True)   ###保存之前数据的格式
	if sheetname in oldE.sheet_names():                    ####给出sheetname列表
		print 'Expected results exist!'
	else:
		newE=copy(oldE)
		nwr=newE.add_sheet(sheetname, cell_overwrite_ok=True)  ##新增一个sheet1，第二参数用于确认同一个cell单元是否可以重设值。
		i=1
		j=1
		for line1 in runFirstnullresult[::2]:
			nwr.write(i, 2, line1)
			nwr.write(i, 1, 'TestCase%s' % i)
			nwr.write(i, 0, '%s' % i)
			i = i + 1

		for line1 in runFirstnullresult[1::2]:
			nwr.write(j, 3, line1)
			j = j + 1
		nwr.write(0, 3, 'Expectresult')
		nwr.write(0, 2, 'URL')
		nwr.write(0, 1, 'TestcaseName')
		nwr.write(0, 0, 'ID')
		print 'EX_result save successfully!'
		newE.save(resultpath)




####################################在测试用例后写入结果################################
def writexistseResult(runFirstresult,resultpath,sheetname):
	oldE=xlrd.open_workbook(resultpath,formatting_info=True)   ###保存之前数据的格式
	newE=copy(oldE,)
	nwr=newE.get_sheet(1)
	sh = oldE.sheet_by_name(sheetname)
	ncols = sh.ncols
	if runFirstresult==[]:
		return None
	else:
		i=1
    	for line in runFirstresult:
			nwr.write(i,ncols,line)
        		i = i + 1
    	nwr.write(0,ncols,'Expectresult')
    	newE.save(resultpath)
