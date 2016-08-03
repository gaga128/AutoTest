# -*- coding: utf-8 -*-
#****************************************************************
# getCase.py
# Author     : Jia
# Version    : 1.0
# Date       : 2016-05-17
# Description:
#****************************************************************
import json
import checkPoint
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def acex(AC_result,EX_result):
	actualresult = json.loads(AC_result)  # 改为json格式
	datas = actualresult["datas"]  # 取key对应的value
	flag = actualresult["flag"]
	desc = actualresult["desc"]
	expectresult = json.loads(EX_result)
	Edatas = expectresult["datas"]
	Edesc = expectresult["desc"]
	Eflag = expectresult["flag"]
	finalresult = checkPoint.check_result(datas, Edatas, desc, Edesc, flag, Eflag,'n')
	return finalresult




#########################################################################
if __name__ == '__main__' :
	acex('{"datas":"","desc":"参数错误","flag":3,"usetime":1}','{"datas":"执行失败","desc":"执行成功","flag":200,"usetime":2}')