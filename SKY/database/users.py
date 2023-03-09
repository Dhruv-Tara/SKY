# BSD 3-Clause License
# Copyright (c) 2023, Yash-Sharma-1807

from .data import cur , DB


def check(userid) -> bool :
    "returns if userid is present in db"
    cur.execute(f"Select * from users where user_id = {userid}")
    X = cur.fetchone()
    if X == None :
        return False
    elif X == userid:
        return True


def add_new(userid) -> None :
    X = check(userid)
    if X == False:
        cur.execute(f"Insert into users Values({userid})")
        DB.commit()
    else :
        pass


def get_all_users() -> int :
    "returns all the users"
    cur.execute("Select * from users")
    return len([x[0] for x in cur.fetchall()])