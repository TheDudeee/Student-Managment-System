from studentClass import *
from courseClass import *
from schoolClass import *

class Teacher:
    
    def __init__(self,firstName,lastName,major):
        self.firstName= firstName
        self.lastName= lastName
        self.major = major
        self.assigned_courses= {}
    
    def __str__(self):
        information_teacher = f"""
Teacher Name: {self.firstName} {self.lastName}
Teacher Faculty: {self.faculty}
Teacher Major: {self.major}       
        """
        return information_teacher

    def assign_teacher_to_course(self,teacher,course):
        self.assigned_courses[teacher]=course
    
