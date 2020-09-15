import pymysql


class DataBaseHandle:
    def __init__(self):
        '''
        建议MySQL连接
        '''
        self.ip = '127.0.0.1'
        self.port = '3306'
        self.username = 'root'
        self.password = '123456'
        self.database = 'mtx'
        # 建立一个MySQL连接
        self.db = pymysql.connect(self.ip, self.username, self.password, self.database, self.port)

    def insert_data(self, sql):
        '''插入数据'''
        # 获取游标
        self.cur = self.db.cursor()
        try:
            # 执行插入语句
            self.cur.execute(sql)
            self.db.commit()
        except Exception as error:
            print("插入数据错误：", error)
            # 发生错误时回滚
            self.db.rollback()
        finally:
            self.cur.close()

    def delete_data(self, sql):
        '''删除数据'''
        # 获取游标
        self.cur = self.db.cursor()
        try:
            # 执行删除语句
            self.cur.execute(sql)
            self.db.commit()
        except Exception as error:
            print("删除数据错误：", error)
            # 发生错误时回滚
            self.db.rollback()
        finally:
            self.cur.close()

    def update_data(self, sql):
        '''更新数据'''
        # 获取游标
        self.cur = self.db.cursor()
        try:
            # 执行更新语句
            self.cur.execute(sql)
            self.db.commit()
        except Exception as error:
            print(error)
            # 发生错误时回滚
            self.db.rollback()
        finally:
            self.cur.close()

    def select_data(self, sql):
        '''查询数据'''
        # 获取游标
        self.cur = self.db.cursor()
        try:
            # 执行查询语句
            self.cur.execute(sql)
            # 从游标里读取数据，赋值给变量
            data = self.cur.fetchall()
            return data
        except Exception as error:
            print(error)
            raise error
        finally:
            self.cur.close()

    def closeDB(self):
        self.db.close()