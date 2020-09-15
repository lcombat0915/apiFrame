import logging.handlers
import config


class GetLog:
    logger = None

    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            # 获取日志器（日记本）
            cls.logger = logging.getLogger()
            # 给日志器设置总的级别，是封装在logging里面的，设置错误级别，使用大写
            cls.logger.setLevel(logging.INFO)
            # 获取格式器
            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
            # 获取格式器参数，以什么样式输出
            fm = logging.Formatter(fmt)
            # 获取处理器
            tf = logging.handlers.TimedRotatingFileHandler(
                                                        filename=config.DIR_NAME + '/logger/test.log',
                                                        when='H',
                                                        interval=1,
                                                        backupCount=3,
                                                        encoding='utf-8')

            # 在处理器中添加格式器
            tf.setFormatter(fm)
            # 在日志器中添加处理器
            cls.logger.addHandler(tf)
        return cls.logger


if __name__ == '__main__':
    # 测试日志调用
    logger = GetLog.get_logger()
    logger.debug("调试")
    logger.info("信息")
    logger.warning("警告")
    logger.error('错误')
    logger.critical("致命")
