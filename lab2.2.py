#!/usr/local/bin/python3
# Name: August Brenner
# File name: lab2.2.py
# Date: July 3rd, 2013

# Modules for CGI handling
import cgi
import lab2modules

print("Content-type: text/html\n")


def HTML_FORMAT_SELECT_FORM(formats):

    HTML_FORMATS = ""

    for format in formats:
        HTML_FORMATS += '<input type="radio" name="format" value="'\
                        + format + '" /> ' + format.title()

    HTML_FORM = """
        <form action="lab2.2.py" method="post" target="_self">""" + HTML_FORMATS + """
        <input type="submit" value="Select Format" />
        </form>
        """
    return HTML_FORM


# fib() generates Fibonacci numbers
def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


# instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
if form.getvalue('format'):
    selected_format = form.getvalue('format')
else:
    selected_format = "decimal"


lab2modules.HTML_START("Lab 2 Exercise 2.2")
print("<h2> First 50 Fibonacci numbers in " + selected_format + "</h2>")

# generates html form
formats = ["decimal", "hex", "octal", "floating point"]
print(HTML_FORMAT_SELECT_FORM(formats))

# generate a list of the first 50 Fibonacci numbers wih list comprehension
fib_list = list(range(50))
fib_list = [fib(x) for x in fib_list]

# handle the different format cases
if selected_format == "decimal":
    lab2modules.table(fib_list, 6)
elif selected_format == "hex":
    fib_list = [hex(x) for x in fib_list]
    lab2modules.table(fib_list,6)
elif selected_format == "octal":
    fib_list = [oct(x) for x in fib_list]
    lab2modules.table(fib_list, 6)
elif selected_format == "floating point":
    fib_list = [float(x) for x in fib_list]
    lab2modules.table(fib_list, 6)


lab2modules.HTML_END
