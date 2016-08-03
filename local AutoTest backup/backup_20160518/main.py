# -*- coding: utf-8 -*-
#****************************************************************
# main.py
# Author     : JIA
# Version    : 1.0
# Date       : 2016-05-17
# Description: 测试组装，用例执行入口
#****************************************************************
import xlrd
import sys,os
import getCase
import getFirstResults
import getAutoCaRe
import writeExcelresult
import sendReport


#接口测试
#设置测试用例
casepath = os.getcwd()+r'/mycase/demo.xls'
# print casepath
resultpath=os.getcwd()+r'/mycase/demo.xls'
sheetname1='Sheet2'
defaultname='Default parameter'
resultname='AutoCaRe'
Speparamlist=['', '!', '@', '&', '#', ',', ' ']
bk = xlrd.open_workbook(resultpath)
sh = bk.sheet_by_name(sheetname1)
ncols = sh.ncols

#testsuite begin
def run():
    if sh.cell_value(0, ncols-1)=='Expectresult':
		getCase.runcase(casepath)

    else:
		runFirstresult = getFirstResults.runcase(casepath,sheetname1)
		writeExcelresult.writeResult(runFirstresult,resultpath,sheetname1)

def runnull():
	if resultname in bk.sheet_names():
		getAutoCaRe.crcase(casepath,defaultname,resultname)
	else:
		runFirstnullresult = getAutoCaRe.createcase(casepath, defaultname, resultname, Speparamlist)
		writeExcelresult.writenullResult(runFirstnullresult, casepath, resultname)

def email():
    sendReport.sendEmail()


if __name__ == '__main__':
    run()
    email()
    #runnull()