from schoolClass import *
from courseClass import *

class Student:
    
    def __init__(self,firstName,lastName,studentNo):
        self.firstName = firstName
        self.lastName = lastName
        self.studentNo = studentNo
        self.student_grade = {}

    def __str__(self):
        information_student = f"""
Name: {self.firstName} {self.lastName}  Student Number: {self.studentNo}
        """
        return information_student

    def add_grade(self,course,grade):
       self.student_grade[course]=grade

    def display_student_grade(self,obj):
            print(self.student_grade[obj])
    

    