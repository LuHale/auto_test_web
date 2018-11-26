import requests
from CommonModel import Common

zentaourl = Common.zentaoUrl()

def createbug(bugdata,productid=1,branch=0,project=0,module=0,openedBuild='trunk',assignedTo='admin',severity=3,pri=3):
    createbugurl = 'bug-create-%s-%s-moduleID=%s.json?zentaosid=%s&t=json'
    data = {
        'product': productid,    # 产品id
        'branch': branch,     # 平台id
        'project': project,    # 项目id
        'module': module,
        'openedBuild[]': openedBuild,    # 影响版本
        'assignedTo': assignedTo,    # 指派人
        'severity': severity,    # 级别
        'pri': pri,    # 优先级
        'deadline':Common.getCurrentTime(),    # 解决时间
        'title': bugdata['title'],    # 标题
        'steps': bugdata['steps']}

    # 登录时sid会有问题导致不能登录成功从而影响创建bug
    createbug = requests.post(zentaourl+createbugurl %(productid, branch, module, Common.zentao_sid()), data = data,auth=Common.zentaoauth())

"""
图片上传接口，返回数据不可用。
{"status":"success","data":"{\"title\":\"\",\"uid\":\"5bd1dc7c53d53\",\"module\":\"0\",\"params\":\"0\",\"pager\":null}","md5":"942702c9fd596b7715e36c4fc67cd319"}

def uploadPNG():
    data = {'localUrl': r'D:\errPNG\error.png'}
    uploadapi = requests.get("http://127.0.0.1/zentao/file-uploadImages-0-0.json?zentaosid=hs7igcblmdff0uqvj1865ja9q5&dir=image",data=data,auth=Common.zentaoauth())
    print(uploadapi.text)
"""




if __name__ == '__main__':
    #bugdata = Common.zentao_bug_info(u'测试登录',u'正确输入用户名密码，点击登录按钮',u'用户登录失败',u'用户登录成功')
    #print(bugdata)
    createbug(bugdata)