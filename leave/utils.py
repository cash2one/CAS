#coding:utf8
import sys, urllib, urllib2, json
import requests
import logging
import time
import datetime

errlog = logging.getLogger('daserr')
#apis.baidu.com

api_res = {u'20170630': u'0', u'20170730': u'1', u'20170731': u'0', u'20161208': u'0', u'20161209': u'0', u'20161206': u'0', u'20161207': u'0', u'20161204': u'1', u'20161205': u'0', u'20161202': u'0', u'20161203': u'1', u'20161201': u'0', u'20171226': u'0', u'20171018': u'0', u'20171019': u'0', u'20171016': u'0', u'20171017': u'0', u'20170831': u'0', u'20171015': u'1', u'20171012': u'0', u'20171013': u'0', u'20171010': u'0', u'20171011': u'0', u'20171202': u'1', u'20171201': u'0', u'20170402': u'1', u'20170403': u'0', u'20171206': u'0', u'20170401': u'1', u'20170406': u'0', u'20170407': u'0', u'20170404': u'0', u'20170405': u'0', u'20171207': u'0', u'20170408': u'1', u'20170409': u'1', u'20170311': u'1', u'20170929': u'0', u'20170928': u'0', u'20170925': u'0', u'20170924': u'1', u'20170927': u'0', u'20170926': u'0', u'20170921': u'0', u'20170920': u'0', u'20170923': u'1', u'20170922': u'0', u'20170119': u'0', u'20170716': u'1', u'20170205': u'1', u'20170206': u'0', u'20170207': u'0', u'20170712': u'0', u'20170713': u'0', u'20170710': u'0', u'20170711': u'0', u'20170208': u'0', u'20170209': u'0', u'20170718': u'0', u'20170719': u'0', u'20170811': u'0', u'20170810': u'0', u'20170813': u'1', u'20170812': u'1', u'20170815': u'0', u'20170814': u'0', u'20170817': u'0', u'20170816': u'0', u'20170819': u'1', u'20170818': u'0', u'20170302': u'0', u'20171219': u'0', u'20161129': u'0', u'20161128': u'0', u'20170518': u'0', u'20170519': u'0', u'20170708': u'1', u'20170510': u'0', u'20170511': u'0', u'20170512': u'0', u'20170513': u'1', u'20170514': u'1', u'20170515': u'0', u'20170516': u'0', u'20170517': u'0', u'20171108': u'0', u'20171109': u'0', u'20170527': u'1', u'20171101': u'0', u'20171102': u'0', u'20171103': u'0', u'20171104': u'1', u'20171105': u'1', u'20171106': u'0', u'20171107': u'0', u'20161130': u'0', u'20170109': u'0', u'20170108': u'1', u'20170107': u'1', u'20170106': u'0', u'20170105': u'0', u'20170104': u'0', u'20170103': u'0', u'20170102': u'0', u'20170101': u'1', u'20170228': u'0', u'20170222': u'0', u'20170223': u'0', u'20170220': u'0', u'20170221': u'0', u'20170226': u'1', u'20170227': u'0', u'20170224': u'0', u'20170225': u'1', u'20170529': u'0', u'20161228': u'0', u'20171014': u'1', u'20171203': u'1', u'20170601': u'0', u'20170602': u'0', u'20170830': u'0', u'20170604': u'1', u'20170605': u'0', u'20170606': u'0', u'20170607': u'0', u'20170608': u'0', u'20170609': u'0', u'20171209': u'1', u'20171208': u'0', u'20170530': u'0', u'20170531': u'0', u'20171128': u'0', u'20171129': u'0', u'20171126': u'1', u'20171127': u'0', u'20171124': u'0', u'20171125': u'1', u'20171122': u'0', u'20171123': u'0', u'20171120': u'0', u'20171121': u'0', u'20170125': u'0', u'20170124': u'0', u'20170127': u'0', u'20170126': u'0', u'20170121': u'1', u'20170120': u'0', u'20170123': u'0', u'20170122': u'1', u'20170129': u'1', u'20170128': u'1', u'20170327': u'0', u'20170326': u'1', u'20170325': u'1', u'20170324': u'0', u'20170323': u'0', u'20170322': u'0', u'20170321': u'0', u'20170320': u'0', u'20170329': u'0', u'20170328': u'0', u'20170914': u'0', u'20170915': u'0', u'20170916': u'1', u'20170917': u'1', u'20170910': u'1', u'20170911': u'0', u'20170912': u'0', u'20170913': u'0', u'20170918': u'0', u'20170919': u'0', u'20170521': u'1', u'20170520': u'1', u'20170523': u'0', u'20170619': u'0', u'20171229': u'0', u'20171228': u'0', u'20170610': u'1', u'20171221': u'0', u'20170525': u'0', u'20171223': u'1', u'20171222': u'0', u'20171225': u'0', u'20171224': u'1', u'20171227': u'0', u'20170616': u'0', u'20170626': u'0', u'20170627': u'0', u'20170624': u'1', u'20170625': u'1', u'20170622': u'0', u'20170623': u'0', u'20170620': u'0', u'20170621': u'0', u'20161229': u'0', u'20161231': u'1', u'20170614': u'0', u'20170628': u'0', u'20170629': u'0', u'20170828': u'0', u'20170829': u'0', u'20171029': u'1', u'20171028': u'1', u'20161221': u'0', u'20171023': u'0', u'20171022': u'1', u'20171021': u'1', u'20171020': u'0', u'20171027': u'0', u'20170825': u'0', u'20171025': u'0', u'20171024': u'0', u'20161223': u'0', u'20171205': u'0', u'20170309': u'0', u'20170308': u'0', u'20170305': u'1', u'20170304': u'1', u'20170307': u'0', u'20170306': u'0', u'20170301': u'0', u'20170303': u'0', u'20170430': u'1', u'20171204': u'0', u'20170930': u'1', u'20161211': u'1', u'20170722': u'1', u'20161213': u'0', u'20171220': u'0', u'20161212': u'0', u'20170727': u'0', u'20170726': u'0', u'20170723': u'1', u'20161210': u'1', u'20170721': u'0', u'20170720': u'0', u'20161215': u'0', u'20161214': u'0', u'20161217': u'1', u'20161216': u'0', u'20161219': u'0', u'20161218': u'1', u'20170729': u'1', u'20170724': u'0', u'20171001': u'1', u'20171003': u'0', u'20171002': u'0', u'20171005': u'0', u'20171004': u'0', u'20171007': u'1', u'20170809': u'0', u'20171009': u'0', u'20170807': u'0', u'20170804': u'0', u'20170805': u'1', u'20170802': u'0', u'20170803': u'0', u'20170801': u'0', u'20170728': u'0', u'20170725': u'0', u'20170415': u'1', u'20170414': u'0', u'20170417': u'0', u'20170416': u'1', u'20170411': u'0', u'20170410': u'0', u'20170413': u'0', u'20170412': u'0', u'20170419': u'0', u'20170418': u'0', u'20170118': u'0', u'20170808': u'0', u'20171211': u'0', u'20170114': u'1', u'20170115': u'1', u'20170116': u'0', u'20170117': u'0', u'20170110': u'0', u'20170111': u'0', u'20170112': u'0', u'20170113': u'0', u'20170709': u'1', u'20170806': u'1', u'20171213': u'0', u'20171008': u'1', u'20170701': u'1', u'20170703': u'0', u'20170702': u'1', u'20170705': u'0', u'20170704': u'0', u'20170707': u'0', u'20170706': u'0', u'20170217': u'0', u'20170216': u'0', u'20170215': u'0', u'20170214': u'0', u'20170213': u'0', u'20170212': u'1', u'20170211': u'1', u'20170210': u'0', u'20170219': u'1', u'20170218': u'1', u'20171218': u'0', u'20170319': u'1', u'20171212': u'0', u'20170424': u'0', u'20170425': u'0', u'20170426': u'0', u'20171210': u'1', u'20170822': u'0', u'20170509': u'0', u'20170508': u'0', u'20171214': u'0', u'20171215': u'0', u'20171216': u'1', u'20171217': u'1', u'20170503': u'0', u'20170502': u'0', u'20170501': u'0', u'20170507': u'1', u'20170506': u'1', u'20170505': u'0', u'20170504': u'0', u'20171119': u'1', u'20171118': u'1', u'20170422': u'1', u'20171113': u'0', u'20171112': u'1', u'20171111': u'1', u'20170315': u'0', u'20171117': u'0', u'20171116': u'0', u'20171115': u'0', u'20171114': u'0', u'20170130': u'0', u'20170131': u'0', u'20170420': u'0', u'20171110': u'0', u'20170330': u'0', u'20170331': u'0', u'20171006': u'0', u'20170421': u'0', u'20170603': u'1', u'20170423': u'1', u'20161230': u'0', u'20171230': u'1', u'20170826': u'1', u'20170613': u'0', u'20170612': u'0', u'20170611': u'1', u'20170522': u'0', u'20170617': u'1', u'20170524': u'0', u'20170615': u'0', u'20170526': u'0', u'20161220': u'0', u'20170528': u'1', u'20161222': u'0', u'20170618': u'1', u'20161224': u'1', u'20161225': u'1', u'20161226': u'0', u'20161227': u'0', u'20171130': u'0', u'20171030': u'0', u'20171031': u'0', u'20170204': u'1', u'20170717': u'0', u'20170714': u'0', u'20170820': u'1', u'20170318': u'1', u'20170715': u'1', u'20170428': u'0', u'20170429': u'1', u'20170821': u'0', u'20170312': u'1', u'20170313': u'0', u'20170310': u'0', u'20170427': u'0', u'20170316': u'0', u'20170317': u'0', u'20170314': u'0', u'20170201': u'0', u'20170823': u'0', u'20170202': u'0', u'20170824': u'0', u'20170203': u'0', u'20171026': u'0', u'20170907': u'0', u'20170906': u'0', u'20170905': u'0', u'20170904': u'0', u'20170903': u'1', u'20170902': u'1', u'20170901': u'0', u'20170827': u'1', u'20170909': u'1', u'20170908': u'0'}


