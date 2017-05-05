import random
import itertools

class Person(object):


    def __init__(self, name):
        self.name = name
        self.grade = None
        self.school = None


class Principal(Person):


    def __init__(self, name, credentials):
        super(Principal, self).__init__(name)
        self.credentials = credentials


class Teacher(Person):


    def __init__(self, name, grade):
        super(Teacher, self).__init__(name)
        super(Teacher, self).__init__(grade)
        self.students = None

    size_cap = 10

class Student(Person):


    def __init__(self, name, grade, GPA):
        super(Student, self).__init__(name)
        super(Student, self).__init__(grade)
        self.GPA = GPA
        self.teacher = None


class School(object):


    def __init__(self, name):
        self.name = name
        self.classes = None


school = {
    'name': '',
    'principal': {

    },
    'students': {

    },
    'teachers': {

    },
}

first_names = open('firstnames.txt', 'rb').read().splitlines()
last_names = open('lastnames.txt', 'rb').read().splitlines() #.title()
school_names = open('schoolnames.txt', 'rb').read().splitlines()
credentials_school = open('credentials.txt', 'rb').read().splitlines()

number_of_teachers = None
number_of_students = None
principal_name = None
grades = ['Kindergarten', '1st Grade', '2nd Grade', '3rd Grade', '4th Grade',
'5th Grade', '6th Grade', '7th Grade', '8th Grade', '9th Grade', ' 10th Grade',
'11th Grade', '12th Grade']

def student_gen():
    global number_of_students
    global school
    global grades

    while len(school['students']) <= number_of_students:

        student_first = random.choice(first_names)
        student_last = random.choice(last_names).title()
        student_name = ('%s, %s') % (student_first, student_last)
        student_grade = random.choice(grades)

        school['students'][student_name] = Student (
            name = student_name,
            grade = student_grade,
            GPA = random.randint(30, 100),
        )

        def teacher_assignment():

            class_size_compare = {

            }

            for teacher in school['teachers']:
                if school['students'][student_name].grade == school['teachers'][teacher].grade:
                    class_size_compare[teacher] = len(school['teachers'][teacher].students)
                    assign = min(class_size_compare, key=class_size_compare.get)

                    return school['students'][student_name].teacher

        teacher_assignment()

def principal_gen():
    global school
    global first_names
    global last_names
    global principal_name

    principal_first = random.choice(first_names)
    principal_last = random.choice(last_names).title()
    principal_name = ('%s, %s') % (principal_first, principal_last)

    school['principal'][principal_name] = Principal(
        name = principal_name,
        credentials = random.choice(credentials_school),
    )


def school_namer():
    global school_names
    global school

    school['name'] = random.choice(school_names)


def size_generator():
    global number_of_teachers
    global number_of_students

    number_of_teachers = random.randint(26, 52)
    number_of_students = random.randint((number_of_teachers * 6), (number_of_teachers * 10))


def welcome():
    global number_of_teachers
    global number_of_students
    global principal_name

    print 'Welcome to %s K-12, it is a pleasure to meet you.' % school['name']
    print 'We have %d classes here taught by an excellent \
staff of teachers.' % len(school['teachers'])
    print 'Each of our teachers can have only %d students, \
as we like to keep classes small.' % Teacher.size_cap
    print 'We currently have %d teachers and %d \
students.' % (number_of_teachers, number_of_students)
    print 'This is our lovely principal %s they got their masters \
at %s.' % (school['principal'][principal_name].name, school['principal'][principal_name].credentials)

school_namer()
size_generator()
principal_gen()
student_gen()
welcome()
import pdb; pdb.set_trace()
