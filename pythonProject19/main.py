class Human:

    leg_count = 4
    can_walk = "True"

    def __init__(self):
        self.get_description = "This is human"

    def set_leg_count(self, count):
        self.leg_count = count


Human_beings = Human()
print("Human:", Human_beings.get_description, Human_beings.can_walk)

Nleg = Human("tiger")
print("Human:", Nleg.get_description, Nleg.leg_count)




