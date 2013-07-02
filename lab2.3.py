#!/usr/local/bin/python3
# Name: August Brenner
# File name: lab2.3.py
# Date: July 3rd, 2013

# Modules for CGI handling
import lab2modules

print("Content-type: text/html\n")
lab2modules.HTML_START("Lab 2 Exercise 2.3")
print("<h2> Methods in Classes </h2>")
python_classes = [list, dict, tuple, str, int, float]

for python_class in python_classes:
    lab2modules.table(dir(python_class), 7)

lab2modules.HTML_END
