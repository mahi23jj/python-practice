class Onlinecourse:
    def __init__(self,course,instractor) -> None:
        self.course=course
        self.inst=instractor
        self.students=[]
    def enroll(self,name):
        self.students.append(name)
        print(f'succesfully enrolled {self.course} !')
    def detail(self):
       print( f"course name: {self.course}\ninstractor: {self.inst}\nenrolled students")
       for st in self.students:
            print(st)
    def complete(self,name):
        if name in self.students:
            self.students.remove(name) 
            print('{name} succesfully completed the course ') 
        else:
            print("{name} don\"t enroled the course")          

##??????????????????
class student:
    def __init__(self,name) -> None:
        self.name=name
        self.coures=[]
    def enrolled(self,course):
        course.enroll()
        self.coures.append(course)
    def data(self):
        print(f'{self.name} is enrolled in the following courses:')
        for cour in self.coures:
            print(cour.course)    
elm=Onlinecourse('programing','Mr. Getent')
elm.enroll('mahlet')
s=Onlinecourse('logic','Mr. mamo')
s.enroll('mahlet')
t=Onlinecourse('Discret','Mr. abel')
t.enroll('mahlet')       
y=student('mahlet')
y.data()


    # def assign(self,course,garde):
    #     for i in range(len(self.coures)):
    #         if course in self.coures[i].course:
    #             if self.name in self.coures[i].students:

                    

# online=Onlinecourse('Math','M.r chere')
# online.enroll('Mahlet')
# online.detail()


       
       



    