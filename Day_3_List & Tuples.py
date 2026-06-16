# task 1.
fruit = ["Mango","litchi","banana","Apple"]
print(fruit)

# task 2.
numbers = [1,2,3,4]
print(numbers[2])

# task 3.
numbers = [1,2,3,4]
print(numbers[-1])

# task 4.
t1 = ("blue","red","yellow","grey","black")
print(t1)

# task 5.
t2 = ("hello", 2, 3)
print(t2[0])

#task 6.
t3 = ["hello","hey","howdy"]
print(len(t3))

# task 7.
t4 = ("hello","hey","howdy")
print(len(t4))

# task 8.
ls = ["hello","howdy","hey"]
ls.append("howey")
print(ls)

# task 9
ls = ["hello","howdy","hey"]
ls.remove("howdy")
print(ls)

# task 10
t = (9,)
print(t)

# task 11
ls = ["hello","howdy","hey","apple"]
print("apple" in ls)

# task 12
ts = ("hello","howdy","hey",10)
print(10 in ts)

# task 13
ls = ["hello","howdy","hey","apple","mango"]
print(ls[1:4:1])

# task 14
ls = ["hello","howdy","hey"]
print(ls[-1::-1])

# task 15
tp = ("hello","howdy","hey")
print(tp[-1::-1])

# task 16
ls = ["hello","howdy","hey","hlw","whats up"]
ls.insert(2,"help")
print (ls)

# task 17
ls = ["hello","howdy","hey","hlw","whats up"]
ls.sort()
print(ls)

# task 18
ls = ["hello","howdy","hey","hlw","whats up"]
ls.sort(reverse=True)
print(ls)

# task 19
ls = ["hello","howdy","hey","hlw","whats up","hey"]
print(ls.count("hey"))

# task 20
ls = ["hello","howdy","hey","hlw","whats up"]
print(ls.index("howdy"))

# task 21
ls = ("hello","howdy","hey","hlw","whats up","hello")
print(ls.count("hello"))

# task 22
ls = ("hello","howdy","hey","hlw","whats up","hello")
print(ls.index("hlw"))

# task 23
ls = ["hello","howdy","hey","hlw","whats up"]
l2 = [19,20,21]
print(ls + l2)

# task 24
tp = ("hello","howdy","hey","hlw","whats up","hello")
t2 = ("hell","heaven")
print(tp + t2)

# task 25
ls = ["hello","howdy","hey","hlw","whats up"]
print(ls*3)

# task 26
ls = ("hello","howdy","hey","hlw","whats up","hello")
print(ls*2)

# task 27
ls = ["hello","howdy","hey","hlw","whats up"]
tp = tuple(ls)
print(tp,type(tp))

# task 28
tp = ("hello","howdy","hey","hlw","whats up")
ls = list(tp)
print(tp,type(tp))

# task 29
ls = ["hello","howdy","hey","hlw","whats up","hello",[1,2,3]]
print(ls[6][1])

# task 30
ls = ("hello","howdy","hey","hlw","whats up","hello",[1,2,3])
print(ls[6][2])

# task 31
ls = ["hello","howdy","hey","hlw","whats up"]
for x in ls:
    print(x) 

# task 32
tp = ("hello","howdy","hey","hlw","whats up","hello")
for x in tp:
    print(x)

# task 33
square = [x**2 for x in range(1,11)]
print(square)

# task 34
even = [x for x in range(0,101) if x%2 == 0]
print (even)

# task 35
ls = [1,4,5,10,11]
print(max(ls))
print(min(ls))

# task 36
ls = [1,4,5,10,11]
print(sum(ls))

# task 37
ls = [1,4,5,10,11]
l1 = ls
print(l1)

# task 38
tp = (10,12,19)
a,b,c = tp
print(a,b,c)

# task 39
tp = (10,12,19)
a,b,c = tp
d = a
a = b
b = c
c = d
print(a,b,c)

# task 40
matrix = [
    [44,55,66,],
    [33,22,11],
    [77,88,99]
    ]

# task 41
print(matrix[0])
print(matrix[1])
print(matrix[2])

#task 42
Stud = input("Enter student name: "), int(input("Enter student age: ")), input("Enter student grade: ")
Student = tuple(Stud)
print("Name:", Student[0])
print("Age:", Student[1])
print("Grade:", Student[2])
print("Type:", type(Student))

# task 43
no1 = int(input("Enter first number: "))
no2 = int(input("Enter second number: "))
no3 = no1, no2
print(type(no3))
print("Numbers:", no3)
print("Sum:",(no1 + no2))

# task 44
no1 = (input("Enter Name: "), int(input("Enter Marks: ")))
print("Name:", no1[0])
print("Marks:", no1[1])

# task 45
Marks = (90,60,80,70,50)
print("Sorted Marks:", sorted(Marks))