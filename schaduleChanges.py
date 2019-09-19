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
        'Coll Read(12)',
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
        'Coll Read (12)',
        'Band (MS)',


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
        'Alg 1(9)'
        'AP Stats'
        'AP Environ'
        'AP Physics'
        'English II(10)'
        
    ])

    seventh = Period([

    ])

    eighth = Period([

    ])

    master = MasterSchedule([
        first,
        second,
        third
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