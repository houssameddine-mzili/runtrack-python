def round_grades(grades):
    rounded_grades = []

    for grade in grades:
       
        if grade >= 40:
            next_multiple_of_five = (grade + 4) // 5 * 5
            if next_multiple_of_five - grade < 3:
                rounded_grades.append(next_multiple_of_five)
            else:
                rounded_grades.append(grade)
        else:
            rounded_grades.append(grade)

    return rounded_grades

original_grades = [84, 29, 57, 99, 82, 38, 77, 70]
rounded_grades = round_grades(original_grades)
print(rounded_grades)

