import os
from studentClass import *
from courseClass import *

# declare constants 
COURSE = 1
STUDENT  = 2
QUIT=0

REGISTER_NEW_STUDENT=1
DISPLAY_STUDENT=2
DISPLAY_ALL_STUDENTS=3
DELETE_STUDENT=4
ADD_STUDENT_GRADE=5
DISPLAY_STUDENT_GRADE=6 
ASSIGN_COURSE_TO_STUDENT=7

ADD_NEW_COURSE=1
DISPLAY_COURSE=2
DISPLAY_ALL_COURSES=3

class School:

    student_list = []
    course_list = []
    teacher_list = []

    def operation_list_for_students(self):
        os.system("cls")
        print("""Welcome to Student Management System
1. Register new student 
2. Display a student
3. Display all students
4. Delete student
5. Add a new grade for a student 
6. Display   student grade 
7. Assign Course to student 

Enter your choice(0 to quit):""")

    def operation_list_for_courses(self):   
        os.system("cls")
        print("""
1. Add a new course
2. Display course detail
Enter your choice(0 to quit):
""")
    def find_student(self,stuNo):
        for obj in self.student_list:
            if obj.studentNo == stuNo:
                return obj

    def find_course(self,coursName):
        for obj in self.course_list:
            if obj.course_name== coursName:
                return obj

    def add_student(self):
        first_name = input("Please enter the first name of the student: ")
        last_name = input("Please enter the last name of the student: ")
        student_no = int(input("Please enter the student number of the student: "))

        student = Student(first_name,last_name,student_no)
        self.student_list.append(student)

    def display_student(self,stuNo):
        print(self.find_student(stuNo))

    def display_all_students(self):
        for obj in self.student_list:
            print(obj)

    def add_course(self):
        course_name = input("Please enter the course name: ")
        course_code = input("Please enter the course code: ")
        course_description = input("Please enter the course description: ")
        course = Course(course_name,course_code,course_description)
        self.course_list.append(course)

    def display_all_courses(self):
        print("---These are the courses---")
        for obj in self.course_list:
            print(obj.course_name)

    def add_course_to_student(self,stuNum,courseName):
        for obj in self.student_list:
            if obj.studentNo == stuNum:
                obj.student_grade[self.find_course(courseName)]=None
        
 
    def dipslay_course(self,courseName):
        print(self.find_course(courseName))

    def run(self):
        while True:
            os.system("cls")
            choice = int(input("If you want to contionue with COURSE section press 1 or for STUDENT section press 2: "))
            if choice==COURSE:
                self.operation_list_for_courses()
                user_input = int(input())

                if user_input == ADD_NEW_COURSE:
                    self.add_course()

                elif user_input== DISPLAY_COURSE:
                    courseName = input("Enter the course name: ")
                    self.dipslay_course(courseName)
                elif user_input == DISPLAY_ALL_COURSES:
                    self.display_all_courses()

            elif choice==STUDENT:
                self.operation_list_for_students()
                user_input = int(input())
                if user_input== REGISTER_NEW_STUDENT:
                    self.add_student()
                elif user_input== DISPLAY_STUDENT:     
                    stuNo = int(input("Enter the student number that you want to display: "))
                    self.display_student(stuNo)
                elif user_input==DISPLAY_ALL_STUDENTS :
                    self.display_all_students()
                elif user_input== DELETE_STUDENT:
                    student_no = int(input("Enter the student number that you want to delete: "))
                    for obj in self.student_list:
                        if obj.studentNo == student_no:
                            self.student_list.remove(obj)
                            del obj

                elif user_input== ADD_STUDENT_GRADE:

                    stuNo = int(input("Enter the student number: "))
                    courseName = input("Enter the course name: ")
                    grade=int(input("Enter the grade:"))
                    for obj in self.student_list:
                        if obj.studentNo == stuNo:
                            obj.add_grade(self.find_course(courseName),grade)

                elif user_input == DISPLAY_STUDENT_GRADE:
                    stuNo = int(input("Enter the student number: "))
                    courseName = input("Enter the course name: ")
                    for obj in self.student_list:
                        if obj.studentNo == stuNo:
                            obj.display_student_grade(self.find_course(courseName))

                elif user_input==ASSIGN_COURSE_TO_STUDENT:
                    student_no = int(input("Please enter the student number: "))
                    self.display_all_courses()
                    courseName = input("Enter the course name: ")
                    self.add_course_to_student(student_no,courseName)
                elif user_input == QUIT:
                    continue
            elif choice==QUIT:
                break

            continue_input = input("Pleae press enter to continue...")
