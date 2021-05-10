import curses
import os
import zipfile
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
        ol = int(input("You Choose: "))
        if ol == 1:
            print("--STUDENT MARK--")
        show_mark()
        break


mark_gpa()
mark_cal()

pw5 = zipfile.ZipFile('D:\\Studies\\B2 subjects\\git\\pp2021\\pw5\\students.dat', "w")

for folder, subfolders, files in os.walk('D:\\Studies\\B2 subjects\\git\\pp2021\\pw5'):

    for file in files:
        if file.endswith('.py'):
            pw5.write(os.path.join(folder, file),
                      os.path.relpath(os.path.join(folder, file), 'D:\\Studies\\B2 subjects\\git\\pp2021\\pw5\\'),
                      compress_type=zipfile.ZIP_DEFLATED)

pw5 = zipfile.ZipFile('D:\\Studies\\B2 subjects\\git\\pp2021\\pw5\\students.dat')
pw5.extractall('D:\\Studies\\B2 subjects\\git\\pp2021\\pw5\\Compress and Decompress\\')

pw5.close()