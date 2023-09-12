students = []
students.append(("Amir", (20,30,40,90,100)))
students.append(("Timo", (60,80,90,20,100)))
students.append(("Outi", (80,90,70,100,90)))
print(students)
for student in students:
    if student[0] == "Amir":
        print(f"The name, {student[0]}")
        print(f"The grades, {student[1] }")
        ave= sum(student[1])/len(student[1])
        print(f"The avarage of the {student[0]}, is {ave}")

