name = str(input("Plaese enter a student name : "))
students_grade_mid = False
students_grade_final = False

while not students_grade_mid:
    try:
        midterm = \
            int(input("Plaese enter student's midterm exam mark (0-100) : "))
        if midterm < 0:
            students_grade_mid = students_grade_mid
            print("Please enter valid exam mark (0-100)")
        elif midterm > 100:
            students_grade_mid = students_grade_mid
            print("Please enter valid exam mark (0-100)")
        else:
            students_grade_mid = True
    except ValueError:
        print("Please enter valid exam mark (0-100)")
    else:
        students_grade_mid = students_grade_mid

while not students_grade_final:
    try:
        final = \
            int(input("Plaese enter student's final exam mark (0-100) : "))
        if final < 0:
            students_grade_final = students_grade_final
            print("Please enter valid exam mark (0-100)")
        elif final > 100:
            students_grade_final = students_grade_final
            print("Please enter valid exam mark (0-100)")
        else:
            students_grade_final = True
    except ValueError:
        print("Please enter valid exam mark (0-100)")
    else:
        students_grade_final = students_grade_final

total_score = (midterm + final) / 2
total_score = int(total_score)

if 80 <= total_score <= 100:
    grade = "A"
elif 70 <= total_score <= 80:
    grade = "B"
elif 60 <= total_score <= 70:
    grade = "C"
elif 50 <= total_score <= 60:
    grade = "D"
elif total_score <= 50:
    grade = "F"
print(name, "has total mark as %.2f" % total_score, "grade as", grade)
