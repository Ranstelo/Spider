# 异步写入mysql数据库
from twisted.enterprise import  adbapi
from MySQLdb import cursors

class MysqlTwistedPipeline(object):
    #这个函数会自动调用
    @classmethod
    def from_settings(cls,settings):
        db_params = dict(
            host=settings["MYSQL_HOST"],
            port=settings["MYSQL_PORT"],
            user=settings["MYSQL_USER"],
            passwd=settings["MYSQL_PASSWD"],
            charset=settings["MYSQL_CHARSET"],
            db=settings["MYSQL_DBNAME"],
            use_unicode=True,
            cursorclass=cursors.DictCursor
        )
        # 创建ConnectionPool 类来管理连接
        dbpool = adbapi.ConnectionPool('MySQLdb',**db_params)

        return cls(dbpool)
    def __init__(self,dbpool):

        self.dbpool = dbpool

    def process_item(self,item,spider):

        query = self.dbpool.runInteraction(self.do_insert,item)
        # 执行SQL查询并返回None
        query.addErrback(self.handle_error,item,spider)
        # 错误处理

    def handle_error(self,failure,item,spider):
        # 错误处理函数
        print(failure)
    def do_insert(self,cursor,item):
        sql = 'insert into bole_blogs(title,blog_url,img_src,blog_date,tags,like_count,comment_count,bookmark_count,img_path)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        # 执行具体的插入
        cursor.execute(sql, (item["title"], item["blog_url"], item["img_src"][0], item["blog_date"], item["tags"], item["like_count"],item["comment_count"], item["bookmark_count"], item["img_path"]))



