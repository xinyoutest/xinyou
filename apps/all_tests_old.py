# coding=utf-8

import unittest
import time
import HTMLTestRunner
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import re
sys.path.append(os.path.dirname(__file__) + '\\action')
from object_db import *


def test(action_path):
    case_list = os.listdir(action_path)
    pattern = re.compile('^(start_){1}\w*.py$')
    for dirname in case_list:
        page_dir = action_path + "\\" + dirname
        if os.path.isdir(page_dir):
            test_dir = []
            case_s = os.listdir(page_dir)
            for case in case_s:
                match = pattern.match(case)
                if match:
                    test_dir.append(case)
            createSuiteList(page_dir)

# 筛选测试用例文件，并创建测试套件


def createSuiteList(action_path, report_name, top_level_dir):
    case_dir = []
    case_list = os.listdir(action_path)
    pattern = re.compile('^(start_){1}\w*.py$')
    for case in case_list:
        match = pattern.match(case)
        if match:
            case_dir.append(case)
    for n in case_dir:
        testunit = unittest.TestSuite()
        # discover方法定义
        discover = unittest.defaultTestLoader.discover(action_path,
                                                       pattern='start_*.py',
                                                       top_level_dir=top_level_dir)
        # discover方法筛选出来的用例，循环添加到测试套件中
        for test_suite in discover:
            for test_case in test_suite:
                testunit.addTests(test_case)
                # sys.exit()
    return testunit, case_dir, report_name

# 执行测试套件并生成测试报告


def startRunner(suite, case_dir, report_path, report_name):
    # 取当前时间：年月日时分秒
    # now = time.strftime("%Y%m%d.%H%M%S", time.localtime(time.time()))
    # 定义个报告存放路径，支持相对路径。
    filename = report_path + '\\' + str(report_name) + '_result.html'
    fp = file(filename, 'wb')
    for item in suite:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title=str(item) + u'测试报告',
            description=u'测试用例执行情况：')
        runner.run(item)


if __name__ == "__main__":
    case_list = os.listdir(action_path)
    for dirname in case_list:
        page_dir = action_path + "\\" + dirname
        if os.path.isdir(page_dir):
            report_name = os.path.basename(page_dir)
            top_level_dir = os.path.dirname(page_dir)
            runtmp = createSuiteList(page_dir, report_name, top_level_dir)
            startRunner(runtmp[0], runtmp[1], report_path, report_name)
