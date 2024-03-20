# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2.)Find the uncommon words from 2 strings

# # s1 = "Hello how are you"
# s2 = "Hello how is"

# 3.)Wrire a code print the 8th fibanochi number
def f1(a,b):
    c=a*b
    return c
#print(f1(6,8))
obj=f1(6,8)
obj1=f1(4,6)


def gracemark(object):
    print(object+4)
gracemark(obj)
gracemark(obj1)
#123

# 123
def palindrome(n):
    string = str(n)
    rev = str(n)[::-1]
    if string==rev:
         print(n, "Palindrome")
    else:
         print("Not palindrome")
a = int(input("Enter the value: "))
palindrome(a)

# ? Based on the declaration of parameter and args
# ? functions are divide into 5 catagories

# Positional args
# keyword args
# default args
# variable length args
# keyword variable length args

# * positional args
# ? The position of parameter have to be same as position as arguments
# Eg:1
def profile(name, phone, mark):
    txt = "My name is {}. My phone number is{}.I got {} marks."
    print(txt.format(name, phone, mark))
profile("Pavan", 9999999999, 95) # unexpected output

# profile(name="Mansoor", 9999999999, marks=95) # error -> positional args follow keyword args
# profile(name="Mansoor", 9999999999, marks=95) # error -> name has multiple values
# profile(name="Mansoor", 9999999999, marks=95)

# * Defualt args
# ! Eg:2
def profile(name, phone, place="Kadapa"):
    if place == "Kadapa" or place=="KADAPA" or place=="kadapa":
       txt = "My name is {}.My phone number is {}.I am from {}."
       print(txt.format(name, phone, place))
    else:
        print("You are not eligible to signup")
    profile("Mann",9999999999)


# * variables length params
# ! Eg:1
# To pass more than 1 arg to a parameter means we use variables length args
# To convert normal parameter to variables length param, add * to there prefix of param

def profile(*name):
    print("my name is",Mann)
profile("Mann", "jan", "prit")


name = "Mann", "jan", "prit"
for val in name:
    print("my name is", name)
    
    def profile (*name, age):
    for val in name:
        print("My name is ",val,"my age is ",age)
profile("pramod", 'name2', 'name3', 26) # error --> age has no args


'''
        
def profile (age,*name):
    for val in name:
        print("My name is ",val,"my age is ",age)
profile(26, "mansoor", 'name2', 'name3'

[1:43 pm, 19/03/2024] Pawan Kalyan: '''
Problem Statement  Given a string S(input consisting) of ‘*’ and ‘#’. 
The length of the string is variable. The task is to find the minimum number of ‘*’ 
or ‘#’ to make it a valid string. The string is considered valid if the number of ‘*’ 
and ‘#’ are equal. The ‘*’ and ‘#’ can be at any position in the string.
Note : The output will be a positive or negative integer based on number of ‘*’ 
and ‘#’ in the input string.

(*>#): positive integer
(#>*): negative integer
(#=*): 0
Example 1:
Input 1:

###*   -> Value of S
Output :

0   → number of * and # are equal
'''
# * Variables length params
# ! Eg:1
# To pass more then 1 arg to a parameter means we use variable length args
# To convert normal parameter to variable length param,add * to their prefix …

[1:43 pm, 19/0  3/2024] Pawan Kalyan: '''
Problem Statement – Given a string S(input consisting) of ‘*’ and ‘#’. 
The length of the string is variable. The task is to find the minimum number of ‘*’ 
or ‘#’ to make it a valid string. The string is considered valid if the number of ‘*’ 
and ‘#’ are equal. The ‘*’ and ‘#’ can be at any position in the string.
Note : The output will be a positive or negative integer based on number of ‘*’ 
and ‘#’ in the input string.

(*>#): positive integer
(#>*): negative integer
(#=*): 0
Example 1:
Input 1:

###*   -> Value of S
Output :

0   → number of * and # are equal

# * Variables length params
# ! Eg:1
# To pass more then 1 arg to a parameter means we use variable length args
# To convert normal parameter to variable length param,add * to their prefix …
#! Eg : 5
                                         
# Eg:-1
'''
def price(**price_list):
    print(price_list)
price(shirt = 1000, iphone = 800000)    
'''
# Eg:-2
'''
d1 = {"a":100, "b":200, "c":300}
d1 = dict(a=100, b=200, c=
# ex:3
# create of a method
#When the function is created with a class is called as method
#class person:
#    def display(person):
#        print("Hello welcome to classes")
#p=person()
#p.display()

class person1:
    frame = "malli" # attribute or static variable
    lname = "T"

    def first_name(person):
        print(person.frame)

    def full_name(person):
        print(person.frame+" " +person.lname)

p = person1()
p.first_name()
p.full_name()
 
