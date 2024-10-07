class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = 'user'


    def get_user_id(self):
        return self.__user_id


    def get_name(self):
        return self.__name


    def set_name(self, name):
        self.__name = name


    def get_access_level(self):
        return self.__access_level


    def __repr__(self):
        return f"User(ID: {self.__user_id}, Name: {self.__name}, Access: {self.__access_level})"


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__access_level = 'admin'
        self.user_list = []


    def add_user(self, user):
        if isinstance(user, User):
            self.user_list.append(user)
            print(f"Пользователь {user.get_name()} добавлен.")
        else:
            print("Ошибка: объект не является пользователем.")


    def remove_user(self, user_id):
        for user in self.user_list:
            if user.get_user_id() == user_id:
                self.user_list.remove(user)
                print(f"Пользователь {user.get_name()} удалён.")
                return
        print(f"Пользователь с ID {user_id} не найден.")


    def show_users(self):
        if self.user_list:
            print("Список пользователей:")
            for user in self.user_list:
                print(user)
        else:
            print("Нет пользователей в системе.")


    def __repr__(self):
        return f"Admin(ID: {self.get_user_id()}, Name: {self.get_name()}, Access: admin)"



admin = Admin(1, "Administrator")


user1 = User(2, "John Doe")
user2 = User(3, "Jane Smith")
user3 = User(4, "Emily Johnson")

admin.add_user(user1)
admin.add_user(user2)
admin.add_user(user3)


admin.show_users()


admin.remove_user(3)


admin.show_users()
