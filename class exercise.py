class Student:
    studentLevel = 'first year computer science 2020/2021 session'
    studentCounter = 0

    def __init__(self, thename, thematricno, thesex, thehostelname , theage,thecsc102examscore):
        self.name = thename
        self.matricno = thematricno
        self.sex = thesex
        self.hostelname = thehostelname
        self.age = theage
        self.csc102examscore = thecsc102examscore
        Student.studentCounter = Student.studentCounter

    registeredCourse = 'CSC102'
    @classmethod
    def registeredcourse(cls):
        print("registerd course is {Student.registeredCourse}")


    def function(self):

        if self.age > 16:
            return "yes, he is older than 16"
        else:
            return "no he is not older than 16"

    def getName(self):
        return self.name

    def setName(self, thenewName):
        self.name = thenewName

    @staticmethod
    def PAUNanthem():
        print('Pau, here we come, Pau, here we come ')


studendt1 = Student('James Kaka', '021074', 'M','cooperative mall',15,98)
print(studendt1.getName())
studendt1.setName('James Gaga')
print(studendt1.getName())
print(studendt1.function())
Student.registeredCourse()


Student.PAUNanthem()