def getHoliday(info):
	url = 'http://apis.baidu.com/xiaogg/holiday/holiday?d=%s'%(info)
	headers = {"apikey":"a6cd14b29a20112d02350a133be393f0"}
	content = None
	for i in range(10):
		try:
			r = requests.get(url, headers=headers)
			content = r.text
			if type(json.loads(content)) == type(1):
				content = json.dumps({info:str(content)})
			elif type(json.loads(content)) == type({'a':1}):
				pass
			else:
				content = None
		except Exception, e:
			time.sleep(0.2)
		if content:
			break
	else:
		errlog.error('百度API异常,无法获取数据')
	return content




def getlocalres(info):
	print info
	info_list = info.split(',')
	res = {}
	for key in info_list:
		res.update({key:api_res[key]})
	return res



def getMonth(year, month, start_day, end_day, half=1):
	month_execpt_weekend = []
	month_apply_day = 0
	res = {}
	if month < 10:
		year_month = str(year) + '0' + str(month)
	else:
		year_month = str(year) + str(month)

	info = ''
	if start_day == end_day:
		if start_day < 10:
			info = info + year_month + '0' + str(start_day) + ','
		else:
			info = info + year_month + str(start_day) + ','
	for day in  range(start_day, end_day+1):
		if day < 10:
			info = info + year_month + '0' + str(day) + ','
		else:
			info = info + year_month + str(day) + ','
	info = info.strip(',')

	#result_json = getHoliday(info)
	#result = json.loads(result_json)
	result = getlocalres(info)
	for k,v in result.items():
		if v == '0':
			month_apply_day = month_apply_day + 1
	if half == 0:
		month_apply_day = month_apply_day - 0.5
	res.update({'year_month': year_month, 'month_apply_day': month_apply_day})
	print res, 'result'
	return res


