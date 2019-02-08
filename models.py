from clcrypto import password_hash


class DatabaseObject:

    def __init__(self):
        self._id = None


class User(DatabaseObject):
    table_name = 'user'

    def __init__(self, username=None, email=None, password=None):
        super().__init__()
        self.username = username
        self.email = email
        self.__password = password_hash(password)

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        if len(password) >= 8:
            self.__password = password_hash(password)

    def save(self, cursor):
        if self._id is None:
            query = f"INSERT INTO {self.table_name} (username, email, password) VALUES (%s, %s, %s) RETURNING ID;"
            values = (self.username, self.email, self.password)
            cursor.execute(query, values)
            self._id = cursor.fetchone()[0]
            return True
        return False

    @staticmethod
    def get_user_by_username(cursor, username):
        query = f"SELECT id, username, email, password, FROM {self.table_name} WHERE username = %s"
        values = (username,)
        cursor.execute(query, values)
        data = cursor.fetchone()
        if data is not None:
            user = User()
            user.id = data[0]
            user.username = data[1]
            user.email = data[2]
            user.__password = data[3]
            return user
