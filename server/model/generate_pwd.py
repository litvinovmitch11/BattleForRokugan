import hashlib
import os
import psycopg2

from server_config import *


def encode_pwd(pwd):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', pwd.encode('utf-8'), salt, 100000)
    return salt.hex(), key.hex()


def check_pwd(salt, key, pwd):
    new_key = hashlib.pbkdf2_hmac('sha256', pwd.encode('utf-8'), bytes.fromhex(salt), 100000)
    return new_key == bytes.fromhex(key)


def add_user(login, password):
    login = login.strip()
    password = password.strip()
    if login != '' and login != 'guest' and password != '':
        with psycopg2.connect(dbname=DBNAME, user=DBUSER, password=DBPWD, host=HOST) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"select * from client.players where client.players.login='{login}';")
                if not cursor.rowcount:
                    salt, key = encode_pwd(password)
                    cursor.execute(f"insert into client.players values ('{login}', '{salt}', '{key}', 0, 0);")
                    return True
    return False


def login_user(login, password):
    with psycopg2.connect(dbname=DBNAME, user=DBUSER, password=DBPWD, host=HOST) as conn:
        with conn.cursor() as cursor:
            cursor.execute(f"select * from client.players where client.players.login='{login}';")
            if cursor.rowcount:
                login, salt, key, games_cnt, wins_cnt = cursor.fetchone()
                return check_pwd(salt, key, password)
    return False


def get_result():
    with psycopg2.connect(dbname=DBNAME, user=DBUSER, password=DBPWD, host=HOST) as connection:
        with connection.cursor() as cur:
            cur.execute(
                f"select login, games_cnt, wins_cnt from client.players order by games_cnt desc, wins_cnt desc, login;")
            return cur.fetchall()


def upd_result(login, password, result: bool):
    if login != 'guest' and login_user(login, password):
        with psycopg2.connect(dbname=DBNAME, user=DBUSER, password=DBPWD, host=HOST) as connection:
            with connection.cursor() as cur:
                cur.execute(f"update client.players set games_cnt = games_cnt + 1 where login='{login}';")
                if result:
                    cur.execute(f"update client.players set wins_cnt = wins_cnt + 1 where login='{login}';")
