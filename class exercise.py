class Student:
    studentLevel = 'first year computer science 2020/2021 session'
    studentCounter = 0

    def __init__(self, thename, thematricno, thesex):
        self.name = thename
        self.matricno = thematricno
        self.sex = thesex
        Student.studentCounter = Student.studentCounter

    def getName(self):
        return self.name

    def setName(self, thenewName):
        self.name = thenewName

    @staticmethod
    def PAUNanthem():
        print('Pau, here we come, Pau, here we come ')


studendt1 = Student('James Kaka', '021074', 'M')
print(studendt1.getName())
studendt1.setName('James Gaga')
print(studendt1.getName())

Student.PAUNanthem()