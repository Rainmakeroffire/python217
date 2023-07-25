import sqlite3
import time
import re

from flask import url_for
from flask_login import UserMixin


def get_time():
    current_time = time.time()
    time_struct = time.localtime(current_time)
    date_time_format = "%A %d %B %Y %H:%M, UK"

    return time.strftime(date_time_format, time_struct)


class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id


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

    def add_comment(self, text, url, username):
        try:
            base = url_for('static', filename='assets/images')
            text = re.sub(r'(?P<tag><img\s+[^>]*src=)(?P<quote>[\'"])(?P<url>.*)(?P=quote)>',
                          r'\g<tag>' + base + r'/\g<url>>', text)
            tm = get_time()
            sql = f'INSERT INTO comments VALUES (NULL, ?, ?, ?, ?)'
            user_id = self.get_user_by_username(username)['id']
            self.__cur.execute(sql, (text, url, tm, user_id))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Failed to add comment to database:' + str(e))
            return False
        return True

    def del_comment(self, id):
        sql = "DELETE FROM comments WHERE id = ?"
        try:
            self.__cur.execute(sql, (id,))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Failed to delete comment from database:', str(e))
            return False
        return True

    def get_comment(self, id):
        try:
            sql = "SELECT * FROM comments WHERE id = ?"
            self.__cur.execute(sql, (id,))
            comment = self.__cur.fetchone()
            if comment:
                return dict(comment)
        except sqlite3.Error as e:
            print('Failed to fetch comment from database:', str(e))
        return None

    def get_comments(self, post_id):
        try:
            sql = "SELECT id, text, time, user_id FROM comments WHERE url == ?"
            self.__cur.execute(sql, (post_id,))
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print('Failed to retrieve comments from database:', str(e))
        return []

    def get_user(self, user_id):
        sql = f"SELECT * FROM users WHERE id = ?"
        self.__cur.execute(sql, (user_id,))
        row = self.__cur.fetchone()
        if row:
            user_data = {
                'id': row[0],
                'username': row[1],
                'password': row[2]
            }
            return user_data
        return None

    def get_user_by_username(self, username):
        sql = f"SELECT * FROM users WHERE username = ?"
        self.__cur.execute(sql, (username,))
        row = self.__cur.fetchone()
        if row:
            user_data = {
                'id': row[0],
                'username': row[1],
                'password': row[2]
            }
            return user_data
        return None

    def send_feedback(self, name, email, message):
        try:
            tm = get_time()
            sql = f'INSERT INTO feedback VALUES (NULL, ?, ?, ?, ?)'
            self.__cur.execute(sql, (name, email, message, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Failed to add feedback to database:' + str(e))
            return False
        return True
