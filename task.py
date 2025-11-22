# Class diary
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
#
# Please, use your imagination and create more functionalities.
# Your project should be able to handle entire school(s?).
# If you have enough courage and time, try storing (reading/writing)
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface (might be text-like).
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#
#Delete these comments before commit!
#Good luck.

class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = {}
        self.attendance = {}
    
    def add_grade(self, subject, grade):
        if subject not in self.grades:
            self.grades[subject] = []
        self.grades[subject].append(grade)


    def add_attendance(self, subject, presence):
        if subject not in self.attendance:
            self.attendance[subject] = []
        self.attendance[subject].append(presence)

    def calculate_average(self):
        all_grades = []
        for grades in self.grades.values():
            all_grades.extend(grades)
        if all_grades:
            return sum(all_grades) / len(all_grades)
        return 0

    def calculate_attendance(self):
        all_presences = []
        for subject in self.attendance:
            all_presences.extend(self.attendance[subject])
        if all_presences:
            return sum(all_presences) / len(all_presences)
        return 0

class Class(Student):
    def __init__(self, subject):
        self.subject = subject
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)

    def calcualte_class_average(self):
        grades = []
        for student in self.students:   
            if self.subject in student.grades:
                grades.extend(student.grades[self.subject])
        if grades:
            return sum(grades) / len(grades)
        return 0

    def calculate_class_attendance(self):
        presences = []
        for student in self.students:
            if self.subject in student.attendance:
                presences.extend(student.attendance[self.subject])
        if presences:
            return sum(presences) / len(presences)
        return 0

class HighSchool(Class):
    def __init__(self, name):
        self.name = name
        self.classes = []
    
    def add_class(self, class_arg):
        self.classes.append(class_arg)

    def school_attendance(self):
        presences = []
        for class_arg in self.classes:
            for student in class_arg.students:
                if class_arg.subject in student.attendance:
                    presences.extend(student.attendance[class_arg.subject])
        if presences:
            return sum(presences) / len(presences)
        return 0

if __name__ == "__main__":
    student1 = Student("Natalia", "Kowalska")
    student2 = Student("Weronika", "Bartoszewska")
    student3 = Student("Alicja", "Jagiełło")

    python_class = Class("Python")

    python_class.add_student(student1)
    python_class.add_student(student2)
    python_class.add_student(student3)

    student1.add_grade("Python", 5)
    student1.add_grade("Python", 4)
    student1.add_attendance("Python", 1)
    student1.add_attendance("Python", 1)    
    student2.add_grade("Python", 3)
    student2.add_grade("Python", 4)
    student2.add_attendance("Python", 1)
    student2.add_attendance("Python", 0)    
    student3.add_grade("Python", 5)
    student3.add_grade("Python", 5)
    student3.add_attendance("Python", 1)

    school = HighSchool("High School AGH")
    school.add_class(python_class)

    print(f"Average grade for {student1.name}: {student1.calculate_average()}")
    print(f"Average attendance for {student1.name}: {student1.calculate_attendance()}")
    print(f"Class average for Python: {python_class.calcualte_class_average()}")
    print(f"Class attendance for Python: {python_class.calculate_class_attendance()}")
    print(f"School attendance: {school.school_attendance()}")
    