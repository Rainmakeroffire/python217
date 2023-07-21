import sqlite3
import time


def get_time():
    current_time = time.time()
    time_struct = time.localtime(current_time)
    date_time_format = "%A %d %B %Y %H:%M, UK"

    return time.strftime(date_time_format, time_struct)


class DataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_objects(self, table):
        sql = f"SELECT * FROM {table}"
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print('Failed to read database')
        return []

    def add_post(self, title, text):
        tm = int(time.time())
        sql = f'INSERT INTO posts VALUES (NULL, ?, ?, ?)'
        try:
            self.__cur.execute(sql, (title, text, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Failed to add post to database:' + str(e))
            return False
        return True

    def get_post(self, post_id):
        try:
            self.__cur.execute(f'SELECT title, text, time FROM posts WHERE url == "{post_id}"')
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print('Failed to retrieve data from database', str(e))
        return None

    def add_comment(self, text, url):
        try:
            tm = get_time()
            sql = f'INSERT INTO comments VALUES (NULL, ?, ?, ?)'
            self.__cur.execute(sql, (text, url, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Failed to add comment to database:' + str(e))
            return False
        return True

    def get_comments(self, post_id):
        try:
            sql = "SELECT text, time FROM comments WHERE url == ?"
            self.__cur.execute(sql, (post_id,))
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print('Failed to retrieve comments from database:', str(e))
        return []
