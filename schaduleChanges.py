class Period:
    def __init__(self, courses):
        self.courses = courses

    def course_name(self, x):
        return self.courses[x]


class MasterSchedule:
    def __init__(self, periods):
        self.periods = periods


if __name__ == '__main__':
    first = Period([
        'Band(HS)',
        'Alg 1(9)',
        'Geometry',
        'AP Eng Lit(12)',
        'AP Seminar(11 & 12)',
        'Street Law',
        'AP CSA',
        'Art 1',
        'Ind Skill Build',
        'AP CSP',
        'Band(HS)'
    ])

    second = Period([
        'Algebra II',
        'Pre - Cal',
        'AP Bio',
        'Chem(9 / 10)',
        'AP Human Geo(9)',
        'AP US / AP Macro(12)',
        'Art 2 Draw',
        'PE',
        'Coll Read(12)'
    ])
    third = Period([

    ])

    fourth = Period([
        'Algebra II',
        'Pre - Cal',
        'Athletics',
        'Chem(9 / 10)',
        'AP Eng Lang(11)',
        'AP World Hist(10)',
        'AP US / AP Macro(12)',
        'Art 1',
        'Athletics',
        'Graphic Design'

    ])

    fifth = Period([

    ])

    sixth = Period([
        'Alg 1(9)',
        'AP Stats',
        'AP Environ',
        'AP Physics',
        'English II(10)'

    ])

    seventh = Period([

    ])

    eighth = Period([
        'Alg 1(9)',
        'Geometry',
        'AP Eng Lit(12)',
        'AP World Hist(10)',
        'AP US History(11)',
        'Intro CS',
        'Art 2 Draw',
        'Graphic Design'

    ])

    master = MasterSchedule([
        first,
        second,
        third,
        fourth,
        fifth,
        sixth,
        seventh,
        eighth
    ])

    print("Input your current schedule")
    firstPeriod = input("First period class: ")
    secondPeriod = input("Second period class: ")
    thirdPeriod = input("Third period class: ")
    fourthPeriod = input("Fourth period class: ")
    fifthPeriod = input("Fifth period class: ")
    sixthPeriod = input("Sixth period class: ")
    seventhPeriod = input("Seventh period class: ")
    eighthPeriod = input("Eight period class: ")
    # Input as a word format EX: first, second,...
    userChoice = input("Which one would you like to change?\n")

    if userChoice == 'first':
        print('These are your choices for first period')
        print(first.courses)
        # input a number of course
        x = input("Which class would you like to choose?")
        print("Your choice is ", first.course_name(x))
