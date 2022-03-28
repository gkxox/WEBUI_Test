from Base.base import BasePage,BaseHandle


class UserCenterPage(BasePage):
    def __init__(self):
        super().__init__()
        self.user_center_url = 'http://localhost:8089/Home/User/index.html'
