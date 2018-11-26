from datetime import datetime
import requests

def driverPath():
    return r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe'


def baseUrl():
    return "http://180.76.135.105/srpweb/userLogin.html"

def zentaoUrl():
    return 'http://127.0.0.1/zentao/'

# 返回Apache用户访问验证
def zentaoauth():
    return ('zentao', 'akx7R0q6oUk')

# change time to str
def getCurrentTime():
    format = "%a %b %d %H:%M:%S %Y"
    return datetime.now().strftime(format)


# Get time diff
def timeDiff(starttime, endtime):
    format = "%a %b %d %H:%M:%S %Y"
    return datetime.strptime(endtime, format) - datetime.strptime(starttime, format)

def zentao_bug_info(bugtitle,bugsteps,result,expectinfo):
    data = {'title': bugtitle, 'steps': '< p > [步骤] < /p > '+ bugsteps +' < br / > < p > [结果] < /p > '+result+'< br / > < p > [期望] < /p > '+expectinfo}
    return data

def getzentaosid():
    getsessionurl = "?m=api&f=getSessionID&t=json"
    sessioninfo = requests.get(zentaoUrl() + getsessionurl, auth=zentaoauth())
    return sessioninfo.cookies['zentaosid']

def getloginsid():
    loginurl = "?m=user&f=login&t=json&sid=%s&account=%s&password=%s"
    logininfo = requests.post(zentaoUrl()+loginurl %(getzentaosid(),'admin','LU123hao'), auth=zentaoauth())
    print(logininfo.url)
    return logininfo.cookies['zentaosid']


def zentao_sid():
    sid = 'hs7igcblmdff0uqvj1865ja9q5'
    return sid