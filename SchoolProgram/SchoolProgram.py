import random
from sys import exit


class Person(object):


    def __init__(self, name):
        self.name = name
        self.school = None


class Principal(Person):


    def __init__(self, name, credentials):
        super(Principal, self).__init__(name)
        self.credentials = credentials


class Teacher(Person):


    def __init__(self, name, grade):
        super(Teacher, self).__init__(name)
        self.grade = grade
        self.students = None

    size_cap = 10


class Student(Person):


    def __init__(self, name, grade, GPA):
        super(Student, self).__init__(name)
        self.grade = grade
        self.GPA = GPA
        self.teacher = None


school = {
    # Name of the school
    'name': '',
    # Principal
    'principal': {

    },
    # All Students
    'students': {

    },
    # All teachers
    'teachers': {

    },
    # Each grade level with it's respective teachers
    'grade_teachers': {
        'Kindergarten': {},
        '1st Grade': {},
        '2nd Grade': {},
        '3rd Grade': {},
        '4th Grade': {},
        '5th Grade': {},
        '6th Grade': {},
        '7th Grade': {},
        '8th Grade': {},
        '9th Grade': {},
        '10th Grade': {},
        '11th Grade': {},
        '12th Grade:': {}
    },
}

# Pulls lists of data from file for generation
first_names = open('firstnames.txt', 'rb').read().splitlines()
last_names = open('lastnames.txt', 'rb').read().splitlines()
school_names = open('schoolnames.txt', 'rb').read().splitlines()
credentials_school = open('credentials.txt', 'rb').read().splitlines()

# Variables to be set per run of program
number_of_teachers = None
number_of_students = None
principal_name = None

grades = ['Kindergarten', '1st Grade', '2nd Grade', '3rd Grade', '4th Grade',
'5th Grade', '6th Grade', '7th Grade', '8th Grade', '9th Grade', '10th Grade',
'11th Grade', '12th Grade']




# The interface for user interaction with the school
def action():
    global grades
    global school
    global student_name

    commands = {

    }
    commands['enroll'] = ('e', 'enroll', 'enroll child', 'enroll student')
    commands['apply'] = ('apply', 'a', 'apply for job', 'apply to be teacher',
'apply to be a teacher')
    commands['grades'] = ('grades', 'g', 'check', 'check grades', 'students grades',
'check students grades')
    commands['tour'] = ('tour', 't', 'take tour', 'tour the school', 'tour school')
    commands['help'] = ('help', 'h', 'get help', 'ask for help')
    commands['yes'] = ('yes', 'y')
    commands['no'] = ('no', 'n')
    commands['directory'] = ('directory', 'd', 'look up', 'directory look up')

    queries = True


    while queries == True:
        act = (raw_input('\nWhat can we help you with today?\n> ').lower())


        if act.title() in school['students']:
            student = school['students'][act.title()]
            #formatting taught by Tanner Lake
            print 'Name: {}\nGrade: {}\nTeacher: {}\nGPA: {}'.format(
                student.name
                student.grade
                student.teacher
                student.GPA
            )
            repeat = (raw_input('\nCan we help you with something \
else?\n> ').lower())
            if repeat in commands['yes']:
                return
            else:
                queries = False

        elif act.title() in school['teachers']:
            teacher = school['teachers'][act.title()]
            #formatting taught by Tanner Lake
            print "Name: {}\nGrade: {}\nStudents: {}".format(
                teacher.name
                teacher.grade
                teacher.students
            )
            repeat = (raw_input('\nCan we help you with something \
else?\n> ').lower())
            if repeat in commands['yes']:
                return
            else:
                queries = False

        elif act in commands['directory']:
            print 'First a list of the students:'
            for name in school['students'].keys():
                print name

            print '\n\nNow for the teachers:'
            for name in school['teachers'].keys():
                print name

            print '\n\n Last but not least our principal.'
            for name in school['principal'].keys():
                print name

        elif act in commands['enroll']:
            print 'Wonderful let\'s get right to it then.'
            name_first = (raw_input('What is the childs first name?\n> ').lower())
            name_last = (raw_input('What is the childs last name?\n> ').lower())
            print 'Fantastic I am sure we will love %s, %s.' % (name_first, name_last)
            grade_level = (raw_input('And what grade will they be coming \
in for?\n> ').lower())
            print 'Let\'s just double check we have room for your child in \
one of our classes, one moment please.'
            new_student = Student(
                name = (name_first, name_last),
                grade = grade_level,
                GPA = '0%',
            )

            teacher_found = _find_least_busy_teacher(new_student)
            if teacher_found:
                new_student.teacher = teacher_found.name
                teacher_found.students.append(new_student.name)
                school['students'][new_student.name]=new_student
            if not teacher_found:
                print 'It seems we are at capacity for that grade level.'
                print 'I am very sorry, you are still welcome to look around \
or learn about the staff and students.'
                leave_or_stay()


        elif act in commands['apply']:
            print 'Fantastic, everyone will be delited to meet you.'
            print 'But first lets get the paper work out of the way.'
            name_first = (raw_input('What is you first name?\n> ').lower())
            name_last = (raw_input('What is your last name?\n> ').lower())
            grade_level = (raw_input('And what grade would you like to \
teach?\n> ').lower())
            print 'Great I am sure the kids will adore you %s, %s.' % (name_first, name_last)
            new_teacher = Teacher(
                name = (name_first, name_last)
                grade = grade_level,
                students = None,
            )

            school['teachers'][new_teacher.name]=new_teacher
            school['grade_teachers'][new_teacher.name]=new_teacher

            print 'Excellent!'
            print 'I speak for all the staff when I say we are excited to \
work with you!'
            print 'I am sure you will have class of your own very soon.'

        elif act in commands['tour']:
            grade_choice = (raw_input('\nWhat grades classes would you like to \
see?\n> '))
            if grade_choice in grades:
                print '\nExcelent!'
                print 'In %s we have:' % grade_choice
                print school['grade_teachers'][grade_choice].values()
                see_class = (raw_input('\nWould you like to see one of their \
classes?\n> ').lower())
                if see_class in commands['yes']:
                    class_choice = (raw_input('\nWho\'s class would you like to \
see?\n> ').lower())
                    if class_choice in school['teachers']:
                        print 'Welcome to %s\'s class.' % class_choice
                        print 'Here are their students: \n'
                        for kid in school['teachers'][class_choice].students:
                            print kid
                            leave_or_stay()
                    else:
                        print 'I don\'t think they teach here?'
                        leave_or_stay()
                else:
                    leave_or_stay()
            else:
                print 'I am not sure that is a grade.'
                leave_or_stay()



        elif act in commands['help']:
            help_command(commands)

        else:
            print '\nI don\'t think I can help you with that.'
            retry = (raw_input('\nWould you like to try something else?\n> '))
            if retry in commands['yes']:
                pass

            elif retry in commands['no']:
                exit('Have a nice day!')

            else:
                print 'I am sorry we can\'t help you with that.'
                exit('Have a nice day!')

    print 'Thank you for visiting %s today.' % school['name']
    print 'We hope you enjoyed your self and look forward to seeing you \
again soon.'
    exit('Have a nice day, goodbye!')

