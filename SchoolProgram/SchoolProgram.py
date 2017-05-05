import random
import itertools

class Person(object):


    def __init__(self, name):
        self.name = name
        self.grade = None
        self.school = None


class Principle(Person):


    def __init__(self, name, description):
        super(Principle, self).__init__(name)
        self.credentials = credentials


class Teacher(Person):


    def __init__(self, name, grade):
        super(Teacher, self).__init__(name)
        super(Teacher, self).__init__(grade)


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


class Classes(object):


    def __init__(self):
        self.teacher = None
        self.students = None
        self.grade = None

    size_cap = 10


school = {
    'name': '',
    'principle': {

    },
    'classes': {

    },
    'students': {

    },
    'teachers': {

    },
}

names = open('names.txt', 'rb').read()
school_names = open('schoolnames.txt', 'rb').read()

number_of_teachers = None
number_of_students = None

def generator():
    global number_of_teachers
    global number_of_students

    number_of_teachers = random.randint(26, 52)
    number_of_students = random.randint((number_of_teachers * 6), (number_of_teachers * 10))


def welcome():
    global number_of_teachers
    global number_of_students

    print 'Welcome to %s it is a pleasure to meet you.' % school['name']
    print 'We have %d classes here taught by an excellent \
staff of teachers.' % len(school['classes'])
    print 'Each of our teachers can have only up to %d students \
as we like to keep classes small.' % Classroom.size_cap
    print 'We currently have %d teachers and %d \
students.' % (number_of_teachers, number_of_students)

generator()
welcome()
