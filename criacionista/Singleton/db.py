from user import User

class DataBase:
    
    _users: list = []

    def __new__(cls) -> None:
        _instance = None
        if(not _instance):
            _instance = cls
        return _instance
    
    def add(self, user: User) -> None:
        self._users.append(user)

    def remove(self, user: User) -> None:
        self._users.remove(user)

    def show(self) -> None:
        for user in self._users:
            print(user.name)

db1 = DataBase()
user = User()
user.name = "seila"
db1.add(db1, user= user)
db1.show(db1)

