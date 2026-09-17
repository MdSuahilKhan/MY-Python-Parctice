

"""

Check whether a number is even or odd.


num = int(input("Entre the Number"))
if num % 2 ==0:
  print("even")
else:
    print("odd")



Find the largest of two numbers.


a = int(input("Entre the first largest number"))
b = int(input("Entre the second largest number"))
if a > b:
    print("largest number =",a)
else:
    print("largest number =",b)


 Check whether a person is eligible for driving license.


 a = int(input("Entre your age"))
if a >= 18:
    print("eligible for driving license" )
else:
    print("not eligible for driving license" )

Print "Pass" or "Fail" based on marks.

marks = int(input("Entre your Marks"))
if marks >= 30:
    print("pass" )
else:
    print("fail" )


Check whether a number is positive or negative.


num = int(input("Entre your Number"))
if num >= 0:
    print("postive" )
else:
    print("negative" )


Check whether a character is a vowel or consonant.


ch = input("Entre your character")
if ch in "AEIOUaeiou":
    print("vowel" )
else:
    print("consonant" )


Check if a year is leap or not.


year = int(input("Entre the year"))
if year % 4 == 0:
    print("leap year" )
else:
    print("not leap year" )


Print "Valid Password" or "Invalid Password"


password = input("Entre your password")
if password == "12345":
    print("Valid Password" )
else:
    print("InValid Password" )


Determine whether salary is taxable or not.


salary = float(input("Entre your salary"))
if salary >= 35000:
    print("salary is taxable" )
else:
    print("salary is not taxable" )


Check whether a number is greater than 50 or not.


num = int(input("Entre your number"))
if num >= 50:
    print("Greater" )
else:
    print(" Not greater" )


Python NESTED IF–ELSE


Find the largest of three numbers.

a = int(input("Entre your first number"))
b = int(input("Entre your second number"))
c = int(input("Entre your third number"))

if a > b:
    if a > c:  
         print("largest=",a )
    else:
         print("largest=",c )

else:
    if b > c:
       print("largest=",b )
    else:
         print("largest=",c )

  Check whether a number is positive, negative, or zero.


num = int(input("Entre your number"))


if num >= 0:
    if num == 0:  
         print("zero")
    else:
         print("positive")

else:
       print("negative")

 Assign grades:
● A → marks ≥ 90
● B → marks ≥ 75
● C → marks ≥ 60
● Fail → below 60


marks = int(input("Entre your marks"))

if marks >= 90:
    print("Grades A")
else:
    if marks >= 75:  
         print("Grades B")
    else:
      if marks >= 60:
       print("Grades C")
      else:
         print("Fail")

Check whether a triangle is equilateral, isosceles, or scalene.
"""


a = int(input("Entre your Side1"))
b = int(input("Entre your Side2"))
c = int(input("Entre your Side3"))

if a == b:
    if b == c:  
         print("Equilateral triangle" )
    else:
         print("sosceles triangle" )

else:
    if a == c:
       print("sosceles triangle" )
    else:
        if b == c:
         print("Isosceles triangle" )
        else:
            print("Scalene triangle")






















    
