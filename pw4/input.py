# packages
import math
import numpy
import curses
from domains.Student import *
from domains.Course import *
from domains.Mark import *


class InputModule:
    # Input number of students
    @staticmethod
    def student_num():
        print("---- TOTAL NUMBER OF STUDENTS----")
        student = int(input("Enter total number of student: "))
        return student

    # Add student
    @staticmethod
    def add_student():
        print("-----ADD A STUDENT-----")
        id = input("Enter Student's ID: ")
        name = input("Enter Student's NAME: ")
        dob = input("Enter Student's DOB: ")
        st_u = {
            'id': id,
            'name': name,
            'dob': dob
        }
        studentIDs.append(id)
        studentIDs.append(st_u)


    # Add number of course
    @staticmethod
    def course_num():
        print("---- ADD NUMBER OF COURSE----")
        course = int(input("Enter total number of course: "))
        return course

    # Add course
    @staticmethod
    def add_course():
        print("---- ADD A COURSE ----")
        cid = input("Enter Course's ID: ")
        cname = input("Enter Course's NAME: ")
        cc = input("Enter Course's Credit:")
        cr_o = {
            'cid': cid,
            'cname': cname,
            'cc': cc
        }
        Course.append(cr_o)
        CourseID.append(cid)

    # Create mark for students
    @staticmethod
    def create_mark():
        g = 1
        tu = len(Student)
        while g <= tu:
            g += 1
            mid = input("Enter the Student ID: ")
            if mid in Student:
                for i in range(0, len(Course)):
                    nid = input("Enter the Course ID: ")
                    if nid in CourseID:
                        mark = float(input("Enter Student Mark: "))
                        m_add = {
                            'mid': mid,
                            'nid': nid,
                            'mark': mark
                        }
                    else:
                        print("Student ID NOT FOUND !!")
                        break
                    Mark.append(m_add)
            else:
                print("Course ID NOT FOUND !!")
                break


def mark_gpa():
    print("---GPA Calculation---")
    value = numpy.array([Mark])
    points = numpy.array([Credit])
    print("Enter Student's ID to calculate: ")
    mid = input("Enter Student's ID: ")
    if mid in StudentID:
        for i in range(len(Mark)):
            totalCredit = numpy.sum(points)
            totalValue = numpy.sum(numpy.multiply(value, points))
            gpa = totalValue / totalCredit
    else:
        return 0
    MarkGPA.append(gpa)


def mark_cal():
    print("---GPA---")
    MarkGPA.append(gpa)
    for m in Mark:
        print(f"Course ID: {Mark[i]['nid']} Student ID: {Mark[i]['mid']}  Gpa: " % gpa)
        break


