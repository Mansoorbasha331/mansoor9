# ----> Assesment
# ----> Assesment
# 1.) dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# Merge two python dictionary
# o/p --> {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# 2.)Python Program to determine if 
# the given Sets Are Disjoint 
# or Not without Using Inbuilt-in Functions

# set1 = {'Python', 'Java', 'Data Science'}
# set2 = {'ML', 'AI', 'R Language', 'Python'}
# set3 = {'Data Analytics', 'Robotics', 'Deep L
# 3.)list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]

# O/P --> ['My', 'name', 'is', 'Kelly']
Umar faruk
09:31
d1={'Ten':10,'Twenty':20,'Thirty':30}
# d2={'Thirty':30,'fourty':40,'fifty':50}
# d1.update(d2)
# print(d1)
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

result = [list1[i] + list2[i]
for i in range(len(list1))]

print(result)

