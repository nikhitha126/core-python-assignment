def calculate(marks):
    return round(sum(marks) / len(marks), 2)
def top_performer(students_marks):
    global topper
    average = {}
    for student, marks in students_marks.items():
        average[student] = calculate(marks)
        topper = max(average, key=average.get)
    return average, topper
students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}
averages, topper = top_performer(students)
print("Average Marks:", averages)
print("Top Performer:", topper)
