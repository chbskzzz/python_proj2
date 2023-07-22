# 프로그래밍 할 때 flag 랑 bool 표현으로 while 구문에 사용하면 된다
# 동기와 책임/ 높은 의지를 유지해야한다. 뭘 하는지 공유하면 된다.
# 혼자만 하게 되면 그냥 쉬게 된다

#Dictionaries, Nesting

#grading program
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    else:
        student_grades[student] = "Good"

print(student_grades)

