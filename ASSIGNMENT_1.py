
MY_NAME =("AKANKSHA")
AGE =(35)
print(MY_NAME)
print(AGE)

 ##data type INTEGER DATA TYPE

student_roll_no =(1,2,3,4,5,6,7,8,9,10)
print(f"roll_no : {student_roll_no}")

student_weight = (20.5,24.4,25.30,27.30,21.34,15.30,16.70,18.20,23.20,12.20)
print(f"weight_of_students:{student_weight}")

name_of_student=("pratyus","mihit","swara","sandy","candy","coca","cumin","jingle","vini","tiny")
print(f"name_of_student:{name_of_student}")


from_class_2 = True
print(f"student_are_from_class_two:{from_class_2}")

## condition
A = int(input("Enter a number: "))
if A>0:
    print("number is positive")
elif A==0:
    print("number is ZERO")
else:
    print("number is negative")

# for loop
for i in range(1,11):
    square = [i*i for i in range(1,11)]
    print(i)
print(f"squre_of_number:{square}")

# for loop with condition
for i in range(1,10):
    if i%2 == 0:
        print(f"even number:{i}")

# while loop
i = 1
while i <= 5:
    print(i)
    i += 1
# function
x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

ADD = x+y
print(ADD)

# FUNCTION WITH CONDITION
def result(TOTAL_MARKS):
  if TOTAL_MARKS >=40:
    return "PASSED"
  else: return "FAIL"
NUMBER = int(input("Enter TOTAL_MARKS:"))
res= result(NUMBER)
print(res)

# list loop
mark_lists =[55,70,48,89,90,10]
total = 0
for mark in mark_lists :
    total += mark

    avg = total/len(mark_lists)

print(f"total={total}")

print(f"avaragr={avg}")



# fruit list
fruits = ["apple", "banana", "cherry"]
print(fruits)
print(fruits[0])
print(fruits[2])
fruits.append("orange")
print(fruits)

### TUPLE
PAITENTS =(("ashu",34,"mumbai"),("nidhi",30,"pune"))
print(PAITENTS[1][0])
print(PAITENTS[1][1])
print(PAITENTS[1][2])

# dictionary
teachers ={1:{"name":"priya","age":25,"country":"India"},
           2:{"name":"shankey","age":26,"country":"uk"}
           }
print(teachers.keys())
print(teachers.values())
for key, value in teachers.items():
    print(key, "<>", value)
#

CLASS_2 ={1:{"name":"priya","mark":25},
           2:{"name":"shankey","mark":26}
           }

for key, value in CLASS_2.items():
    print(key, "<>", value)

    ### tuple_list
    CLASS_3= [
    ("Rahul", 78),
    ("Aman", 32),
    ("Neha", 56),
    ("Priya", 40)
]
    results = {}

    for name, marks in CLASS_3:
        if marks >= 40:
            results[name] = "Pass"
        else:
            results[name] = "Fail"


    def calculate_average(CLASS_3):
        total = 0
        for _, marks in CLASS_3:
            total += marks
        return total / len(CLASS_3)
    average_marks = calculate_average(CLASS_3)

    for name, status in results.items():
        print(f"{name} : {marks} : {status}")


with open("sample.txt","r") as file:
    lines = file.readlines()
    lines.insert(1, "103|rahul|28\n")

print(lines)

print("\nAverage Marks:", average_marks)