import os

class ScreenShotUtil:

    def __init__(self,driver,filepath=os.getcwd(),file_name='error.png'):
        self.filename = file_name
        self.driver = driver
        self.filepath = filepath

    def take_screenshot(self):
        if not os.path.exists(self.filepath+'\\errPNG'):
            os.makedirs(self.filepath+'\\errPNG')
        else:
            os.chdir(self.filepath+'\\errPNG')
        self.driver.get_screenshot_as_file(self.filename)

