import random

first_names = open('firstnames.txt', 'rb').read().splitlines()
last_names = open('lastnames.txt', 'rb').read().splitlines()

grades = ['Kindergarten', '1st Grade', '2nd Grade', '3rd Grade', '4th Grade',
'5th Grade', '6th Grade', '7th Grade', '8th Grade', '9th Grade', ' 10th Grade',
'11th Grade', '12th Grade']

class Person(object):


    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.school = None


class Teacher(Person):


    def __init__(self, name, grade):
        super(Teacher, self).__init__(name, grade)
        self.students = None

    size_cap = 10


school = {
    'name': '',
    'principal': {

    },
    'students': {

    },
    'teachers': {

    },
}

number_of_teachers = None

def size_generator():
    global number_of_teachers
    global number_of_students

    number_of_teachers = random.randint(26, 52)
    number_of_students = random.randint((number_of_teachers * 6), (number_of_teachers * 10))



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

    print school['teachers']
    choice = raw_input('>')
    if choice in school['teachers']:
        print school['teachers'][choice].grade

size_generator()
teacher_gen()
