#!/usr/bin/python

import pymysql.cursors
import hashlib

connection = pymysql.connect(host='127.0.0.1',
                            user='user',
                            password='password',
                            db='db',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)

with connection.cursor() as cursor:
    for a in range(0,2):
        for b in range(0,10):
            for c in range(0,10):
                for d in range(0,10):
                    for e in range(0,10):
                        md5 = hashlib.md5(bytes("{0}{1}{2}{3}{4}".format(a,b,c,d,e).encode())).hexdigest()
                        sql = """insert into tbl(a,b,c,d,e,str) value({0}, {1}, {2}, {3}, {4}, '{5}')""".format(a,b,c,d,e,md5)
                        cursor.execute(sql)
connection.commit()
connection.close()