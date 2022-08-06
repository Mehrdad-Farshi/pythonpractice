student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# This is the scoring criteria:

# Scores 91 - 100: Grade = "Outstanding"

# Scores 81 - 90: Grade = "Exceeds Expectations"

# Scores 71 - 80: Grade = "Acceptable"

# Scores 70 or lower: Grade = "Fail"

#TODO-1: Create an empty dictionary called student_grades.
student_grades={}
#TODO-2: Write your code below to add the grades to student_grades.
for key in student_scores:
    score=student_scores[key]
    if score>=91 :
        student_grades[key]= 'Outstanding' 
    elif 90>=score>=81 : 
        student_grades[key]= 'Exceeds Expectations'
    elif 80>=score>=71 : 
        student_grades[key]= 'Acceptable'    
    elif 70>=score :
        student_grades[key]= 'Fail'    
# 🚨 Don't change the code below 👇
print(student_grades)
