class Student:
    def __init__(self,first_name,second_name,age,country):
        self.first_name=first_name
        self.second_name=second_name
        self.age=age
        self.country=country
    def greet(self):
        return f"hello your name is {self.first_name} {self.second_name}"    
    def initials(self):
        return f"your initials are {self.first_name[0]}{self.second_name[0]}"

    def birth_year(self):
        year=2022-self.age
        return f"you were born in {year}"    


   
        
   
       
    