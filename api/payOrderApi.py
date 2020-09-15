from tools.logger import GetLog
import config
log = GetLog().get_logger()
class PayOrder:
    def __init__(self):
        '''
        这个支付接口是需要重定向，302的url是从提交订单的接口里面获取jump_url
        '''
        # 消费数据
        self.url = config.JUMP_URL
        log.info(f'self.url的值是{self.url}')

    def pay_order(self,session):
        # 对302接口进行处理，不让其重定向 allow_redirects=False
        resp = session.get(self.url,allow_redirects= False)
        print(f"resp.headers['location']是：{resp.headers['location']}")
        resp_pay = session.get(resp.headers['location'])
        return resp_pay