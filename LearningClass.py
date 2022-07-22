class Student:
    def __init__(self, name, GPA, age, detentions, accommodations, classes,):
        self.name = name
        self.GPA = GPA
        self.age = age
        self.detentions = detentions
        self.accommodations = accommodations
        self.classes = classes

    def myfunc(self):
        print ("NAME:", self.name)

p1 = Student("JOHN", 97.5, 17, 2, "NO ACCOMODATIONS", 9)
p1.myfunc()

class Course:
    def __init__(self, name, difficulty, teacher, RoomNumber):
        self.classname = name
        self. difficulty = difficulty
        self.teacher = teacher
        self.RoomNumber = RoomNumber

    def myfunc(self):
        print ("COURSE NAME:", self.classname)

p2 = Course("BC CALC", "HIGH DIFFICULTY", "MS. JOHNSON", 203)
p2.myfunc()
