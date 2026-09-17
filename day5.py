"""

Use a for loop to print numbers from 1 to 10.


for i in range ( 1,11):
        print(i)

Print all even numbers between 1 and 20.

for i in range (1,21):
    if i % 2 ==0:
          print(i)

Print the sum of numbers from 1 to 10 using a for loop.


sum=0
for i in range (1,11):
    sum= sum+i
print(sum)

Take a number from the user and print its multiplication table up to 10.

num= int (input ("entre the number"))

for i in range (1,11):
    
        print (num*i)

Take a string and count the total number of characters using a for loop.

text = input("entre the total number of characters")
count=0
for ch in text:
    count= count+1
print(count)

Print numbers from 1 to 10. Stop the loop when the number becomes 5.

for i in range(1,10):
   if i == 5:
      break
   print(i)


Print numbers from 1 to 10. Skip number 5.

for i in range(1,11):
    if i == 5:
       continue
    print(i)


Print numbers from 1 to 20. Skip all even numbers.

for i in range (1,21):
      if i % 2 == 0:
          continue
      print(i)


Print each character of the string "PYTHON". Skip the letter "O".

text = "PYTHON"
for ch in text:
    if ch == "O":
        continue
    print(ch)

 Run a loop from 1 to 5 but do nothing inside the loop using pass.


 for i in range (1,6):
 pass
print("loop")

Loop from 1 to 10. If number is 6, just use pass.

for i in range(1,11):
    if i == 6 :
        pass
    print(i)

Search for number 100 in a list. If found, print "Found". If not found, print "Not Found

num = 12,58,60,89,
for i in num:
    if num == 100:
        break
    print("found")
else:
    print("not found")


num = int (input("entre the number"))
if num<2:
   print(" not prime")
else:
    for i in range (2,num):
        if num%1 == 0:
            print("not prime")
            break
        else:
            print("prime")



for i in range(1,6):
    for j in range(1,i+1):
        print("*" ,end="")
    print()



for i in range(1,6):
    for j in range(1,i+1):
        print(i ,end="")
    print()



for i in range(1,6):
    for j in range(1,i+1):
        print(j ,end="")
    print()


 for i in range(1,6):
    for j in range(1,i+1):
        print(j+64 ,end="")
    print()




for i in range(1,6):
    for j in range(1,i+1):
        print(chr(j+64) ,end="")
    print()



for i in range(1,6):
    for j in range(1,i+1):
        print(chr(j+96) ,end="")
    print()


k=65
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(k) ,end="")
        k+=1
    print()


for i in range(1,6):
    for k in range(5,i,-1):
         print(" ",end="")
    for j in range(1,i+1):
        print("*" ,end="")
        k+=1
    print()
"""

for i in range(1,6):
    for k in range(5,i,-1):
         print(" ",end="")
    for j in range(1,i+1):
        print("*" ,end="")
        k+=1
    print()


   

















    
