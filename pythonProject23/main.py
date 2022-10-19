

class User:

    __password = "password"

    def get_password(self):
        return self.__password


class ActiveUser(User):
    def get_password(self):
        return "********"


exit_user = ActiveUser()
print(exit_user.get_password())


