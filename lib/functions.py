#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
greet_programmer()

def greet(name):
    print(f"Hello, {name}!")
greet("lucy")    

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

    return "Hello, programmer!"
greet_with_default("Eva")

def add(num1, num2):
    return num1 + num2
print(add(3,5))

def halve(number):
    return number / 2
print(int(halve(8)))

