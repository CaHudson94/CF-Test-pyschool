import random
import exit

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


def action(act):
    enroll =
    job_apply =
    grade_check =
    tour =
    help =
    yes =
    no =


    while queries == True:
        if act in enroll:

        elif act in job_apply:

        elif act in grade_check:

        elif act in tour:

        elif act in help:

        else:
            print 'I don\'t think I can help you with that.'
            retry = (raw_input('Would you like to try something else?\n> '))
                if retry in yes:

                elif retry in no:
                    exit('Have a nice day!')

                else:
                    print 'I am sorry we can\'t help you with that.'
                    exit('Have a nice day!')

def teacher_gen():
    global number_of_teachers
    global school
    global grades

    while len(school['teachers']) < number_of_teachers:

        teacher_first = random.choice(first_names)
        teacher_last = random.choice(last_names).title()
        teacher_name = ('%s, %s') % (teacher_first, teacher_last)
        teacher_grade = random.choice(grades)

        school['teachers'][teacher_name] = Teacher (
            name = teacher_name,
            grade = teacher_grade,
        )

        school['teachers'][teacher_name].students = []


def student_gen():
    global number_of_students
    global school
    global grades

    while len(school['students']) < number_of_students:

        student_first = random.choice(first_names)
        student_last = random.choice(last_names).title()
        student_name = ('%s, %s') % (student_first, student_last)
        student_grade = random.choice(grades)
        student_GPA = random.randint(0, 100)

        school['students'][student_name] = Student (
            name = student_name,
            grade = student_grade,
            GPA = '%d%%' % student_GPA,
        )

        def teacher_assignment():

            class_size_compare = {

            }

            for teacher in school['teachers']:
                if school['students'][student_name].grade == school['teachers'][teacher].grade:
                    if len(school['teachers'][teacher].students) < 10:
                        class_size_compare[teacher] = len(school['teachers'][teacher].students)
                        assign = min(class_size_compare, key=class_size_compare.get)

                        school['students'][student_name].teacher = assign

                        for student in school['students']:
                            for class_teacher in school['students'][student].teacher:
                                if school['teachers'][teacher_name] == class_teacher:
                                    school['teachers'][teacher_name]['students'].append(student)

                    elif len(school['teachers'][teacher].students) >= 10:
                        student_grade = random.choice(grades)

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
    print 'We currently have  %d students.' % number_of_students
    print 'This is our lovely principal %s they got their masters \
at %s.' % (school['principal'][principal_name].name, school['principal'][principal_name].credentials)
    print 'What can we help you with today?'

    action_choice = (raw_input('You can enroll a student, apply for a job, \
check how your child is doing, tour the school, or ask for help?\n> ').lower())

    action(action_choice)

school_namer()
size_generator()
principal_gen()
student_gen()
teacher_gen()
welcome()
