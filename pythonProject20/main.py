class Human:


    leg_count = 4
    get_gender= "Unknown"

    def get_gender(self):
        print("Human: Unknown")

class Man(Human):


    def get_gender(self):
        print("Gender: Man")