def getMonthadd(year, month, start_day, end_day, half=1):
	month_execpt_weekend = []
	month_add_day = 0
	res = {}
	if month < 10:
		year_month = str(year) + '0' + str(month)
	else:
		year_month = str(year) + str(month)

	info = ''
	if start_day == end_day:
		if start_day < 10:
			info = info + year_month + '0' + str(start_day) + ','
		else:
			info = info + year_month + str(start_day) + ','
	for day in  range(start_day, end_day+1):
		if day < 10:
			info = info + year_month + '0' + str(day) + ','
		else:
			info = info + year_month + str(day) + ','
	info = info.strip(',')

	# result_json = getHoliday(info)
	# result = json.loads(result_json)
	result = getlocalres(info)

	for k,v in result.items():
		if v != '0':
			month_add_day = month_add_day + 1
	if half == 0:
		month_add_day = month_add_day - 0.5
	res.update({'year_month': year_month, 'month_add_day': month_add_day})
	return res



if __name__ == "__main__":

	now = datetime.datetime(2016, 11, 28)
	result = {}
	while True:
		date = now.strftime('%Y%m%d')
		print date
		if date == '20171231':
			break
		res = json.loads(getHoliday(date))
		result.update(res)
		print result
		now = now + datetime.timedelta(days=1)
		print now