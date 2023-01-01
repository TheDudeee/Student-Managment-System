import os

class Student:
    
    def __init__(self,firstName,lastName,studentNo):
        self.firstName = firstName
        self.lastName = lastName
        self.studentNo = studentNo
        self.student_grade = {}

    def __str__(self):
        information_student = f"""
Name: {self.firstName} {self.lastName}
Student Number: {self.studentNo}
        """
        return information_student

    def add_student_grade(self,obj):
        stuNum = int(input("Please enter the student number: "))
        courseName = input("Please enter the course name you want to add grade: ")
        grade = int(input("Please enter the grade you want to add: "))
        if obj.course_name == courseName and stuNum==self.studentNo:
                self.student_grade[obj]=grade

    def display_student_grade(self,obj):
        stuNum = int(input("Please enter the student number: "))
        courseName = input("Please enter the course name: ")
        if obj.course_name == courseName and stuNum==self.studentNo:
            print(self.student_grade[obj])
    
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
    
class School:
    
    student_list = []
    course_list = []
    teacher_list = []

    def add_student(self):
        first_name = input("Please enter the first name of the student: ")
        last_name = input("Please enter the last name of the student: ")
        student_no = int(input("Please enter the student number of the student: "))

        student = Student(first_name,last_name,student_no)
        self.student_list.append(student)

    def display_student(self):
        stuNo = int(input("Please enter the student number that you want to display: "))
        for obj in self.student_list:
            if obj.studentNo == stuNo:
                print(obj)

    def display_all_students(self):
        for obj in self.student_list:
            print(obj)

    def add_course(self):
        course_name = input("Please enter the course name: ")
        course_code = int(input("Please enter the course code: "))
        course_description = input("Please enter the course description: ")
        course = Course(course_name,course_code,course_description)
        self.course_list.append(course)

    def display_all_courses(self):
        for obj in self.course_list:
            print(obj.course_name)

    """"
    def find_student(self,stuNo):
        for obj in self.student_list:
            if obj.studentNo == stuNo:
                return obj
    def find_course(self,coursName):
        for obj in self.course_list:
            if obj.course_name== coursName:
                return obj
                """

    def add_course_to_student(self,stuNum):
        courseName = input("Please enter the course name: ")
        for obj in self.student_list:
            if obj.studentNo == stuNum:
                obj.student_grade[self.find_course(courseName)]=None
        

    def dipslay_course(self):
        courseCode = int(input("Please enter the course code: "))
        for obj in self.course_list:
            if obj.course_code == courseCode:
                print(obj)

    
    
def information_student():
    os.system("cls")
    print("""Welcome to Student Management System
If you want to register new student print 1
If you want to display the students print 2
If you want to display all students print 3
If you want to delete a student print 4
If you want to add a new grade for student print 5
If you want to display the student grade print 6
If you want to register a course print 7
If you want to leave print 0
""")

def information_course():
    os.system("cls")
    print("""
If you want to add new course print 1
If you want to display the course print 2
If you want to leave print 0 
""")
school = School()

while True:
    os.system("cls")
    choice = int(input("If you want to contionue with COURSE section press 1 or for STUDENT section press 2: "))
    if choice==1:
        information_course()
        user_input = int(input())
        if user_input == 1:
            school.add_course()
    
        elif user_input== 2:
            school.dipslay_course()
        
        elif user_input == 3:
            print("See you again:)")
            break

    elif choice==2:
        information_student()
        user_input = int(input())
        if user_input== 1:
            school.add_student()

        elif user_input== 2:
            
            school.display_student()
        
        elif user_input==3 :
            school.display_all_students()

        elif user_input== 4:
            removed_student_no = int(input("Please enter the student number that you want to delete: "))
            for obj in school.student_list:
                if obj.studentNo == removed_student_no:
                    school.student_list.remove(obj)
                    del obj
        elif user_input== 5:
            
        elif user_input == 6:
            
        elif user_input==7:
            student_no = int(input("Please enter the student number: "))
            school.display_all_courses()
            school.add_course_to_student(student_no)
        elif user_input == 0:
            print("See you again:)")
            break

    continue_input = input("Pleae press enter to continue")

for i in school.student_list[0].student_grade:
    print(i)