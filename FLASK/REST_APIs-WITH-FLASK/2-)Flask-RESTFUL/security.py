from werkzeug.security import safe_str_cmp
from user import User

USERS = [
    User(1, 'baysan', 'asd')
]


USERNAME_MAPPING = {u.username: u for u in USERS}
USERID_MAPPING = {u.id: u for u in USERS}


def authenticate(username, password):
    # dict'ten user'i al, eğer bulamazsan None dön
    user = USERNAME_MAPPING.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return USERID_MAPPING.get(user_id, None)
