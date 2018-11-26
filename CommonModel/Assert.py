import unittest
from CommonModel import screenshot,Common
def Assert(getinfo,expectedresult,buginfo,bugstate=None):
    if expectedresult != getinfo and bugstate == None:
        takephoto = screenshot.ScreenShotUtil(self.driver, filepath='d:', file_name='test_login')
        takephoto.take_screenshot()
        data = Common.zentao_bug_info(u'用户登录失败', u'正确输入用户名密码，点击登录按钮', u'用户登录失败', u'用户登录成功')
        #CreateBug.createbug(data)