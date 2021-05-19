import hashlib


def hash_password(password):
    hash_obj = hashlib.sha256(password.encode())
    return hash_obj.hexdigest()


class User:
    def __init__(self, id, username, picture, name, password, is_admin):
        self.id = id
        self.username = username
        self.picture = picture
        self.name = name
        self.password = password
        self.is_admin = bool(is_admin)

    def check_password(self, password):
        return hash_password(password) == self.password

    def __getstate__(self):

        # not sending "password" when instance is "jsonified"

        return {
            "id": self.id,
            "username": self.username,
            "picture": self.picture,
            "name": self.name,
            "is_admin": self.is_admin,
        }
