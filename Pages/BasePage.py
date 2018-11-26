class BasePage(object):
    """创建页面基类"""

    def __init__(self, driver):
        self.driver = driver