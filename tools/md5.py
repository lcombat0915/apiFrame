import base64
import hashlib


class Secret:
    '''实现加密方法'''

    def __init__(self, string):
        """
        对字符串进行encode()
        """
        self._string = string.encode('utf-8')

    def md5(self):
        '''
        md5加密
        :return:
        '''
        try:
            sign = hashlib.md5(self._string)
            return sign
        except:
            return False

    def sha1(self):
        """
        sha1加密
        :return:
        """
        try:
            sign = hashlib.sha1(self._string)
            return sign
        except:
            return False

    def base64encode(self):
        """
        base64编码的方法
        :return:
        """
        try:
            sign = base64.b64encode(self._string).decode('utf-8')
            return sign
        except:
            return False

    def base64decode(self):
        """
        base64 解码的方法封装
        :return:
        """
        try:
            sign = base64.b64decode(self._string).decode('utf-8')
            return sign
        except:
            return False


if __name__ == '__main__':
    str = 'hello'
    print(Secret(str).md5())
    # 编码
    jm = Secret(str).base64encode()
    print(Secret(str).base64encode())
    # 解码
    print(Secret(jm).base64decode())


