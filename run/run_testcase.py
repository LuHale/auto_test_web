from TestCases import TestLogin
from run import Monitor_bug_state

import os
def get_test_case():
    testcaselist = []
    testcase_path = os.path.abspath('..') + r'\TestCases'
    #os.chdir(testcase_path)
    for eachfile in os.listdir(testcase_path):
        if eachfile[:4].lower() == 'test':
            testcaselist.append(eachfile)
    return testcaselist

def  run_resolved_case():
    buglist = Monitor_bug_state.get_testcasename()    #获取已解决的bug的方法列表
    print(buglist)
    for eachtest in buglist:
        print(eachtest.split('.')[0] + '()')
        temptest = eval(eachtest.split('.')[0] + '.' + eachtest.split('.')[0] + '()')
        temptest.setUp()
        eval('temptest.' + eachtest.split('.')[1] + '()')
        temptest.tearDown()

run_resolved_case()
