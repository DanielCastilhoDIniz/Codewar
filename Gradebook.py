
def get_grade(s1, s2, s3):
    return {6:'D', 7:'C', 8:'B', 9:'A', 10:'A'}.get((s1 + s2 + s3) / 30, 'F')

print(get_grade(67,67,67))



def get_gradeA(s1, s2, s3):
    average = float((s1 +s2 + s3)/3)
    if average < 60:
        grade = "F"
    elif average >=60 and average < 70:
        grade = "D"
    elif average >=70 and average < 80:
        grade = "C"
    elif average >=80 and average < 90:
        grade = "B"
    else:
        grade = "A"     
    return grade

print(get_gradeA(67,67,67))