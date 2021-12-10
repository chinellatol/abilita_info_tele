import sys
import math

a=2+3j
print("module of 2+3j:" , abs(a))
print("maxsize in python:" , sys.maxsize)
print("pi= ", math.pi)

str1='Hello'
str2='World'
print("Print all: ", str1, str2)
print("Print only a little part: ", str1[2:5])
print("Sum of words: ", str1 + str1  + str2)

str3='Hel'+'lo W'+'o'*5+'rld'
print("A funny phrase: ", str3)

str4='Letizia'
str5="Hello %s" %str4
print("For you: ", str5)

str6=str4.replace('a','o')
print("Your male name would be", str6)
str7=str1.strip('llo')
print("Hello is now", str7)
str8=str1.split('l')
print("Hello -ll is made by", str8)
str9=str1.upper()
print("A big Hello:", str9)