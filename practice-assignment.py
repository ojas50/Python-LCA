#1. Write a python program to Print following statements as an output using print statement.

print("Student Name: John Doe")
print("Address: 123 Main Street")
print("Contact_No: 9876543210")
print("Mother Tongue: English")
print("School_Name: Springfield High")
print("Year: 2026")
print("Panel: A")
print("Roll_No: 101")

#2.In the previous code you written, modify the statements printing following fields into multi-line comments, so these fields will not be the part of the output.

print("Student Name: John Doe")
"""
Address: 123 Main Street
Contact_No: 9876543210
Mother Tongue: English
"""

print("School_Name: Springfield High")
print("Year: 2026")
print("Panel: A")
print("Roll_No: 101")

#3 Accept Student Name, Roll Number and Marks of the 3 subjects from the user. Calculate the percentage of the marks and display it. Display the Subject with Highest and lowest marks.
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))

total_marks = sub1 + sub2 + sub3
percentage = (total_marks / 300) * 100  # Assuming each subject is out of 100

marks_dict = {"Subject 1": sub1, "Subject 2": sub2, "Subject 3": sub3}
highest_sub = max(marks_dict, key=marks_dict.get)
lowest_sub = min(marks_dict, key=marks_dict.get)

print(f"\n--- Student Report ---")
print(f"Student Name: {name}")
print(f"Roll Number: {roll_no}")
print(f"Percentage: {percentage:.2f}%")
print(
    f"Highest Marks: {highest_sub} ({marks_dict[highest_sub]} marks)"
)
print(f"Lowest Marks: {lowest_sub} ({marks_dict[lowest_sub]} marks)")