import math
import numpy as np
print("**********INTERNSHIP-PROJECT**********")
a = []
b = []
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
def power(x, y):
    return math.pow(x, y)
def modulo(x, y):
    return x % y
def floor_divide(x, y):
    return x // y
def sqrt(x):
    return math.sqrt(x)
def sq(x):
    return x * x
def floor(x):
    return math.floor(x)
def ceil(x):
    return math.ceil(x)
def sine(x):
    return math.sin(x)
def cosine(x):
    return math.cos(x)
def tangent(x):
    return math.tan(x)
def fact(x):
    return math.factorial(x)
def arradd(a, b):
    return np.add(a, b)
def arrsub(a, b):
    return np.subtract(a, b)
def arrmul(a, b):
    return np.multiply(a, b)
def arrdiv(a, b):
    return np.divide(a, b)
print("Select Your Choice For Arithmetic Operations...")
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")
print("5.POWER")
print("6.MODULUS")
print("7.FLOOR DIVISION")
print("8.SQUARE ROOT")
print("9.SQUARE")
print("10.FLOOR")
print("11.CEIL")
print("12.SINE")
print("13.COSINE")
print("14.TANGENT")
print("15.FACTORIAL")
print("Select Your Choice For Operations On Array...")
print("16.ARRAY ADDITION")
print("17.ARRAY SUBTRACTION")
print("18.ARRAY MULTIPLICATION")
print("19.ARRAY DIVISION")
print("20.ARRAY LENGTH")
while True:
    choice = input("Enter Your Choice For Operations :")
    if choice in ('1', '2', '3', '4', '5', '6', '7', '16','17','18','19','20'):
        if choice == '16':
            n = int(input("1st array, Enter The Number Of Elements In The Array :"))
            for i in range(0, n):
                ele = int(input())
                a.append(ele)
            n = int(input("2nd array,Enter The Number Of Elements In The Array :"))
            for i in range(0, n):
                ele1 = int(input())
                b.append(ele1)
            print(a)
            print(b)
            print("Addition Of Array Is :", np.add(a, b))
        if choice == '17':
            n = int(input("1st array, Enter The Number Of Elements In The Array :"))
            for i in range(0, n):
                ele = int(input())
                a.append(ele)
            n = int(input("2nd array,Enter The Number Of Elements In The Array :"))
            for i in range(0, n):
                ele = int(input())
                b.append(ele)
            print(a)
            print(b)
            print("Subtraction Of Array Is :", np.subtract(a, b))
        if choice == '18':
            n = int(input("1st array, Enter The Number Of Elements In The Array :"))
            for i in range(0, n):
                ele = int(input())
                a.append(ele)
            n = int(input("2nd array,Enter The Number Of Elements In The Array :"))
            for i in range(0, n):
                ele = int(input())
                b.append(ele)
            print(a)
            print(b)
            print("Multiplication Of Array Is :", np.multiply(a, b))
        if choice == '19':
            n = int(input("1st array, Enter The Number Of Elements In The Array :"))
            for i in range(0, n):
                ele = int(input())
                a.append(ele)
            n = int(input("2nd array,Enter The Number Of Elements In The Array :"))
            for i in range(0, n):
                ele = int(input())
                b.append(ele)
            print(a)
            print(b)
            print("Division Of Array Is :", np.divide(a, b))
        if choice == '20':
            n = int(input("Enter The Number Of Elements In The Array :"))
            for i in range(0, n):
                ele = int(input())
                a.append(ele)
            print("Length Of Array Is :",len(a))
        try:
            num1 = float(input("Enter The First Number :"))
            num2 = float(input("Enter The Second Number :"))
        except ValueError:
            print("Invalid Input, Please Enter A Valid Number")
            continue
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        elif choice == '5':
            print(num1, "**", num2, "=", power(num1, num2))
        elif choice == '6':
            print(num1, "%", num2, "=", modulo(num1, num2))
        elif choice == '7':
            print(num1, "//", num2, "=", floor_divide(num1, num2))
    elif choice in ('8', '9', '10', '11', '12','13','14','15'):
        num = float(input("Enter The Number :"))
        if choice == '8':
            print("Root(", num, ")=", sqrt(num))
        if choice == '9':
            print("Square(", num, ")=", sq(num))
        if choice == '10':
            print("Floor(",num,")=", floor(num))
        if choice == '11':
            print("Ceil(",num,")=", ceil(num))
        if choice == '12':
            print("Sin(", num, ")=", sine(num))
        if choice == '13':
            print("Cos(", num, ")=", cosine(num))
        if choice == '14':
            print("Tangent(", num, ")=", tangent(num))
        if choice == '15':
            print("Factorial(", num, ")=", fact(num))

        next_calculation = input("Would you like to do further calculations? (Yes/No): ")

        if next_calculation.lower() == "yes":
            continue
        else:
            print("Exited!!")
            break
