# (1) Python Basics - Practice assignment
#1. Print Student Details

print("Student Name: Ojas")
print("Address: 123 Main Street")
print("Contact_No: 1234567890")
print("Mother Tongue: English")
print("School_Name: Springfield High")
print("Year: 2026")
print("Panel: A")
print("Roll_No: 101")

#2. Multi-line Comments for Specific Fields
print("Student Name: Ojas")
"""
Address: 123 Main Street
Contact_No: 1234567890
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

#4. Check if a Number is Positive, Negative, or Zero
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

# Mini Project 1
distance = float(input("How far do you want to travel (in miles)? "))
if distance < 3:
  print("Recommendation: Ride a bicycle.")
elif distance < 300:
  print("Recommendation: Ride a motorcycle.")
else:
  print("Recommendation: Drive a supercar.")

# Mini Project 2
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

# (2) List Practice

#1. Create a list of 5 integers and display/access elements
my_list = [10, 20, 30, 40, 50]
print("List:", my_list)
print("Element at index 0:", my_list[0])
print("Element at index 2:", my_list[2])

#2. Append a new item to the end of the list
my_list = [1, 2, 3]
my_list.append(4)
print("Appended list:", my_list)

#3. Reverse the order of items in the list
my_list = [1, 2, 3, 4]
my_list.reverse()
print("Reversed list:", my_list)

#4. Print number of occurrences of a specified element
my_list = [1, 2, 3, 2, 4, 2]
count = my_list.count(2)
print("Occurrences of 2:", count)

#5. Append items of list1 to list2 in the front
list1 = [1, 2]
list2 = [3, 4]
list2 = list1 + list2
print("Combined list:", list2)

#6. Insert a new item before the second element
my_list = [10, 30, 40]
my_list.insert(1, 20)
print("Updated list:", my_list)

#7. Remove the item from a specified index
my_list = [10, 20, 30, 40]
del my_list[1]
print("List after removal:", my_list)

#8. Remove the first occurrence of a specified element
my_list = [10, 20, 30, 20, 40]
my_list.remove(20)
print("List after removing first 20:", my_list)

#9. Accept 20 values and perform operations
vals = []
for i in range(20):
  vals.append(int(input("Enter value: ")))

# a) Count similar elements and print index
seen = set()
for i in range(len(vals)):
  val = vals[i]
  if vals.count(val) > 1 and val not in seen:
    seen.add(val)
    indices = [idx for idx, x in enumerate(vals) if x == val]
    print("Element", val, "appears at indices:", indices)

# b) Count even and odd values
even_count = sum(1 for v in vals if v % 2 == 0)
odd_count = len(vals) - even_count
print("Even count:", even_count, "Odd count:", odd_count)

# c) Count positive and negative values
pos_count = sum(1 for v in vals if v > 0)
neg_count = sum(1 for v in vals if v < 0)
print("Positive count:", pos_count, "Negative count:", neg_count)

#10. Accept 10 values, sort, and display length
vals = []
for i in range(10):
  vals.append(int(input("Enter value: ")))

print("Sorted list using sorted():", sorted(vals))
vals.sort(reverse=True)
print("Sorted list descending using sort():", vals)
print("Length of list:", len(vals))

#11. Merge two lists using +
list1 = input("Enter list 1 elements separated by space: ").split()
list2 = input("Enter list 2 elements separated by space: ").split()
merged = list1 + list2
print("Merged list:", merged)

#12. Create an acronym from a phrase
phrase = input("Enter a phrase: ")
acronym = "".join([word[0].upper() for word in phrase.split()])
print("Acronym:", acronym)

#13. Abbreviation of a month given its number
months = [
    "",
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]
num = int(input("Enter month number (1-12): "))
print("Month abbreviation:", months[num] if 1 <= num <= 12 else "Invalid")

#(3) Dictionary Practice

#1. Add key and value to a dictionary
d = {0: 10, 1: 20}
d[2] = 30
print("Updated dictionary:", d)

#2. Concatenate dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic1.update(dic2)
dic1.update(dic3)
print("Concatenated dictionary:", dic1)

#3. Check if key exists
d = {1: 10, 2: 20}
key = int(input("Enter key to check: "))
print("Key exists:", key in d)

#4. Iterate over keys, values, and both
d = {1: 10, 2: 20, 3: 30}
print("Keys:", list(d.keys()))
print("Values:", list(d.values()))
for k, v in d.items():
  print("Key:", k, "Value:", v)
  
#5. Dictionary with numbers 1-15 as keys and squares as values
d = {i: i**2 for i in range(1, 16)}
print(d)

#6. Sum all values in a dictionary
d = {'a': 10, 'b': 20, 'c': 30}
print("Sum:", sum(d.values()))

#7. Student information dictionary operations
my_dict = {
    'name': 'John',
    'panel': 'A',
    'rollno': 101,
    'marks': 85,
    'grade': 'A',
}
my_dict['age'] = 20  # Add
del my_dict['grade']  # Delete
print("Student Info:", my_dict)

#8. Convert list to dictionary
list1 = ['name', 'panel', 'rollno']
list2 = ['ABC', 'B', 34]
my_dict = dict(zip(list1, list2))
print(my_dict)

#9. Convert dictionary to lists of keys and values
my_dict = {'name': 'ABC', 'panel': 'B', 'rollno': 34}
print("Keys:", list(my_dict.keys()))
print("Values:", list(my_dict.values()))

#10. Find mean of values of dictionary
mydict = {'marks1': 23, 'marks2': 123, 'marks3': 43, 'marks4': 13, 'marks5': 39}
vals = list(mydict.values())
print("Mean:", sum(vals) / len(vals))

#11. Sort elements of dictionary using sorted()
my_dict = {
    'name': 'ABC',
    'panel': 'B',
    'rollno': 34,
    'marks': [65, 87, 67, 94],
}
print("Sorted keys:", sorted(my_dict))

#(4) Tuple Problems

#1. Print 4th element from first and 4th from last
t = (10, 20, 30, 40, 50, 60, 70)
print("4th from start:", t[3])
print("4th from last:", t[-4])

#2. Check whether element exists in a tuple
t = (10, 20, 30, 40)
val = int(input("Enter value to check: "))
print("Exists:", val in t)

#3. Convert a list into a tuple
my_list = [1, 2, 3, 4]
print(tuple(my_list))

#4. Find index of an item in a tuple
t = (10, 20, 30, 20, 40)
print("Index:", t.index(30))

#5. Replace last value of tuples in a list to 100
sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
new_list = [tuple(list(item[:-1]) + [100]) for item in sample_list]
print(new_list)

#(5) Set Practice
#1. Remove given item from set
s = {10, 20, 30, 40}
s.discard(20)
print(s)

#2. Intersection of sets
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(s1.intersection(s2))

#3. Union of sets
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1.union(s2))

#4. Maximum and minimum value in a set
s = {15, 3, 89, 22, 7}
print("Max:", max(s))
print("Min:", min(s))
