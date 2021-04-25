import math
import numpy
import curses

#
Student = []
StudentID = []
Course = []
CourseID = []
Mark = []
Credit = []
gpa = []
MarkGPA = []


class Students:
    def __init__(self, id, name, dob):
        self.__id = id
        self.__name = name
        self.__dob = dob
        Student.append(self)
        StudentID.append(self.__id)

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_dob(self):
        return self.dob


class Courses:
    def __init__(self, cid, cname, ccredit):
        self._cid = cid
        self._cname = cname
        self._ccredit = ccredits
        Course.append(self)
        CourseID.append(self._cid)
        Credit.append(self._ccredit)

    def get_id(self):
        return self._cid

    def get_name(self):
        return self.cname

    def get_credit(self):
        return self._ccredit


class Marks:
    def __init__(self, mid, nid, mark, gpa):
        self._mid = mid
        self._nid = nid
        self._mark = mark
        Mark.append(self)

    def get_mid(self):
        return self.mid

    def get_nid(self):
        return self.nid

    def get_mark(self):
        return self.mark

    def get_gpa(self):
        return self.gpa


# Input total number of students

def student_num():
    print("---- TOTAL NUMBER OF STUDENTS----")
    student = int(input("Enter total number of student: "))
    return student


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
    Student.append(st_u)
    StudentID.append(id)


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


# Create mark for students
def create_mark():
    g = 1
    tu = len(Student)
    while g <= tu:
        g += 1
        mid = input("Enter the Student ID: ")
        if mid in Student:
            for i in range(0, len(CourseID)):
                nid = input("Enter the Course ID: ")
                if nid in CourseID:
                    mark = float(input("Enter Student Mark: "))
                    kk = {
                        'mid': mid,
                        'nid': nid,
                        'mark': mark
                    }
                else:
                    print("Student ID NOT FOUND !!")
                    break
                Mark.append(kk)
        else:
            print("Course ID NOT FOUND !!")
            break


def mark_gpa():

    int = numpy.array([self.mark])
    null = numpy.array([self._ccredit])
    strace.addstr("Enter Student's ID:")
    id = strace.getstr().decode()
    if id in StudentID:
        for i in range(0, len(Student)):
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


def gpa_sort():
    sortg = numpy.array([MarkGPA])
    sortg[::-1].sort()
    strace.addstr("GPA Sorted %s: \n" % sortg)
    strace.refresh()


def show_list_student():
    print("----Student List----")
    for i in range(0, len(Student)):
        print(f"ID:{Student[i]['id']} name:{Student[i]['name']} DoB:{Student[i]['dob']}")


def show_list_course():
    print("----COURSE LIST----")
    for i in range(0, len(Course)):
        print(f"ID:{Course[i]['id']}  name : {Course[i]['name']}")


def show_mark():
    print("----STUDENTS MARK LIST----")
    for i in range(0, len(Mark)):
        print(f"ID-course: {Mark[i]['b']} ID-Student: {Mark[i]['a']}  mark:{Mark[i]['mark']}")


# main
s = int(student_num())
l = 1
while l <= s:
    l += 1
    add_student()
    show_list_student()

c = int(course_num())
p = 1
while p <= c:
    p += 1
    add_course()
    show_list_course()

# GPA
mark_gpa()


create_mark()
for i in range(0, len(Course)):
    ol = int(input("You Choose: "))
    if ol == 1:
        print("--STUDENT MARK--")
        show_mark()
        break
    else:
        break
