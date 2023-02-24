#Single line comment:
# This is a single line comment in Python
#Inline comment:
print("Hello World") # This line prints "Hello World"
''''''''''''#Comments spanning multiple lines have''
""" or ''' on either end. This is the same as a multiline string, but
they can be used as comments:'''''
"
This type of comment spans multiple lines.
These are mostly used for documentation of functions, classes and modules.
"""
def func():
 """This is a function that does nothing at all"""
 return

#Write documentation using docstrings


def hello(name):
 """Greet someone.
 Print a greeting ("Hello") for the person with the given name.
 """
 print("Hello "+name)
class Greeter:
 """An object used to greet people.
 It contains multiple greeting functions for several languages
 and times of the day.
 """

 def hello(name, language="en"):
 #""" Say hello to a person.
 #Arguments:
 #name: the name of the person
 #language: the language in which the person should be greeted
 #"""
 print(greeting[language]+name)