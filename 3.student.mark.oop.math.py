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

print("Magic things about to happen....")
screen = curses.initscr()
print("Approved")
screen.refresh()
curses.napms(3000)
curses.endwin()
print("Ended")


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
        self._ccredit = ccredit
        Course.append(self)
        CourseID.append(self._cid)
        Credit.append(self._ccredit)

    def get_id(self):
        return self.cid

    def get_name(self):
        return self.cname

    def get_credit(self):
        return self.ccredit


class Marks:
    def __init__(self, mid, nid, mark, gpa):
        self._mid = mid
        self._nid = nid
        self._mark = mark
        self._gpa = gpa
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
    return course


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
        mid = input("Enter Student's ID: ")
        if mid in StudentID:
            for i in range(0, len(Course)):
                nid = input("Enter Course's ID: ")
                if nid in CourseID:
                    mark = math.floor(float(input("Enter Student's Mark: ")))
                    m_add = {
                        'mid': mid,
                        'nid': nid,
                        'Mark': mark

                    }
                Mark.append(m_add)


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


def gpa_sort():
    arr = numpy.array([gpa_sort()])
    arr[::-1].sort()
    print("=====LIST====")
    print("The list is %s:\n" % arr)


def show_list_student():
    print("----Student List----")
    for i in range(0, len(Student)):
        print(f"ID:{Student[i]['id']} name:{Student[i]['name']} DoB:{Student[i]['dob']}")


def show_list_course():
    print("----COURSE LIST----")
    for i in range(0, len(Course)):
        print(f"ID:{Course[i]['cid']}  name : {Course[i]['cname']}")


def show_mark():
    for i in range(0, len(Mark)):
        print(f"Course ID: {Mark[i]['nid']} Student ID: {Mark[i]['mid']}  Mark:{Mark[i]['Mark']}")


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

create_mark()
for i in range(0, len(Course)):
    print("Show mark? 1. YES  2. NO")
    choose = int(input("You Choose: "))
    if choose == 1:
        print("--STUDENT MARK--")
        show_mark()
        break

mark_gpa()
mark_cal()
