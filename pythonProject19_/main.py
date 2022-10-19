class Human:

    leg_count = 4
    can_walk = "True"

    def __init__(self):
        self.get_description = "This is human"

    def set_leg_count(self, count):
        self.leg_count = count


human = Human()
print("Human:", human.get_description, human.can_walk)

leg_count = Human()
print("Human:", leg_count.get_description, leg_count.leg_count)






