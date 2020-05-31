from Person import Person

#No. of People
#Energy per person
class HouseHold():
    def __init__(self,number_of_people):
        self.number_of_people = number_of_people
        self.appliance_list = []
        self.household_appliance_list = []
        self.person_list = []

        for i in range(self.number_of_people):
            self.person_list.append(Person())