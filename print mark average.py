n = int(input("enter no of students:"))
student_marks = {}
print ("first write name space write marks.\n")
for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input("student name:")
l1 = list(student_marks[query_name]) 
addition = sum(l1)
result = addition/len(l1)
print('%.2f'% result)
#2f use for flot result print 
