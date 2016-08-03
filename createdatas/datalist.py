# -*- coding: utf-8 -*-
#****************************************************************
# main.py
# Author     : JIA
# Version    : 1.0
# Date       : 2016-05-30
# Description: 造数据
#****************************************************************
import json

def Actionid():
	# actionlist={'ACTION_ACCESS ':'0','ACTION_BUG':'1','ACTION_ADD':'2','ACTION_DEL':'3','ACTION_EXCHANGE':'4','ACTION_REG':'5','ACTION_CLICK':'6','ACTION_SCAN':'7','ACTION_SHARE':'8','ACTION_COLLECT':'9','ACTION_MOD':'10','ACTION_SEARCH':'11','ACTION_SORT':'12','ACTION_REMOVE':'13','ACTION_LOOK':'14','ACTION_UP':'15','ACTION_DOUM':'16','ACTION_SUBSCRIBE':'17','ACTION_BINDING':'18','ACTION_CONVERT':'19'}
	actionlist ={'访问':'0','购买':'1','添加':'2','删除':'3','换购':'4','注册':'5','点击':'6','扫描':'7','分享':'8','收藏':'9','修改':'10','搜索':'11','排序':'12','退货':'13','查看':'14','上行':'15','下行':'16','关注':'17','绑定':'18','兑换':'19'}
	actionlists=json.dumps(actionlist)
	# print actionlist.values()
	# print actionlists
	return actionlist.values()


def expand_info():
	expand_info={'EXP_PROVINCE':'0','EXP_CITY':'1','EXP_GENDER':'2','EXP_AGE':'3','EXP_USERAGENT':'4','EXP_SYSTEM':'5','EXP_USER_MOBILE':'6','EXP_USER_SHARE':'7','EXP_USER_SOURCE':'8','EXP_USER_MAIL':'9','EXP_USER_QQ':'10','EXP_USER_NICKNAME':'11','EXP_OTHER_PLATFORM':'12','EXP_INTEGRAL':'13','EXP_LEVEL':'14','EXP_LOCATION_X_Y':'15','EXP_MULTIPLE_VALUE':'16','EXP_SCORE':'17','EXP_TEXT_CONTENT':'18'}
	# expand_info = {'省份':'0','城市':'1','性别':'2','年龄':'3','浏览器':'4','用户系统':'5','用户手机号':'6','分享者':'7','用户来源':'8','邮箱':'9','QQ':'10','用户呢称':'11','其他平台':'12','积分':'13','等级':'14','经纬度':'15','用户状态多值2进制转10进制结果':'16','分值变化':'17','文本内容':'18'}
	expand_infos = json.dumps(expand_info)
	# print expand_infos
	return expand_info.values()

def itemtype():
	# itemtype ={'ITEM_PRODUCT':'0','ITEM_MENU':'1','ITEM_BUTTON':'2','ITEM_PAGE':'3','ITEM_QR':'4','ITEM_ORDER':'5','ITEM_MEESSAGE':'6','ITEM_ACTIVITY':'7'}
	itemtype ={u'产品、商品':'0',u'菜单':'1',u'按钮':'2',u'页面':'3',u'二维码':'4',u'订单':'5',u'消息':'6',u'活动':'7'}
	itemtypes = json.dumps(itemtype)
	# print itemtypes
	return itemtype.values()
def utype():
	# utype={'USER_WEIBO':'0','USER_WEIXIN':'1','USER_PC_WEBSITE':'2','USER_WAP_WEBSITE':'3','USER_MEMBER ':'4'}
	utype={'微博用户':'0','微信用户':'1','pc页面用户':'2','wap页面用户':'3','客户会员':'4'}
	utypes = json.dumps(utype)
	# print utypes
	return utype.values()


if __name__ == "__main__":
	Actionid()
	expand_info()
	itemtype()
	utype()