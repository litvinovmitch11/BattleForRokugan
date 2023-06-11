import hashlib
import os
from config import *
import psycopg2


def encode_pwd(pwd):
    pass


def check_pwd(salt, key, pwd):
    pass


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


def upd_result(login, result: bool):
    with psycopg2.connect(dbname=DBNAME, user=DBUSER, password=DBPWD, host=HOST) as connection:
        with connection.cursor() as cur:
            cur.execute(f"update client.players set games_cnt = games_cnt + 1 where login='{login}';")
            if result:
                cur.execute(f"update client.players set wins_cnt = wins_cnt + 1 where login='{login}';")
