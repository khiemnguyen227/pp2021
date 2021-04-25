import curses
from output import OutputModule
from input import InputModule
from domains.Student import *
from domains.Course import *
from domains.Mark import *


class MainModule:
    # main
    s = int(student_num())
    l = 1
    while l <= s:
        l += 1
        add_student()
    show_list_student()

    c = int(number_course())
    p = 1
    while p <= c:
        p += 1
        add_course()
    show_list_course()

    create_mark()
    for i in range(0, len(Course)):
        print("Show mark? 1. YES  2. NO")
        ol = int(input("You Choose: "))
        if ol == 1:
            print("--STUDENT MARK--")
        show_mark()
        break


# GPA
mark_gpa()
mark_cal()
