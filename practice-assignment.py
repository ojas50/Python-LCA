#1. Print Student Details

print("Student Name: John Doe")
print("Address: 123 Main Street")
print("Contact_No: 9876543210")
print("Mother Tongue: English")
print("School_Name: Springfield High")
print("Year: 2026")
print("Panel: A")
print("Roll_No: 101")

#2. Multi-line Comments for Specific Fields

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

#3 Student Marks, Percentage, Highest & Lowest Subjects
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))

total_marks = sub1 + sub2 + sub3
percentage = (total_marks / 300) * 100 

marks_dict = {"Subject 1": sub1, "Subject 2": sub2, "Subject 3": sub3}
highest_sub = max(marks_dict, key=marks_dict.get)
lowest_sub = min(marks_dict, key=marks_dict.get)

print(f"\n--- Student Report ---")
print(f"Student Name: {name}")
print(f"Roll Number: {roll_no}")
print(f"Percentage: {percentage:.2f}%")
print(f"Highest Marks: {highest_sub} ({marks_dict[highest_sub]} marks)")
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
for num in range(10,101):
  if num > 1:
    for i in range(2, num):
      if (num % i) == 0:
        break
    else:
      print(num, end=" ")

#11. Sum of All Digits of a Given Number
num = int(input("Enter a number: "))
temp = abs(num)
digit_sum = 0
while temp > 0:
  digit_sum += temp % 10
  temp //= 10
print(f"The sum of the digits is: {digit_sum}")

#12. Reverse a Given Number
num = int(input("Enter a number: "))
temp = abs(num)
rev = 0
while temp > 0:
  rev = (rev * 10) + (temp % 10)
  temp //= 10
if num < 0:
  rev = -rev
print(f"Reversed number: {rev}")

#13. Check if a Given Number is a Palindrome
num_str = input("Enter a number: ")
if num_str == num_str[::-1]:
  print(f"{num_str} is a palindrome.")
else:
  print(f"{num_str} is not a palindrome.")

#14. Accept 5 Numbers and Display Their Cube Values

cubes = []
for i in range(5):
  n = float(input(f"Enter number {i+1}: "))
  cubes.append(n**3)

print("Cube values:", cubes)
#15. Display Prime Factors of a Number
n = int(input("Enter a number: "))
print(f"Prime factors of {n}:", end=" ")
i = 2
while i * i <= n:
  if n % i:
    i += 1
  else:
    n //= i
    print(i, end=" ")
if n > 1:
  print(n)
else:
  print()

#16. Pattern 1 (Left-Aligned Triangle)
rows = 4
for i in range(1, rows + 1):
  for j in range(i):
    print("*", end=" ")
  print()

#17. Pattern 2 (Spaced/Right-Aligned Triangle)
rows = 4
for i in range(1, rows + 1):
  print("  " * (rows - i), end="")
  for j in range(i):
    print("*", end=" ")
  print()

#Mini Project 1
distance = float(input("How far do you want to travel (in miles)? "))
if distance < 3:
  print("Recommendation: Ride a bicycle.")
elif distance < 300:
  print("Recommendation: Ride a motorcycle.")
else:
  print("Recommendation: Drive a supercar.")

#Mini Project 2
# Given data
cost_per_hour = 0.51
cost_per_day = cost_per_hour * 24
cost_per_week = cost_per_day * 7
cost_per_month = cost_per_day * 30
budget = 918.0
days_with_budget = budget / cost_per_day

print(f"How much does it cost to operate one server per day?")
print(f"-> ${cost_per_day:.2f}\n")

print(f"How much does it cost to operate one server per week?")
print(f"-> ${cost_per_week:.2f}\n")

print(f"How much does it cost to operate one server per month?")
print(f"-> ${cost_per_month:.2f}\n")

print(f"How many days can I operate one server with $918?")
print(f"-> {days_with_budget:.1f} days")