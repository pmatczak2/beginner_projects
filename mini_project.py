# Weighted Exam Score Average

# Entering how mny exams you have done
number_of_exams = int(input("Enter number of exams: "))
print(number_of_exams)

# Entering how many credits these exams cover
total_credits = int(input("Enter how many credits these exams cover: "))

# Begin wiht average of 0 and then add up prcentages form eacg exam
average = 0
for exam in range(number_of_exams):
    score = int(input("Enter exam score: "))
    exam_credits = int(input("Enter how many credits this exam covered: "))
    average = average + score*exam_credits/total_credits
print("Your average is", average)
