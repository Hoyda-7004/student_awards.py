# Author: Hoyda Al Yahiri
# File Name: student_awards.py
# Description: This app accepts student names and GPAs and determines if a student qualifies for the Dean's List or Honor Roll.

# Initialize an infinite loop to keep accepting student records until 'ZZZ' is entered.
while True:
    last_name = input("Enter the student's last name (enter 'ZZZ' to quit): ")
    if last_name == 'ZZZ':
        break

    first_name = input("Enter the student's first name: ")
    gpa = float(input("Enter the student's GPA: "))

 # Check if the student's GPA qualifies for the Dean's List or the Honor Roll.
    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List.")
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll.")
    else:
        print(f"{first_name} {last_name} does not qualify for any awards.")
        