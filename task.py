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
import json
import random
from typing import List, Dict, Any

Grades = Dict[str, List[int]]
Attendance = Dict[str, List[int]]
Student = Dict[str, Any]
Dataset = Dict[str, Any]

def load_data(file_path: str) -> Dict:
    with open(file_path, 'r') as file:
        return json.load(file)

def save_data(file_path: str, data: Dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def student_couse_average(student: Dict, course: str) -> float:
    grades: List[int] = student['grades'].get(course, [])
    return sum(grades) / len(grades) if grades else 0.0

def student_total_average(student: Dict) -> float:
    all_grades: List[int] = [grade for courses in student['grades'].values() for grade in courses]
    return sum(all_grades) / len(all_grades) if all_grades else 0.0

def student_attendance(student: Dict, course: str) -> float:
    attendance: List[int] = student.get('attendance', {}).get(course, [])
    return sum(attendance) / len(attendance) if attendance else 0.0

def course_average(data: Dict, course: str) -> float:
    grades: List[int] = []
    for student in data['students']:
        grades.extend(student['grades'].get(course, []))
    return sum(grades) / len(grades) if grades else 0.0

def course_attendance(data: Dataset, course: str) -> float:
    attendance: List[int] = []
    for student in data["students"]:
        attendance.extend(student["attendance"].get(course, []))
    return sum(attendance) / len(attendance) if attendance  else 0.0

def school_average(data: Dict, school: str) -> float:
    students: List[Student] = list(filter(lambda s: s['school'] == school, data['students']))
    grades: List[int] = [grade for student in students for courses in student['grades'].values() for grade in courses]
    return sum(grades) / len(grades) if grades else 0.0

def school_attendance(data: Dict, school: str) -> float:
    students: List[Student] = list(filter(lambda s: s["school"] == school, data["students"]))
    attendance: List[int] = [a for s in students for c in s["attendance"].values() for a in c]
    return sum(attendance) / len(attendance) if attendance else 0.0


def dataset() -> Dict:
    courses = ['Mathematics', 'Chemistry', 'History', 'Art', 'Physics', 'Biology']
    schools = ['Highschool A', 'Highschool B']

    students = []
    for i in range(20):
        students.append({
            "name": f"Student{i+1}",
            "school": schools[i % 2],
            "grades": {course: random.choices([3, 4, 5], k=3) for course in courses},
            "attendance": {course: random.choices([1, 1, 0], k=3) for course in courses}
        })
    return {'students': students, 'courses': courses, 'schools': schools}

if __name__ == "__main__":
    data = dataset()
    save_data('school_data.json', data)
    data = load_data('school_data.json')

    student = data["students"][0]
    print("Student:", student["name"])
    print("Total Average:", student_total_average(student))

    print("Average in Mathematics:", student_couse_average(student, "Mathematics"))
    print("Attendance in Mathematics:", student_attendance(student, "Mathematics"))

    print("Average in Chemistry for all students:", course_average(data, "Chemistry"))
    print("Average for Highschool A:", school_average(data, "Highschool A"))
    print("Attendance for Highschool B:", school_attendance(data, "Highschool B"))
