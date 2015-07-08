#coding=utf-8

import unittest
import time
import HTMLTestRunner
import os
import sys
import re
import multiprocessing
xinyou_path = os.path.dirname(__file__)
action_path = xinyou_path + '\\test_case'+ '\\webapp'+ '\\action'
sys.path.append(action_path)
report_path = xinyou_path + '\\test_case'+ '\\webapp'+ '\\report'	

#筛选测试用例文件，并创建测试套件
def createSuiteList(action_path):
	case_dir = []
	case_list = os.listdir(action_path)
	pattern = re.compile('^(start_){1}\w*.py$')
	for case in case_list:
		match = pattern.match(case)
		if match:
			case_dir.append(case)
	suite = []
	for n in case_dir:
		testunit = unittest.TestSuite()
		#discover方法定义
		discover = unittest.defaultTestLoader.discover(action_path,
			pattern = 'start_*.py',
			top_level_dir= None)
		#discover方法筛选出来的用例，循环添加到测试套件中
		for test_suite in discover:
			for test_case in test_suite:
				testunit.addTests(test_case)
		suite.append(testunit)
	return suite, case_dir

#执行测试套件并生成测试报告
def startRunner(suite, case_dir, report_path):
	#取当前时间：年月日时分秒
	now = time.strftime("%Y%m%d.%H%M%S", time.localtime(time.time()))
	#定义个报告存放路径，支持相对路径。
	filename = report_path+ '\\'+ now+ 'result.html'
	fp = file(filename, 'wb')
	proc_list = []
	for index, item in enumerate(suite):
		print case_dir[index]
		runner = HTMLTestRunner.HTMLTestRunner(
			stream = fp,
			title = str(case_dir[index]) + u'测试报告',
			description = u'测试用例执行情况：')
		proc = multiprocessing.Process(target = runner.run, args = (item,))
		proc_list.append(proc)
	print proc_list
	for proc in proc_list:
		proc.start()
	for proc in proc_list:
		proc.join()


if __name__ == "__main__":
	runtmp = createSuiteList(action_path)
	startRunner(runtmp[0], runtmp[1], report_path)
#暂时有问题不可用