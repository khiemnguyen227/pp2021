# packages
import math
import numpy
import curses
from domains.Student import *
from domains.Course import *
from domains.Mark import *


class InputModule:
    # Input number of students
    def student_num():
        print("---- TOTAL NUMBER OF STUDENTS----")
        student = int(input("Enter total number of student: "))
        return student
    totals = student_num()
    file = open('students.txt', "w")
    file.write("Student's ID: " + str(totals))

    # Add student
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
        StudentID.append(id)
        Student.append(st_u)
        return st_u
    stuinfo = add_student()
    file = open('students.txt', "w")
    file.write("Student's info: " + str(stuinfo))
    file.close()
    # Add number of course
    def course_num():
        print("---- ADD NUMBER OF COURSE----")
        course = int(input("Enter total number of course: "))
        return

    # Add course
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
        return cr_o

    course = add_course()
    file2 = open('courses.txt', "w")
    file2.write("Course's info: " + str(course))
    file2.close()

    # Create mark for students
    def create_mark():
        g = 1
        tu = len(Student)
        while g <= tu:
            g += 1
            print("-- ADD COURSE INFORMATION --")
            mid = input("Enter the Student ID: ")
            if mid in StudentID:
                for i in range(0, len(CourseID)):
                    nid = input("Enter the Course ID: ")
                    if nid in CourseID:
                        mark = float(input("Enter Student Mark: "))
                        kk = {
                            'mid': mid,
                            'nid': nid,
                            'mark': mark
                        }
                        return kk
                    else:
                        print("Student ID NOT FOUND !!")
                        break
                    Mark.append(kk)
            else:
                print("Course ID NOT FOUND !!")
                break

    marks = create_mark()
    file3 = open('marks.txt', "w")
    file3.write("Marks info: " + str(marks))
    file3.close()

    def mark_gpa():

        int = numpy.array([self.mark])
        null = numpy.array([self._ccredit])
        strace.addstr("Enter Student's ID:")
        id = strace.getstr().decode()
        if id in StudentIDs:
            for i in range(0, len(Students)):
                marktotal = numpy.sum(null)
                gpatotal = numpy.sum(numpy.multiply(int, null))
                strace.refresh()
                gpa = gpatotal / marktotal
                strace.refresh()

        else:
            return 0
        print(gpa)

        MarkGPA.append(gpa)
        strace.refresh()
        for point in Mark:
            strace.clear()
            strace.refresh()
            strace.addstr(" [Mark: ] %s   [GPA: ]%s \n" % (mark.get_id(), gpa))
            strace.refresh()

            break
