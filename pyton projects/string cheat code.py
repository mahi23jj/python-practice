# first='I learn coding'
# sec='  I hope   '
# this='&&I hope&&&&'
# # methods
# u=first.upper() # -> I LEARN CODING
# print(u)

# l=first.lower()# -> i learn coding
# print(l)

# r=first.replace(' ','.')# -> I.learn.coding
# print(r)

# c=sec.strip()# ->I hope -> this remove first & last  white space 
# print(c)

# c=this.strip('&')# ->I hope -> this remove first & last & element
# print(c)

# s=sec.rstrip() # -> '  I hope' this help to remove last space 
# print(s)

# li=r.split('.') # -> ['I', 'learn', 'coding'] -> slplit str based on some criteria or by defulat of space and cheged to list  
# print(li)

# j=' '.join(li) # -> it change list to string -> ['I', 'learn', 'coding'] to  I learn coding
# print(j)

# f=first.find('r') # -> 5 it out put the index of 'r
# print(f)

# str.count(s) returns the number of occurrences of substring 's' in my_str
# my_str.count('s') # => 6
# '0123123'.isdigit() # => True
# '0123123x'.isdigit() # => False
# 'abc'.isalpha() # => True
# '0123123x'.isalnum() # => True

#challenge-2
str1=''' It display: "You\'ve got an error!"\n \\n means a new line.\n \\ is known as the escape character.'''
print(str1)

#challenge-3
# val=float(input())
# result=val*30.48
# print(f"{val}ft in centimeter will be {result:.2f}cm")

#challenge-4 (palindrome)
# str2=input()
# rev=str2[::-1]
# print(str2==rev)

#challenge-5
# x= 'Hello!'
# t=x[:2]+x[4:]
# print(t)

# #challenge-6
# str4='mamamama'
# f=str4[0]
# print(f+str4[1:].replace(f,'$'))

# #challenge-7
# str5='mamamama'
# num=int(input())
# print(str5[:num]+str5[num+1:])

# #challenge-8
pi=3.1415
r=float(input())
area=pi*r**2
print(f"{area:.f4}")

#challenge-12
n = 12384756982
n_comma = f'{n:,}'# :, inside the curly braces {} is a format specifier
# that tells Python to include commas as thousand separators.

print(n_comma)











