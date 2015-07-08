# encoding:utf-8
import time
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
# 只封装自己独有的一些属性和方法

user_name = {'id': 'reg_email', 'name': 'email'}
user_pwd = {'id': 'reg_password', 'name': 'password'}
login_sub = {'class_name': 'register_but'}
remember_pwd = {
    'id': 'is_remember', 'name': 'is_remember', 'link_text': '记住密码'}
forget_pwd = {'link_text': '忘记密码？'}
register_btn = {'link_text': '注册'}

error_info_login_account = ["请填写邮箱/手机号/昵称", "邮箱/手机号/昵称未注册"]
error_info_login_password = ["请输入密码", "密码由6-16个字符组成"]
error_info_login_password = ["用户名或密码不正确"]

error_info_register_email = ["请填写邮箱", "请填写有效邮箱地址", "邮箱已被注册，您可以 找回密码 或 联系我们"]
error_info_register_nickname = ["请输入昵称", "请填写有效邮箱地址", "邮箱已被注册，您可以 找回密码 或 联系我们"]
error_info_register_password = ["请输入密码", "密码由6-16个字符组成"]
error_info_register_cpassword = ["请输入确认密码", "密码由6-16个字符组成", "两次密码输入不一致"]


# 封装的方法

# 打开ajax登录窗口进行登录
def login_ajax(self):
    '''
    1、输入账号
    2、输入密码
    3、点击登录
    '''
    self.dr.find_element_by_link_text("登录").click()
    self.dr.find_element_by_id(user_name['id']).clear()
    self.dr.find_element_by_id(user_name['id']).send_keys(self.account)
    self.dr.find_element_by_id(user_pwd['id']).clear()
    self.dr.find_element_by_id(user_pwd['id']).send_keys(self.password)
    self.dr.find_element_by_class_name(login_sub['class_name']).click()
    time.sleep(3)


def login_varify_success(self, param):
    '''验证用户登录成功是否，通过判断是否有参加行程权限来判断是否登录成功'''
    # js = "var varify_name = document.getElementByClass('imge');return varify_name"
    # js = "return document.title"
    # center = self.dr.execute_script(js)
    self.assertEqual(self.account, param)


def login_varify_error(self, model):
    if model == 'email':
        error_info = self.dr.find_element_by_id(
            "reg_emailTip").find_element_by_class_name("onError").text
        self.assertEqual(self.varify_message, error_info)
    elif model == 'password':
        error_info = self.dr.find_element_by_id(
            "reg_passwordTip").find_element_by_class_name("onError").text
        self.assertEqual(self.varify_message, error_info)
    elif model == 'email_password':
        error_info_email = self.dr.find_element_by_id(
            "reg_emailTip").find_element_by_class_name("onError").text
        error_info_password = self.dr.find_element_by_id(
            "reg_passwordTip").find_element_by_class_name("onError").text
        error_info = error_info_email + "\n" + error_info_password
        self.assertEqual(self.varify_message, error_info)

