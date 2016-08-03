# -*- coding: utf-8 -*-
#****************************************************************
# main.py
# Author     : JIA
# Version    : 1.0
# Date       : 2016-05-17
# Description: 测试组装，用例执行入口
#****************************************************************
import xlrd
import os
import writeExcelresult
import sendReport
import getAutoCasesResults
import getCasesResults

#接口测试
#设置测试用例
casepath = os.getcwd()+r'/mycase/demo.xls'
# print casepath
resultpath=os.getcwd()+r'/mycase/demo.xls'
casesheet='Sheet2'
caseresult='CaRe'
Autocasesheet='Default parameter'
Autocaseresult='AutoCaRe'
Speparamlist=['']

bk = xlrd.open_workbook(resultpath)
sh = bk.sheet_by_name(casesheet)
ncols = sh.ncols

#testsuite begin
def run():
	runFirstresult =getCasesResults.runcase(casepath, casesheet, caseresult)
	writeExcelresult.writeResult(runFirstresult, casepath,caseresult)

	runFirstnullresult = getAutoCasesResults.createcase(casepath, Autocasesheet, Autocaseresult, Speparamlist)
	writeExcelresult.writeResult(runFirstnullresult,casepath, Autocaseresult)


def email():
    sendReport.sendEmail()


if __name__ == '__main__':
    run()
    email()