#function if time

def help_command(commands):
    print '\n You can look for students and teachers by name or via \
the directory.'
    print 'Or you can use a few commands to help us help you.'
    print '\nThey are: \n'
    for key in commands.keys():
        print key
    print '\nEach one has a few options you can use.'
    yes_no = (raw_input('\nWould you like to see options for one?\n> '))
    if yes_no in commands['yes']:
        choice = (raw_input('\nPut one in to see it\'s options or \
use back if you are done.\n> '))
        for k, command in commands.items():
            if choice in command:
                print
                for option in command:
                    print option

    elif yes_no in commands['no']:
        print '\nAlright where were we...'

    else:
        print '\n That is not a yes or no.'
        print '\nAlright where were we...'

def leave_or_stay():
    leave_or_stay = (raw_input('\n Alright is that it for today?\n> ').lower())
    if leave_or_stay in commands['yes']:
        return queries = False
    elif leave_or_stay in commands['no']:
        return
    else:
        return queries = False


def teacher_gen():
    global number_of_teachers
    global school
    global grades

    while len(school['teachers']) < number_of_teachers:

        teacher_first = random.choice(first_names).title()
        teacher_last = random.choice(last_names).title()
        teacher_name = ('%s, %s') % (teacher_first, teacher_last)
        teacher_grade = random.choice(grades)

        school['teachers'][teacher_name] = Teacher (
            name = teacher_name,
            grade = teacher_grade,
        )

        school['teachers'][teacher_name].students = []
        for grade in school['grade_teachers']:
            if school['teachers'][teacher_name].grade == school['grade_teachers'][grade]:
                school['grade_teachers'][grade] = teacher_name

#reformated by Tanner Lake
def _find_least_busy_teacher(student):
    class_size_compare = {}

    for teacher in school['teachers'].values():
        if (student.grade == teacher.grade) \
        and (len(teacher.students) < 10):
            class_size_compare[teacher] = len(teacher.students)

    if class_size_compare:
        return min(class_size_compare, key=class_size_compare.get)


def student_gen():
    global number_of_students
    global school
    global grades

    while len(school['students']) < number_of_students:

        student_first = random.choice(first_names).title()
        student_last = random.choice(last_names).title()
        student_name = ('%s, %s') % (student_first, student_last)
        student_grade = random.choice(grades)
        student_GPA = random.randint(0, 100)

        new_student = Student(
            name = student_name,
            grade = student_grade,
            GPA = '%d%%' % student_GPA,
        )

        school['students'][student_name] = new_student

        teacher_found = _find_least_busy_teacher(new_student)


        while not teacher_found:
            new_student.grade = random.choice(grades)
            teacher_found = _find_least_busy_teacher(new_student)

        new_student.teacher = teacher_found.name
        teacher_found.students.append(new_student.name)


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
    print 'You can enroll a student, apply for a job, check your \
students grades, tour the school, or ask for help.'

    action()




def main():
    school_namer()
    size_generator()
    principal_gen()
    teacher_gen()
    student_gen()
    welcome()

if __name__ == "__main__":
    main()
