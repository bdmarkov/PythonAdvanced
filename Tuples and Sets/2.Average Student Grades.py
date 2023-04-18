n = int(input())

def calclulate_avg(values):
    return sum(values) / len(values)

dic = {}

for i in range(n):
    name, grade = input().split()
    grade = float(grade)
    if name not in dic:
        dic[name] = [grade]
    else:
        dic[name].append(grade)

for student, grades in dic.items():
    grades_string = ' '.join(map(lambda grade: f'{grade:.2f}' , grades))
    avg_grade = calclulate_avg(grades)
    print(f"{student} -> {grades_string} (avg: {avg_grade:.2f})")