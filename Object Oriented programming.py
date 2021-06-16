# # class Student:
# #     def __init__(self,name,age):
# #         self.name = name
# #         self.age = age
# #     def get_name(self):
# #         return self.name
# #     def get_age(self):
# #         return self.age
# #     def set_age(self,age):
# #         self.age = age
# # student1 = Student("Tolu",16)
# # student1.set_age(17)
# # print(student1.get_name())
# # print(student1.get_age())
# # Explanation of class
# class Student:
#     def __init__(self,name,age,grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
#     def get_grade(self):
#         return self.grade
#
# class Course:
#     def __init__(self,name,max_student):
#         self.name = name
#         self.max_student = max_student
#         self.students = []
#     def add_students(self,Student):
#         if len(self.students) < self.max_student:
#             self.students.append(Student)
#             return True
#         return False
#     def get_average_grade(self):
#         value =0
#         for students in self.students:
#             value += students.get_grade()  # students here is from the "for" statement
#
#         return value / len(self.students)
# s1 = Student("Joseph",17,99)
# s2 = Student("George",31,83)
# s3 = Student("Akaolisa",17,93)
# s4 = Student("Ugochukwu",19,100)
# course = Course("Computer Science",2)
# course.add_students(s2)
# course.add_students(s4)
# print(course.add_students(s1))
# print(course.students[0].name)
#
# print(course.get_average_grade())

# Inheritance
class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(f"My name is {self.name} and I am {self.age} years old")
    def speak(self):
        print("I dont know what to say")
class Dog(Pet):
    def speak(self):
        print("bark")
class Cat(Pet):
    def speak(self):
        print("meow")
class Fish(Pet):
    pass
p = Pet("Ziggi",4)
p.show()
p.speak() # prints out I dont know what to say since it is directly under the class Pet
c = Cat("Kitty",7)  # inherited from the class Pet
c.show() # inherited from the class Pet
c.speak() #prints meow because it is more  specific to cat
d = Dog("Max",2) # inherited from the class Pet
d.show() # inherited from the class Pet
d.speak() # prints bark because it is more specific to dog
f = Fish("Bubbles",10)
f.speak() # prints I dont know what to say because the speak method was not defined and therefore it inherits "speak" from Pet
