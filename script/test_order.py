import requests

from api.orderApi import Order
from api.loginApi import MtxLogin

class TestOrder:
    def setup_class(self):
        # web ui自动化 创建driver
        self.session = requests.Session()
        self.order_obj = Order()


    def test_order(self):
        '''
        依赖于登录：api级别的，请求级别，完全独立
        :return:
        '''
        # 调用成功的登录接口
        MtxLogin().login_success(self.session)
        resp_order = self.order_obj.order(self.session)
        assert resp_order.json().get('msg') == "提交成功"


