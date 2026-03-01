#map_QUESTION_1
C = [0, 10, 20, 30, 40]
def tem(C):
    return (C * 9 / 5) + 32
F = list(map(tem, C))
print(f"Temprature in Fahrenheit:{F}")
## USING LAMPDA
C1 = [0, 10, 20, 30, 40]
Fahrenheit = list(map(lambda x: (x * 9 / 5) + 32, C1))
print(f"Temprature in Fahrenheit :{Fahrenheit}")
# QUESTION_2
A=['hello', 'world', 'python']
def upper(A):
    return A.upper()
R= list(map(upper, A))
print(R)
###QUESTION_3
NUM = [1, 2, 3, 4, 5]
SQUARE = list(map(lambda x:x**2,NUM))
print(f"square of list are:{SQUARE}")
##QUESTION_4
STR = ['apple', 'banana', 'cherry', 'date']
def length(STR):
    return len(STR)
L = list(map(length, STR))
print(f"length of strings are:{L}")

#FILTER QUESTION_5
NUM1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def even(NUM1):
    return NUM1 % 2 == 0
is_even = list(filter(even,NUM1))
print(f"even numbers are :{is_even}")

#QUESTION_6
NUM2 = [-5, 3, -2, 8, -1, 7, 0, -9, 4]
def is_negative(NUM2):
    return NUM2 < 0
negative = list(filter(is_negative, NUM2))
print(f"Negative numers are:{negative}")

#QUESTION_7
B=['apple', 'bat', 'cherry', 'dog', 'elephant']
def length(B):
    return len(B) >= 4

result = list(filter(length, B))
print(result)

#QUESTION_8
for i in range(1,101):
    def is_odd(i):
        return i % 3 == 0 or i % 5 ==0
odd = list(filter(is_odd, range(1,101)))
print(f"Number are divisible by 3 or 5:{odd}")

# Range QUESTION_9
for i in range(1,20,2):
    print(i)
# QUESTION_10
for b in range(50,10,-5):
    print(f"Number skipping by 5:{b}")
# QUESTION_11
for s in range(7,77,7):
    print(f"Number skipping by 7:{s}")
# QUESTION_12
for d in range(2,22,2):
    print(f"Number skipping by 2:{d}")
# Round QUESTION_13
result= round(3.14159,2)
print(result)

#QUESTION_14
L=[2.567, 3.423, 5.789, 1.234]
result_l=[round(x, 1) for x in L]
print(result_l)

#QUESTION_15
AVG = [85, 92, 78, 95, 88]
TOTAL = 0
for num in AVG:
    TOTAL += num
average = TOTAL / len(AVG)
result_avg = round(average,1)
print(f"Average number is {result_avg}")

#QUESTION_16
result_1= round(2.5)
print(result_1)
result_2= round(3.5)
print(result_2)
result_3= round(4.5)
print(result_3)
result_4= round(5.5)
print(result_4)

#QUESTION_17
k=abs(-42)
print(k)
#QUESTION_18
x1, y1 = 3, 4
x2, y2 = 7, 1

dx = abs(x2 - x1)
dy = abs(y2 - y1)

print("Absolute difference in x:", dx)
print("Absolute difference in y:", dy)
#Question_19
abs_n = [-10, 5, -3, 8, -1]
print(list(map(abs, abs_n)))

#QUESTION_20
a=15
b=47
c=a-b
print(abs(c))

# sum QUESTION_21
sun= [10, 20, 30, 40, 50]
ADD = sum(sun)
print(ADD)

# question_22
square = [x1*x1 for x1 in range(1,11)]
sum_square = sum(square)
print(sum_square)

# QUESTION_23
T= [(1, 2), (3, 4), (5, 6)]
tuple_result = sum(sum(T) for T in T)
print(tuple_result)

# Question_24


t24 = [5,10,15]
final = sum(t24, 100)
print(final)

# question_25

t25= [64, 34, 25, 12, 22, 11, 90]
sort25 = sorted(t25)
desc = sorted(t25, reverse=True)
print(sort25)
print(desc)

# QUESTION_26
t26 = ['banana', 'apple', 'cherry', 'date']
re26 = sorted(t26)
print(re26)

# QUSESTION_27
t27 =[(1, 'one'), (3, 'three'), (2, 'two')]
re27 = sorted(t27)
print(re27)

# QUESTION_28
t28 = {'apple': 3, 'banana': 1, 'cherry': 2}
re28 = sorted(t28,reverse=True)
print(re28)

# QUESTION_30
T29=[1, 2, 3, 4, 5]
re29 = sorted(T29, reverse=True)
print(re29)

# question_31
l31 = "Python"
r31 = list(reversed(l31))
print(r31)

for char in reversed(l31):
    print(char)

# question_32
rst = list(reversed(range(10,20)))
print(rst)

# question_33
r33 = "radar"
rst33 = list(reversed(r33))
print(rst33)

for char in rst33:
    print(char)

# question_34
l34 = "hello"
r34 = list(l34)
print(r34)

# QUESTION_35
T35=(10, 20, 30, 40)
R35 = list(T35)
print(R35)

# QUESTION_36
R36 = list(range(5,15))
print(R36)

# QUESTION_37
D37= {'a': 1, 'b': 2, 'c': 3}
R37 = list(D37)
print(R37)

# question_38
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'Mumbai']
r38 = dict.fromkeys(keys, values)
z38 = zip(keys, values)
print(list(z38))
print(r38)

# question_39
t39=[('a', 1), ('b', 2), ('c', 3)]
d39 = dict(t39)
print(d39)

# question_40
d40 = dict(name='Bob', age=30, profession='Engineer')
print(d40)

# question_41
d41 = dict()
d41["name"]='puru'
d41["age"]='8'
d41["class"]='2'
print(d41)

# question_42
