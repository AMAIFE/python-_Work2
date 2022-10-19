

class Hunt:

    __Weapon = "Assault Rifle"

    def get_weapon(self):
        return self.__Weapon + ":" + "Not Available"


hunt = Hunt()
print(hunt.get_weapon())

