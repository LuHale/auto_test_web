import requests
from CommonModel import Common
import json
def view_bug_list(productid=1):
    bug_list_url = 'bug-browse-%s-0-unclosed.json?zentaosid=%s&t=json'
    bug_list = requests.get(Common.zentaoUrl()+bug_list_url %(productid,Common.zentao_sid()),auth=Common.zentaoauth())
    buginfo = json.loads(bug_list.json()['data'])
    return buginfo['bugs']

"""
可以通过模块名称进行分类，bug-browse-1--byModule-1.json
"""

def view_bug(bugid):
    viewbugurl = "bug-view-%s.json?zentaosid=%s&t=json"
    buginfo = requests.get(Common.zentaoUrl()+viewbugurl %(str(bugid),Common.zentao_sid()),auth=Common.zentaoauth())
    bug = json.loads(buginfo.json()['data'])
    return bug['bug']

if __name__ == '__main__':
    bug = view_bug(21)
    print(bug['status'])
    print(view_bug_list())