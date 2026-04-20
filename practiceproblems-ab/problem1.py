# q1 :given a  list of tuples with info (name,subject):
   # 1. list all unique course
   # 2.list student enrolled in English
   # 3.create dictionary(student, set of courses)

info = [
     ("Alice","math"),
     ("Bob","science"),
     ("Alice","science"),
     ("Charlie","math"),
     ("Bob","math"),
     ("Alice","English"),
     ("Charlie","English"),
 ]
unique= set()
for tup in info:
    unique.add(tup[1])    
print(unique) 

for name,course in info:
    if (course=="English"):
       print(name)