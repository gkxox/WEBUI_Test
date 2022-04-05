from Base.base import BasePage

class UserCenterPage(BasePage):
    def __init__(self,broswer):
        super().__init__(broswer)
        self.user_center_url = 'http://localhost:8089/Home/User/index.html'
