import unittest
from selenium import webdriver
from CommonModel import Common,TestCaseInfo
from Pages import LoginPage
from selenium.webdriver.chrome.options import Options
import time
from Reports import CreateBug
from CommonModel import screenshot

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.options = Options()
        self.options.add_argument('disable-infobars')
        self.driver = webdriver.Chrome(Common.driverPath(),chrome_options=self.options)
        self.baseurl = Common.baseUrl()
        self.testcaseinfo = TestCaseInfo.TestCaseInfo(id=1, name="LoginTest", owner='luhao')
        #self.testResult = TestReport()
        #LogUtility.CreateLoggerFile("Test_TC_Login")

    def test_login(self):
        try:
            self.testcaseinfo.starttime = Common.getCurrentTime()
            self.driver.get(self.baseurl)
            loginpage = LoginPage.LoginPage(self.driver)
            loginpage.set_username(u"逯浩")
            loginpage.set_password("111111")
            loginpage.click_login()
            time.sleep(1)
            if u'全国学会组织管理信息平台' != loginpage.get_title():
                takephoto = screenshot.ScreenShotUtil(self.driver,filepath='d:',file_name='test_login')
                takephoto.take_screenshot()
                data = Common.zentao_bug_info(u'用户登录失败',u'正确输入用户名密码，点击登录按钮',u'用户登录失败',u'用户登录成功')
                CreateBug.createbug(data)
        except Exception as err:
            self.testcaseinfo.errorinfo = str(err)
            print(self.testcaseinfo.errorinfo)
        finally:
            self.testcaseinfo.endtime = Common.getCurrentTime()
            self.testcaseinfo.secondsDuration = Common.timeDiff(self.testcaseinfo.starttime, self.testcaseinfo.endtime)

    def test_username_wrong(self):
        try:
            self.testcaseinfo.starttime = Common.getCurrentTime()
            self.driver.get(self.baseurl)
            loginpage = LoginPage.LoginPage(self.driver)
            loginpage.set_username("")
            loginpage.set_password("111111")
            loginpage.click_login()
            if loginpage.get_nameerrorinfo() != '请输入用户名':
                data = Common.zentao_bug_info(u'用户名提示信息不正确$TestLogin.test_username_wrong()', u'正确输入密码，点击登录按钮', u'用户提示信息不正确', u'正确显示提示信息')
                CreateBug.createbug(data)
        except Exception as err:
            self.testcaseinfo.errorinfo = str(err)
            print(self.testcaseinfo.errorinfo)
        finally:
            self.testcaseinfo.endtime = Common.getCurrentTime()
            self.testcaseinfo.secondsDuration = Common.timeDiff(self.testcaseinfo.starttime, self.testcaseinfo.endtime)


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(TestLogin("test_login"))
    suite.addTest(TestLogin("test_username_wrong"))
    runner = unittest.TextTestRunner()
    runner.run(suite)