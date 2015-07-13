# coding=utf-8

import unittest
import HTMLTestRunner
import logging
import logging.config
import os
import time
import sys
import re
apps_path = os.path.dirname(__file__)
action_path = apps_path + "\\" + "action"
conf_path = apps_path + "\\" + "conf"
sys.path.append(action_path)
report_path = apps_path + "\\" + "report"


# 筛选测试用例文件，并创建测试套件
def createSuiteList(subpath, childpath):
    case_lists = []  # 目录下有效测试用例列表
    flists = os.listdir(childpath)  # 目录下所有文件列表
    # main_logger.info(childpath + "目录下所有文件列表为：" + str(flists))
    pattern = re.compile('^(start_){1}\w*.py$')
    for fname in flists:
        match = pattern.match(fname)
        if match:
            case_lists.append(fname)
    # main_logger.info(childpath + "目录下有效测试用例文件列表为：" + str(case_lists))
    suite_lists = []
    for case in case_lists:
        test_unit = unittest.TestSuite()
        # discover方法定义
        discovers = unittest.defaultTestLoader.discover(
            childpath, pattern='start_*.py', top_level_dir=subpath)
        # discover方法筛选出来的用例，循环添加到测试套件中
        for test_suite in discovers:
            test_unit.addTests(test_suite)
    suite_lists.append(test_unit)
    # main_logger.info(childpath + "目录下筛选出的测试套件列表为：" + str(suite_lists))
    return suite_lists, case_lists


# 执行测试套件并生成测试报告
def startRunner(suite_lists, case_lists, report_path):
    # 取当前时间：年月日时分秒
    now = time.strftime("%Y%m%d.%H%M%S", time.localtime(time.time()))
    # 定义个报告存放路径，支持相对路径。
    filename = report_path + '\\' + now + 'result.html'
    fp = file(filename, 'wb')
    for index, item in enumerate(suite_lists):
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title=str(case_lists[index]) + u'测试报告',
            description=u'测试用例执行情况：')
        runner.run(item)


if __name__ == "__main__":
    # config_log = conf_path + "\\" + "logging.conf"
    # logging.config.fileConfig(config_log)
    # main_logger = logging.getLogger('main')
    subpath = action_path
    childpath = subpath + "\\" + "login"
    suite_lists, case_lists = createSuiteList(subpath, childpath)
    startRunner(suite_lists, case_lists, report_path)
