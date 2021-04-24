class Student:
    def __init__(self, id, name, dob):
        self.__id = id
        self.__name = name
        self.__dob = dob

    Student.append(self)
    StudentID.append(self.__id)

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob


class Course:

    def __init__(self, cid, cname):
        self.cid = cid
        self.cname = cname

    Course.append(self)
    CourseID.append(Self.cid)

    def get_cid(self):
        return self.cid

    def get_name(self):
        return self.cid


class Mark:

    def __init__(self, a, b, mark):
        self.a = a
        self.b = b
        self.mark = mark

    Mark.append(sefl)

    def get_a(self):
        return self.a

    def get_b(self):
        return self.b

    def get_mark(self):
        return self.mark


# Input number of students

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
    studentID.append(id)
    student.append(st_u)


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
    cr_o = {
        'cid': cid,
        'cname': cname
    }
    Course.append(cr_o)
    CourseID.append(cid)


# Create mark for students
def create_mark():
    g = 1
    tu = len(Student)
    while g <= tu:
        g += 1
        a = input("Enter the Student ID: ")
        if a in StudentID:
            for i in range(0, len(Course)):
                b = input("Enter the Course ID: ")
                if b in CourseID:
                    mark = float(input("Enter Student Mark: "))
                    kk = {
                        'a': a,
                        'b': b,
                        'mark': mark
                    }
                else:
                    print("Student ID NOT FOUND !!")
                    break
                Mark.append(kk)
        else:
            print("Course ID NOT FOUND !!")
            break


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
s = int(totalnumberofstudent())
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
    ol = int(input("Your option is: "))
    if ol == 1:
        print("--STUDENT MARK--")
        show_mark()
        break
    else:
        break
