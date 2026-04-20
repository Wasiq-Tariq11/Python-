class Student:
    college_name="ABC" #class attribute
    def __init__(self, name, cgpa):
        self.name = name #instance attribute
        self.cgpa=cgpa
    def get_cgpa(self):
        return self.cgpa


stu1 = Student("Wasiq",9.3)
stu2 = Student("Ifham",9.4)
stu3 = Student("Aqib",9.5)

print(stu1.name)
print(f"{stu1.name} has cgpa= {stu1.get_cgpa()}")
print(stu1.college_name)
   



