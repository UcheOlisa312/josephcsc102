# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def get_name(self):
#         return self.name
#     def get_age(self):
#         return self.age
#     def set_age(self,age):
#         self.age = age
# student1 = Student("Tolu",16)
# student1.set_age(17)
# print(student1.get_name())
# print(student1.get_age())
#
class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    def get_grade(self):
        return self.grade

class Course:
    def __init__(self,name,max_student):
        self.name = name
        self.max_student = max_student
        self.students = []
    def add_students(self,Student):
        if len(self.students) < self.max_student:
            self.students.append(Student)
            return True
        return False
    def get_average_grade(self):
        pass
s1 = Student("Joseph",17,100)
s2 = Student("George",31,100)
s3 = Student("Akaolisa",17,100)
s4 = Student("Ugochukwu",19,100)
course = Course("Computer Science",3)
course.add_students(s2)
course.add_students(s4)
#print(course.students[0].name)
for a in course.students:
    print(a.name)
