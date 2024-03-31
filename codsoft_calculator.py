#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def add(a, b):
    return a+b
def subtract(a, b):
    return a-b
def multiply(a, b):
    return a*b
def divide(a,b):
    return a/b

print("+ add")
print("- subtract")
print("* multiply")
print("/ divide")

num1 = int(input("Enter first value: "))
num2 = int(input("Enter second value: "))
operators = input("Enter operators(+,-,*,/)")
if operators=="+":
    print(num1+num2)
elif operators=="-":
    print(num1-num2)
elif operators=="*":
    print(num1*num2)
elif operators=="/":
    print(num1/num2)
print("Invalid operators")

