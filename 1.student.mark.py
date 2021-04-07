# student management
Student = []
StudentID = []
Course = []
CourseID = []
Mark = []


# Input of number of student
def totalnumberofstudent():
    student_class = int(input("Enter the number of student:"))
    if (student_class <= 0):
        print("Student must be higher than 0")
        return 'False'
    else:
        return student_class


# Add student information
def add_student():
    print("--Add student information--" )

    id = input("Enter student's ID:")
    name = input("Enter student's NAME:")
    dob = input("Enter student's DOB:")
    stinfor = {
        'id': id,
        'name': name,
        'dob': dob
    }
    StudentID.append(id)
    Student.append(stinfor)


# Input number of course
def number_course():
    print("Course number ")
    coursenumber = int(input("Enter the number of course :"))
    if (coursenumber <= 0):
        print("Number of course must higher than 0")
        return 0
    else:
        return coursenumber


# Add Course
def add_course():
    name = input("Enter course's NAME:")
    id = input("Enter course's ID: ")
    course_f = {
        'name': name,
        'id': id
    }
    Course.append(course_f)
    CourseID.append(id)


# Create mark for students
def mark_mana():
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


# Show all of student in class
def show_list_student():
    print("--Student List--")
    for i in range(0, len(Student)):
        print(f"ID:{Student[i]['id']} name:{Student[i]['name']} DoB:{Student[i]['dob']}")


# Show all of student course
def show_list_course():
    print("--COURSE LIST--")
    for i in range(0, len(Course)):
        print(f"ID:{Course[i]['id']}  name : {Course[i]['name']}")


# Show the mark of student
def show_mark():
    print("STUDENTS MARK LIST")
    for i in range(0, len(Mark)):
        print(f"ID-course: {Mark[i]['b']} ID-Student: {Mark[i]['a']}  mark:{Mark[i]['mark']}")


# main
# recall student
s = int(totalnumberofstudent())
l = 1
while l <= s:
    l += 1
    add_student()
show_list_student()

# recall course
c = int(number_course())
p = 1
while p <= c:
    p += 1
    add_course()
show_list_course()

# Recall student mark
mark_mana()

print("""Choose your options: """)
print("1.YES")
print("2.NO")
for i in range(0, len(Course)):
    ol = int(input("Your option is: "))
    if ol == 1:
        print("--STUDENT MARK--")
        show_mark()
        break
    else:
        break