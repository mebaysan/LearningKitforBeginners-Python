from user import User

users = [User(1, "Enes", "şifre1"), User(
    2, "Yusuf", "şifre2"), User(3, 'Baysan', "şifre3")]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}


def authenticate(username, password):
    user = username_table.get(username, None)
    if user and password == user.password:
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)
