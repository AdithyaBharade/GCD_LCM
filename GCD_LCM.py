'''
Given two numbers a and b. Find the GCD and LCM of and d.
Input:
• Two positive integers a and b (1 <=a, b <=1000)
Output:
For GCD function, an integer representing the GCD of a 'and b
For LCM function, an integer representing the LCM of a and b
Sample Input:
12 18
Output:
6
36
'''
'''import math
def gcd(a, b):
    return math.gcd(a, b)
def lcm(a, b):
    return a * b // math.gcd(a, b)
# Read input
a, b = map(int, input().split())
# Calculate GCD and LCM
gcd_value = gcd(a, b)
lcm_value = lcm(a, b)
# Output results
print(gcd_value)
print(lcm_value)'''

#or

'''import math
a=int(input("enter the a value:"))
b=int(input("enter the b value:"))
res1=math.gcd(a,b)
res2=math.lcm(a,b)
print("Lcm=",res2)
print("Gcd=",res1)'''

#or



a=int(input("enter the a value:"))
b=int(input("enter the b value:"))
