# Need to be given a list of class or exams
# Hard and soft contraints need to be provided
# The timetable for the classes / exams need to be generated 

# Compulsory classes & Non compulsory classes in groups (eg. Degree: Mathematics - Compulsory: Math, Sci Non_compulsory: Eng, Bio)

#With this the given data will be:

class Degree:
    def __init__ (self, degreeName, compulsoryClasses, nonCompulsoryClasses):
        self.degreeName = degreeName
        self.compulsoryClasses = compulsoryClasses
        self.nonCompulsoryClasses = nonCompulsoryClasses
example = Degree("Mathematics", ["Maths", "Science", "ComputerScience"], ["English", "Biology","Art History"])

print(example.degreeName)
print(example.nonCompulsoryClasses)