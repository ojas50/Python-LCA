#Create list1 consisting of student names and list2 with their marks, find highest marks and who got them
list1 = ["swar", "vinayak", "animesh"]
list2 = [96,95,93]

print("Names of students:", list1)
print("Marks:", list2)

highest_mark = max(list2)

highest_index = list2.index(highest_mark)
top_student = list1[highest_index]

print("Highest marks:", highest_mark)
print("Top student:", top_student) 

#Accpet any five numbers in a list and find a specific one 
numbers = []
for i in range(1,6):
    num=int(input("Enter number: "))
    numbers.append(num)

num1 = int(input("Find specific number:"))
if num1 in numbers:
    print("Number found")
else:
    print("Not found")