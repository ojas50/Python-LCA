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

# 4. Check if a Number is Positive, Negative, or Zero
num = float(input("Enter a number: "))
if num > 0:
  print("The number is Positive.")
elif num < 0:
  print("The number is Negative.")
else:
  print("The number is Zero.")

#5. Check if a Number is Even or Odd
num = int(input("Enter an integer: "))
if num % 2 == 0:
  print("The number is Even.")
else:
  print("The number is Odd.")

#6. Check Same Last Digit for Two Non-Negative Values\
num1 = int(input("Enter first non-negative value: "))
num2 = int(input("Enter second non-negative value: "))
if num1 % 10 == num2 % 10:
  print("True")
else:
  print("False")

#7.1 Print Numbers from 1 to 10 in a Single Row with Tab Space
for i in range(1,11):
  print(i, end="\t")
print()

#7.2 Print Numbers from 1 to 10 always on a new line
for i in range(1,6):
  print(i, end="\n")
  print

#8. Print Even Numbers Between 23 to 57 (Separate Rows)
for i in range(23,58):
  if i % 2 == 0:
    print(i)

#9. Check if a Given Number is Prime or Not
num = int(input("Enter a number: "))
if num <= 1:
  print("Not a prime number")
else:
  is_prime = True
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      is_prime = False
      break
  if is_prime:
    print(f"{num} is a Prime number.")
  else:
    print(f"{num} is not a Prime number.")

#10. Print Prime Numbers Between 10 to 99
print("Prime numbers between 10 and 99:")
for num in range(10, 100):
  is_prime = True
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      is_prime = False
      break
  if is_prime:
    print(num, end=" ")
print()
