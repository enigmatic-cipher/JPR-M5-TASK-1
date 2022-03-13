"""
Given a number as input, print whether is it prime or not.
Input-> 29
Output_> Prime
"""

def primeNo(num):
  if (num==1):
    return "Not Prime"
  for i in range(2,num):
    if (num%i==0):
      return "Not Prime"
  else:
    return "prime"

n=29
print(primeNo(n))
