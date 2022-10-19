

class Human:

    leg_count = 4
    get_gender = "Unknown"

    def get_gender(self):
        print("Human: Unknown")


class Man(Human):
    def get_gender(self):
        print("Gender: Man")


class Woman(Human):
    def get_gender(self):
        print("Gender: Woman")


human1 = Human()
human1.get_gender()

man1 = Man()
man1.get_gender()

woman1 = Woman()
woman1.get_gender()