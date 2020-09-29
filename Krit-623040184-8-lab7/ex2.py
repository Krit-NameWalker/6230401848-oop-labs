class Student:
    university_name = "Khon Kaen University"

    def __init__(self, name, *course_ids):
        self.name = name
        self.course_ids = course_ids

    def print(self):
        print(f"{self.name} registered courses {self.course_ids}")


if __name__ == '__main__':
    manee = Student("Manee", "842004")
    mana = Student("Manee", "842004", "842005", "813701")
    chujai = Student("Chujai", "842004", "842005")
    manee.print()
    mana.print()
    chujai.print()
    print(f"These students are in {Student.university_name}")