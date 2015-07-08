# coding=utf-8

from selenium import webdriver
import unittest
import sys
import os
reload(sys)
sys.setdefaultencoding("utf-8")
action_path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(action_path)
from object_db import model_path
sys.path.append(model_path)
from object_db import chrome
from object_db import set_implicitly_wait
from object_db import set_page_toload_timeout
from object_db import start_Browser
from object_db import getExecl
from object_db import save_error_image
from object_db import getCookie
from login_model import login_ajax
from login_model import login_varify_success
from login_model import login_varify_error
import inspect

class Login(unittest.TestCase):

    def setUp(self):
        self.dr = chrome()
        # 设置智能等待时间
        set_implicitly_wait(self, 60)
        # 设置页面加载等待时间
        set_page_toload_timeout(self, 60)
        "%s.%s invoked"%(self.__class__.__name__, get_current_function_name())
        sys.exit()

    def tearDown(self):
        self.dr.quit()

    # 酷鸟登录用例
    def test_login_0001(self):
        u"""验证正确的【邮箱】和正确的【密码】，可以登录（ajax）"""
        self.url = getExecl('login', 4, 2)
        self.account = getExecl('login', 5, 2)
        self.password = getExecl('login', 6, 2)
        start_Browser(self)
        login_ajax(self)
        cookie_user = getCookie(self, "last_login_emial")
        login_varify_success(self, cookie_user)
        self.dr.close()

    # 酷鸟登录用例
    def test_login_0002(self):
        u"""验证错误的【邮箱】和正确的【密码】，不可以登录（ajax）"""
        self.url = getExecl('login', 4, 3)
        self.account = getExecl('login', 5, 3)
        self.password = getExecl('login', 6, 3)
        self.varify_message = getExecl('login', 7, 3)
        start_Browser(self)
        login_ajax(self)
        login_varify_error(self, "email_password")
        self.error_image_name = __file__.split('\\')[-1].split('.')[0]
        save_error_image(self)
        self.dr.close()

    # 酷鸟登录用例
    def test_login_0003(self):
        u"""验证正确的【邮箱】和错误的【密码】，不可以登录（ajax）"""
        self.url = getExecl('login', 4, 4)
        self.account = getExecl('login', 5, 4)
        self.password = getExecl('login', 6, 4)
        self.varify_message = getExecl('login', 7, 4)
        start_Browser(self)
        login_ajax(self)
        login_varify_error(self, "password")
        self.error_image_name = __file__.split('\\')[-1].split('.')[0]
        save_error_image(self)
        self.dr.close()

    # 酷鸟登录用例
    def test_login_0004(self):
        u"""验证正确的【昵称】和正确的【密码】，可以正常登录（ajax）"""
        self.url = getExecl('login', 4, 5)
        self.account = getExecl('login', 5, 5)
        self.password = getExecl('login', 6, 5)
        self.varify_message = getExecl('login', 7, 5)
        start_Browser(self)
        login_ajax(self)
        cookie_user = getCookie(self, "last_login_emial")
        login_varify_success(self, cookie_user)
        self.dr.close()

    # 酷鸟登录用例
    def test_login_0005(self):
        u"""验证错误的【昵称】和正确的【密码】不可以正常登录（ajax）"""
        self.url = getExecl('login', 4, 6)
        self.account = getExecl('login', 5, 6)
        self.password = getExecl('login', 6, 6)
        self.varify_message = getExecl('login', 7, 6)
        start_Browser(self)
        login_ajax(self)
        login_varify_error(self, "email_password")
        self.error_image_name = __file__.split('\\')[-1].split('.')[0]
        save_error_image(self)
        self.dr.close()

    # 酷鸟登录用例
    def test_login_0006(self):
        u"""验证正确的【昵称】错误的【密码】不可以正常登录（ajax）"""
        self.url = getExecl('login', 4, 7)
        self.account = getExecl('login', 5, 7)
        self.password = getExecl('login', 6, 7)
        self.varify_message = getExecl('login', 7, 7)
        start_Browser(self)
        login_ajax(self)
        login_varify_error(self, "password")
        self.error_image_name = __file__.split('\\')[-1].split('.')[0]
        save_error_image(self)
        self.dr.close()


if __name__ == "__main__":
    unittest.main()
