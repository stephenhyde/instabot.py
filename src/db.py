import sqlite3
import time

class instabot_db:

    #conn = sqlite3.connect('/home/innwadmin/instanetwork/instabot/instabot.py/src/instabot.db')
    conn = sqlite3.connect('/Users/stephen.hyde/repositories/instabot.py/src/instabot.db')
    cursor = conn.cursor()

    def __init__(self):
        self.cursor.execute("create table if not exists users(userid int, username varchar(200) , isfollowed chr(1) default '1', insert_time timestamp)")

    def get_next_unfollower(self, user_name, ufollow_interval):
        unfollow_time = time.time() - ufollow_interval
        user = self.cursor.execute("select userid, username, insert_time from users where isfollowed = '1' and username = ? and insert_time < ? order by RANDOM() limit 1", (user_name, unfollow_time,))
        u = user.fetchone()
        if u is not None and len(u) > 0:
            return u[0], u[1], u[2]
        else:
            return 0,'',''

    def is_followed(self, user_name, user_id):
        users = self.cursor.execute("select userid from users where userid = ? and username = ?",  (user_id, user_name,))
        return len(users.fetchall()) > 0

    def unfollow(self, user_name, user_id):
        self.cursor.execute("update users set isfollowed = '0' where userid = ? and username = ?", (format(user_id), user_name,))
        self.conn.commit()

    def follow(self, user_name, user_id):
        self.cursor.execute("insert into users (userid, username, isfollowed, insert_time) values (%i, '%s', '1', %f)" %(user_id, user_name, time.time()))
        self.conn.commit()

    def close(self):
        self.conn.close()
