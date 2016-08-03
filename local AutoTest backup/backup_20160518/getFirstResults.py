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
import httpRequests
import json
from xlutils.copy import copy
import os
import writeExcelresult
"""
casepath：传入用例路径
处理excel用例
取得并拼接参数列表
调用封装的http请求
执行用例
"""
def runcase(casepath,sheetname):
	bk = xlrd.open_workbook(casepath)  # 打开excel文件
	httpString = bk.sheet_by_name('Sheet1').cell_value(0, 0)  # 接口url在表1里
	sh = bk.sheet_by_name(sheetname)  # 测试数据在表2里
	nrows = sh.nrows
	ncols = sh.ncols
	runFirstresult=[]
	if sh.cell_value(0,ncols-1)=='Expectresult':
		print 'Expectresult exist!'
		return runFirstresult
	else:
		try:      #拼接参数名与参数值

			for j in range(1,nrows):
				mylist=[]
				myvalue=[]
				for i in range(3,ncols):
					x = sh.cell_value(j,i)          #参数值
					y = sh.cell_value(0,i)          #参数名
					xtype=sh.cell(j,i).ctype
					ytype=sh.cell(0,i).ctype        ######ctype :  0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
					if ytype == 2:
						y = str(int(y))
					if xtype==2 or xtype==4:
						x = str(int(x))
					if x.find(' ')!=-1 or y.find(' ')!=-1:
						x = x.replace(' ','+')
						y = y.replace(' ','+')
					if xtype==4 and x=='1':
						x='True'
					elif ytype==4 and x=='0':
						x='False'
					methods = sh.cell_value(j, 2)
					if methods == 'GET':
						param = y + '=' + x  # 不加双引号
						mylist.append(param)
						params = '&'.join(mylist)  # 拼接成get型
						EX_result = httpRequests.httpRequests(httpString, params, methods)
					else:
						value = '"' + y + '":"' + x + '"'
						myvalue.append(value)
						values = ','.join(myvalue)  # 拼接成post型
						EX_result = httpRequests.httpRequests(httpString, values, methods)
				# print EX_result
				runFirstresult.append(EX_result)
			print runFirstresult
		except Exception,e:
			print e

		return runFirstresult

		writeExcelresult.writenullResult(runFirstresult,resultpath,sheetname)


#########################################################################
if __name__ == '__main__' :
    runFirstresult= runcase(os.getcwd()+r'/mycase/demo.xls','Sheet2')
    writeExcelresult.writeResult(runFirstresult,os.getcwd()+r'/mycase/demo.xls','Sheet2')