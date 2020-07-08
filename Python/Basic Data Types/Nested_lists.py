class_list = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        class_list.append([str(name) , score])

def second_lowest_grade(class_list):
    grade_set = set(_[1] for _ in class_list)
    grade_list = sorted(grade_set)
    second_lowest_grade = grade_list[1]
    result = [_[0] for _ in class_list if _[1] == second_lowest_grade]
    result = sorted(result)
    return result

t = second_lowest_grade(class_list)
for x in t:
    print(x)
