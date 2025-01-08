# Function to calculate average and determine grade
def calculate_grade(marks):
    average = sum(marks) / len(marks)
    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    else:
        grade = 'D'
    return average, grade

# Input marks for three subjects
marks = []
for i in range(1, 4):
    mark = float(input(f"Enter the marks for subject {i}: "))
    marks.append(mark)

# Calculate average and determine grade
average, grade = calculate_grade(marks)

# Print the result
print(f"The average marks are: {average:.2f}")
print(f"The grade is: {grade}")