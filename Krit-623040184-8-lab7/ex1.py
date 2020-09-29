class Student:

    def __init__(self, name, *course_ids):
        self.name = name
        self.course_ids = course_ids


if __name__ == '__main__':
    manee = Student("Manee", "842004")
    mana = Student("Manee", "842004", "842005", "813701")
    chujai = Student("Chujai", "842004", "842005")
    print(f"{manee.name} registered courses {manee.course_ids}")
    print(f"{mana.name} registered courses{mana.course_ids})")
    print(f"{chujai.name} registered courses{chujai.course_ids})")
