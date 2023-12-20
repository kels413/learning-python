# input a list of student scores
# function to get the highest score of students
student_scores = input("please input grades of student ")
# student_scores[10]

student_scores = student_scores.split()
student_scores_length = len(student_scores)
highest_score = int(student_scores[0])
for i in range(0, student_scores_length):
    student_scores[i] = int(student_scores[i])
    if student_scores[i] > highest_score:
        highest_score = student_scores[i]

print("highest score == ", highest_score)
