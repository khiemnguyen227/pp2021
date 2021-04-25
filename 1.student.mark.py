Student = []
StudentID = []
Course = []
CourseID = []
Mark = []


# Input total number of students
def student_num():
    print("---- TOTAL NUMBER OF STUDENTS----")
    student = int(input("Enter total number of student:"))
    return student


# Add student information
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


# Input number of course
def course_num():
    print("Course number ")
    coursenumber = int(input("Enter the number of course :"))
    if coursenumber <= 0:
        print("Number of course must higher than 0")
        return 0
    else:
        return coursenumber


# Add Course
def add_course():
    name = input("Enter course's NAME:")
    id = input("Enter course's ID: ")
    cr_o = {
        'name': name,
        'id': id
    }
    Course.append(cr_o)
    CourseID.append(id)


# Create mark for students
def create_mark():
    g = 1
    tu = len(Student)
    while g <= tu:
        g += 1
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
                else:
                    print("Student ID NOT FOUND !!")
                    break
                Mark.append(kk)
        else:
            print("Course ID NOT FOUND !!")
            break


def show_list_student():
    print("--Student List--")
    for i in range(0, len(Student)):
        print(f"ID:{Student[i]['id']} name:{Student[i]['name']} DoB:{Student[i]['dob']}")


def show_list_course():
    print("--COURSE LIST--")
    for i in range(0, len(Course)):
        print(f"ID:{Course[i]['id']}  name : {Course[i]['name']}")


def show_mark():
    print("STUDENTS MARK LIST")
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


create_mark()
for i in range(0, len(Course)):
    ol = int(input("You Choose: "))
    if ol == 1:
        print("--STUDENT MARK--")
        show_mark()
        break
    else:
        break
