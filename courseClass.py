from studentClass import *
from schoolClass import *

class Course:
    
    def __init__(self,course_name,course_code,course_description):
        self.course_name = course_name
        self.course_code = course_code
        self.course_descrtiption = course_description

    def __str__(self):
        information_student = f"""
Course Name: {self.course_name}
Course Code: {self.course_code}
Course Description: {self.course_descrtiption}       
        """
        return information_student

