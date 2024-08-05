import datetime as dt
class Animal():
    def __init__(self):
        pass
    def legs(self):
        print("some animals have 2 legs and some have 4, i guess some have more than 4 also ")
        
class Person(Animal):
    def __init__(self, name , country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth
        
    def shout(self):
        print("my date of birth is", self.date_of_birth)
        
    def legs(self):
        print("humans have only 2 legs")
        
    def find_age(self):
        year_of_birth = int(self.date_of_birth[-4:])
        current_year = dt.datetime.now().year
        age = current_year-year_of_birth
        return age


p1 = Person("ram", "India", "30-08-1999")
print(p1.find_age())

p1.legs()
