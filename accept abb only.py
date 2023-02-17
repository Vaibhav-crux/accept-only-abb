# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 18:32:32 2022

@author: Vaibhav Tiwari
"""
#Accept only when last 3 will be abb & only set of {a,b}
""" TEST CASES
    1. abb
    2. abbabb
    3. bcabb
    4. abbab"""

a=input("Enter a string : ")
b=""
for i in a:
    if("a" in i or "b" in i):
        b+=i
    else:
        b+=i
        break
print(b)
if(b[-1]!='b'):
    print("Rejected")
elif(b[-3]=='a' and b[-2]=='b' and b[-1]=='b'):
    print("Accepted")
else:
    print("Rejected")
    
    
    
