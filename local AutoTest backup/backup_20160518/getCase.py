# -*- coding: utf-8 -*-
#****************************************************************
# getCase.py
# Author     : hsn
# Version    : 1.0
# Date       : 2016-04-20
# Description:
#****************************************************************
import xlrd
##import xlwt
##from xlutils.copy import copy
import httpRequests
import checkPoint
import json
import writeLog
import FileOperation
"""
casepath：传入用例路径
处理excel用例
取得并拼接参数列表
调用封装的http请求
执行用例
"""
def runcase(casepath):
    bk = xlrd.open_workbook(casepath) # 打开excel文件
    httpString = bk.sheet_by_name('Sheet1').cell_value(0,0)#接口url在表1里
    sh = bk.sheet_by_name('Sheet2')#测试数据在表2里
    nrows = sh.nrows
    ncols = sh.ncols
    FileOperation.DelFile(r'./log/failresult.html')
    try:
        #拼接参数名与参数值
        for j in range(1,nrows):
            mylist=[]
            myvalue=[]
            for i in range(3,ncols-1):
                x = sh.cell_value(j,i)          #参数值
                y = sh.cell_value(0,i)          #参数名
                if isinstance(x,float):
                    x = str(int(x))
                if isinstance(x,float):
                    y = str(int(y))
                if x == True:
                    x = 'TRUE'
                if x == False:
                    x = 'FALSE'
                if x.find(' ')!=-1:
                    x = x.replace(' ','+')
                if y.find(' ')!=-1:
                    y = y.replace(' ','+')
                #param = '"'+y+'"'+'='+'"'+x+'"'#加双引号
                param = y+'='+x                 #不加双引号
                mylist.append(param)
                s = '&'
                params = s.join(mylist)         #拼接成get型
                value = '"'+y+'":"'+x+'"'
                myvalue.append(value)
                values = ','.join(myvalue)      #拼接成post型
            #print params
            #print values
            num = sh.cell_value(j,0)
            num = str(int(num))
            name = sh.cell_value(j,1)
            name = str(name)
            EX_result=sh.cell_value(j,ncols-1)
            expectresult = json.loads(EX_result)
            Edatas = expectresult["datas"]
            Edesc = expectresult["desc"]
            Eflag = expectresult["flag"]
            methods = sh.cell_value(j,2)
            if methods == 'GET':
                AC_result = httpRequests.httpRequests(httpString,params,methods)
            else:
                AC_result = httpRequests.httpRequests(httpString,values,methods)
            actualresult = json.loads(AC_result)#改为json格式
            datas = actualresult["datas"]#取key对应的value
            flag = actualresult["flag"]
            desc = actualresult["desc"]
            url = httpRequests.URLreturn(httpString,params)
            #print url
            finalresult = checkPoint.check_result(datas,Edatas,desc,Edesc,flag,Eflag,name)
            if finalresult == False:
                writeLog.errorlog('FAIL:wrong datas case is number:'+num+':'+name,url)

    except Exception,e:
        print e

#########################################################################
if __name__ == '__main__' :
    runcase(r'F:\AutoTest\mycase\demo.xls')



