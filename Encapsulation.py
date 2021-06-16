class Student:
    __schoolName = 'PAU' # private class attribute

    def __init__(self,thename,thematricno):
        self.__name=thename # private instance variable
        self.__matric=thematricno # private instance variable

    def __display(self): # private method
        print('this is a private method')

    def getdisplay (self):
        self.__display()

    def getname(self):
        return self.__name

    def setname(self):
        self.__name = 'Kaka Brown'


thestudent = Student('Kaka Brown', '021072')
thestudent.getdisplay()
print(thestudent.getname())
