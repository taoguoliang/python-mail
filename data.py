import configparser
import datetime
import sqlite3
import json
import pymysql


def transform(all):
    rs = []
    for item in all:
        p = {
            "from": item[0],
            "to0": item[1],
            "to": json.loads(item[2]),
            "subject": item[3],
            "content": item[4],
            "time": item[5].strftime('%Y-%m-%d %H:%M:%S'),
        }
        rs.append(p)
    return rs


class DataAccess:

    def __init__(self):
        # self.conn = sqlite3.connect(":memory:", check_same_thread=False);
        cf = configparser.ConfigParser()
        cf.read("cfg.ini")

        mysqlhost = cf.get("mysql", 'host')
        mysqlport = cf.getint("mysql", "port")
        mysqluser = cf.get("mysql", "user")
        mysqlpassword = cf.get("mysql", "password")
        self.conn = pymysql.connect(host=mysqlhost, port=mysqlport, user=mysqluser, passwd=mysqlpassword, db='mine',
                                    charset='utf8mb4')

        # c = self.conn.cursor()
        # c.execute("CREATE TABLE msg(frm TEXT, to0 TEXT, tos TEXT, subject TEXT, content TEXT,createDate timestamp)");
        # c.execute("CREATE INDEX index_frm ON msg (frm);")
        # c.execute("CREATE INDEX index_to0 ON msg (to0);")
        # self.conn.commit()

    def store_msg(self, msg):
        c = self.conn.cursor()
        c.execute("insert into msg values(%s,%s,%s,%s,%s,%s)",
                  (msg['from'], msg['to'][0], json.dumps(msg['to']), msg['subject'], msg['content'],
                   datetime.datetime.now()))
        self.conn.commit()

    def read_from(self, frm):
        c = self.conn.cursor()
        c.execute("select * from msg where frm = %s order by createDate desc limit 100", (frm,))
        rs = c.fetchall()
        return transform(rs)

    def read_to(self, to):
        c = self.conn.cursor()
        c.execute("select * from msg where to0 = %s order by createDate desc limit 100", (to,))
        rs = c.fetchall()
        return transform(rs)

    def read_all(self):
        c = self.conn.cursor()
        c.execute("select * from msg order by createDate desc limit 100")
        rs = c.fetchall()
        return transform(rs)


dataInstance = DataAccess()
