# 1.
num1 = int(input("Enter a number:"))
num2 = int(input("Enter another number:"))
print(num1 + num2)

# 2.
num1 = int(input("Enter a number:"))
num2 = int(input("Enter another number:"))
print(num1 - num2)

# 3.
num1 = int(input("Enter a number:"))
num2 = int(input("Enter another number:"))
print(num1 * num2)

# 4.
num1 = int(input("Enter a number:"))
num2 = int(input("Enter another number:"))
print(num1 / num2)

# 5.
num1 = int(input("Enter a number:"))
num2 = int(input("Enter another number:"))
print(num1 % num2)

# 6.
num1 = int(input("Enter a number:"))
print(num1 ** 2)

# 7.
num1 = int(input("Enter a number:"))
print(num1 ** 3)

# 8.
num1 = float(input("Enter a number:"))
num2 = float(input("Enter another number:"))
num3 = (num1 + num2)
print(num3 / 2)

#9.
num1 = int(input("Enter a number:"))
num2 = int(input("Enter another number:"))
print(num1 == num2)

# 10.
num1 = int(input("Enter a number:"))
num2 = int(input("Enter another number:"))
if(num1 > num2):
    print(num1, "is greater than", num2)
else:
    print(num2, "is greater than", num1)

# 11.
String = "Hello"
print(String)

# 12.
String = input("Enter a string:")
print(String)

# 13.
String = input("Enter a string:")
print(String[0])

# 14.
String = input("Enter a string:")
print(String[-1])

# 15.
String = input("Enter a string:")
print(String[0:3:1])

# 16.
String = input("Enter a string:")
print(String[0:5:1])

# 17.
String = input("Enter a string:")
print(String[-1:-4:-1])

# 18.
String = "HelloWorld"
print(String[2:6])

# 19.
String = "hello"
print(len(String))

# 20.
String = str(input("Enter a String:"))
print(String.upper())

# 21.
String = str(input("Enter a String:"))
print("String.lower()")

# 22.
String = "hallo"
print(String.count("a"))

# 23.
String = "hello world"
print(String.replace("hello", "hey"))

# 24.
String = "hello world"
print(String.capitalize())

# 25.
String = "hello world"
print(String.title())

# 26.
String = "    hello world"
print(String.strip())

# 27.
String = "hello world"
print(String.find("d"))

# 28.
String = "hello world"
print(String.startswith("h"))

# 29.
String = "hello world"
print("h" in String)

# 30.
l1 = ["mango","banana","orange"]

# 31.
l1 = ["mango","banana","orange"]
print(l1[0])

# 32.
l1 = ["mango","banana","orange"]
print(l1[-1])

# 33.
l1 = ["mango","banana","orange"]
print(l1[1])

# 34.
ls = ["mango","banana","orange"]
print(len(ls))

# 35.
ls = ["mango","banana", "orange"]
ls.append("grapes")
print(ls)

# 36.
ls = ["mango","banana", "orange"]
ls.insert(1, "grapes")
print(ls)

# 37.
ls = ["mango","banana", "orange"]
ls.remove("banana")
print(ls)

# 38.
ls = ["mango","banana", "orange"]
print(len(ls))

# 39.
ls = ["mango","banana", "orange"]
ls.sort()
print(ls)

# 40.
ls = ["mango","banana", "orange"]
ls.reverse()
print(ls)

# 41.
ls = ["mango","banana", "banana", "orange"]
print(ls.count("banana"))

# 42.
ls = ["mango","banana", "orange"]
l2 = ["grapes", "kiwi"]
print(ls + l2)

# 43.
Student1 = {"Name": "Shubham", "Age": 18, "City": "jalgoan"}
print(Student1)
Student2 = {"Name": "Satyarth", "Age": 19, "City": "jalgoan"}
print(Student2)

# 44.
Numbers = {"one": 1, "two": 2, "three": 3}
print(Numbers)

# 45.
Student1 = {"Name": "Shubham", "Age": 18, "City": "jalgoan"}
Student2 = {"Name": "Satyarth", "Age": 19, "City": "jalgoan"}
print(Student1["Name"])
print(Student2["Name"])
