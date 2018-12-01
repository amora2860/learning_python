class Address:
    def __init__(self, street, num):
        self.street_name = street
        self.number = num
        #self.office_number =office_num
    def __str__(self):
        return self.street_name() +"monkey "+ self.number()


class CampusAddress(Address):
    def __init__(self, office):
        Address.__init__(self,"massachusetts Ave.", "77")
        self.office1 = office
    def office_number(self):
        print(self.office1)
    def street_name2(self):
        print(self.street_name)
    def number2(self):
        print(self.number)

Sarina_addr = CampusAddress("g123")
Sarina_addr.office_number()
Sarina_addr.street_name2()
Sarina_addr.number2()


