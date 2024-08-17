
if __name__ == "__main__":
    N = int(input("Enter the number of students: "))
    students = []
    score = []
    names = []
    
    for _ in range(N):
        name = input("Enter student name: ")
        grade = float(input("Enter student grade: "))
        students.append([name, grade])
        score.append(grade)
        names.append(name)
        
    score = list(set(score))
    score.sort()
    second_lowest = score[1]
    output = [i[0] for i in students if i[1] == second_lowest]
    for i in output:
        print(i)
