from Reports import BugState

def get_testcasename():
    for eachbuginfo in BugState.view_bug_list():
        #print(eachbuginfo)
        resolvedbuglist = []
        if eachbuginfo['status'] == 'resolved':
            _,testcasename = eachbuginfo['title'].split('$')
            resolvedbuglist.append(testcasename)
            return resolvedbuglist