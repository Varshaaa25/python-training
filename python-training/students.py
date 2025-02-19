class Sem:
    def __init__(self,subjects,marks):
        self.subjects=subjects
        self.marks=marks
        
    def __str__(self):
        return f"{self.subjects} {self.marks}"


class Student:
    def __init__(self,name,usn,sems:list):
        self.name=name
        self.usn=usn
        self.sems=sems

    def getDetails(self,usn,sem=None):
        details="\n"
        # if sem parameter is empty
        if sem==None:
            for j in range(len(self.sems[-1].subjects)):
                    details+=self.sems[-1].subjects[j]+ "-"+str(self.sems[-1].marks[j]) +"\n"
        # if sem parameter is passed as argument
        else:
            for i in self.sems:
                if i==sem:
                    for j in range(len(sem.subjects)):
                        details+=sem.subjects[j]+ "-"+str(sem.marks[j]) +"\n"
        print(f"Student with usn {usn} has the following marks:{details}")





sem1=Sem(["kannada","english"],[100,90])
sem2=Sem(["cs","maths"],[80,70])

s1=Student("varsha",176,[sem1,sem2])
# passing sem as parameter
s1.getDetails(176,sem1)
# not passing any sem to the function
s1.getDetails(176)