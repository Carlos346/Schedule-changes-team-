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
        'Algebra II',
        'Pre-Cal',
        'AP Bio',
        'Chem (9/10)',
        'Creative Writing',
        'AP Human Geo (9)',
        'AP US/AP Macro (12)',
        'Math 6 C (TTM)',
        'Art 2 Draw',
        'PE',
        'Coll Read (12)'


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
        'AP Cal',
        'Geometry',
        'Ind Skill Build',
        'AP Chemistry',
        'AP Eng Lang(11)',
        'AP Human Geo(9)',
        'Model UN',
        'Practicum',
        'Ind Skill Build'
        'AP CSP',
        'Jazz Band',

    ])

    sixth = Period([
        'Alg 1(9)',
        'AP Stats',
        'AP Environ',
        'AP Physics',
        'English II(10)',
        'Intro CS',
        'Art 3 Draw',
        'Health / PACE',
        'Graphic Design'

    ])

    seventh = Period([
        'Algebra II',
        'Pre - Cal',
        'Bio(9)',
        'Chem(9 / 10)',
        'AP Human Geo(9)',
        'AP Psych / SSAS',
        'AP CSA',
        'AP Studio Art',
        'PE',
        'Graphic Design'
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
    # Input as a word format EX: first, second, third, ...
    userChoice = input("Which one would you like to change?\n")

    # first Period
    if userChoice == "first":
        print('These are your choices for first period')
        print(first.courses)
        # input a number of course
        l = int(input("Which class would you like to choose?\n"))
        print("Your choice is", first.course_name(l))
        firstPeriod = first.course_name(l)

    # Second Period
    if userChoice == "second":
        print('These are your choices for second period')
        print(second.courses)
        # input a number of course
        l = int(input("Which class would you like to choose?\n"))
        print("Your choice is", second.course_name(l))
        secondPeriod = second.course_name(l)

    # Third Period
    if userChoice == "third":
        print('These are your choices for third period')
        print(third.courses)
        # input a number of course
        l = int(input("Which class would you like to choose?\n"))
        print("Your choice is", third.course_name(l))
        thirdPeriod = third.course_name(l)

    # Fourth Period
    if userChoice == "fourth":
        print('These are your choices for fourth period')
        print(fourth.courses)
        # input a number of course
        a = int(input("Which class would you like to choose?\n"))
        print("Your choice is", fourth.course_name(a))
        fourthPeriod = fourth.course_name(a)

    # Fifth Period
    if userChoice == "fifth":
        print('These are your choices for fifth period')
        print(fifth.courses)
        # input a number of course
        b = int(input("Which class would you like to choose?\n"))
        print("Your choice is", fifth.course_name(b))
        fifthPeriod = fifth.course_name(b)

    # Sixth Period
    if userChoice == "sixth":
        print('These are your choices for sixth period')
        print(sixth.courses)
        # Input a number of course
        c = int(input("Which class would you like to choose?\n"))
        print("Your choice is", sixth.course_name(c))
        sixthPeriod = sixth.course_name(c)

    # Seventh Period