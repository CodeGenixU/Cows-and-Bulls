name = input("Enter your name :")
print("                                                    Welcome ",name)
print("                                                    GAME RULES")
print("There will be two persons on will be Thinker and other will be Guesser")
print("Thinker will think a number and feed its digits in internal codes by accessing the codes\
 in place of \n First digit in u \n Second digit in i \n Third digit in o \n Forth digit in p")
print("NOTE  The digits can not be same")
print("Guesser will guess th number by entering the digits in their place")
print("Cows mean the number of digits are same in the Guesser and thinker number")
print("Bulls mean the number of digits which are same and are in their correct place")
co = input("Type yes for approval : ")
u = 3
i = 5
o = 8
p = 9
n1 = int(input("First Digit : "))
n2 = int(input("Second Digit : "))
n3 = int(input("Third Digit : "))
n4 = int(input("Forth Digit : "))
cow1 = n1 is u
if cow1 == True:
    c1 = 1
else:
    c1 = 0
cow2 = n2 is i
if cow2 == True:
    c2 = 1
else:
    c2 = 0
cow3 = n3 is o
if cow3 == True:
    c3 = 1
else:
    c3 = 0
cow4 = n4 is p
if cow4 == True:
    c4 = 1
else:
    c4 = 0
cow = c1+c2+c3+c4
n1 = (n1*1000)
n2 = (n2*100)
n3 = (n3*10)
n4 = (n4*1)
num = (n1+n2+n3+n4)
str5 = num
str1 =  u
str2 =  i
str3 =  o
str4 =  p
bull1 = str(str1) in str(str5)
if bull1 == True:
    b1 = 1
else:
    b1 = 0
bull2 = str(str2) in str(str5)
if bull2 == True:
    b2 = 1
else:
    b2 = 0
bull3 = str(str3) in str(str5)
if bull3 == True:
    b3 = 1
else:
    b3 = 0
bull4 = str(str4) in str(str5)
if bull4 == True:
    b4 = 1
else:
    b4 = 0
bull = (b1+b2+b3+b4)
print("Your Cows are :", bull)
print("Your Bulls are :", cow)
while cow <= 3:
     print("                                               TRY AGAIN")
     n1 = int(input("First Digit : "))
     n2 = int(input("Second Digit : "))
     n3 = int(input("Third Digit : "))
     n4 = int(input("Forth Digit : "))
     cow1 = n1 is u
     if cow1 == True:
         c1 = 1
     else:
         c1 = 0
     cow2 = n2 is i
     if cow2 == True:
         c2 = 1
     else:
         c2 = 0
     cow3 = n3 is o
     if cow3 == True:
         c3 = 1
     else:
         c3 = 0
     cow4 = n4 is p
     if cow4 == True:
         c4 = 1
     else:
         c4 = 0
     cow = c1+c2+c3+c4
     n1 = (n1*1000)
     n2 = (n2*100)
     n3 = (n3*10)
     n4 = (n4*1)
     num = (n1+n2+n3+n4)
     str5 = num
     bull1 = str(str1) in str(str5)
     if bull1 == True:
         b1 = 1
     else:
         b1 = 0
     bull2 = str(str2) in str(str5)
     if bull2 == True:
         b2 = 1
     else:
         b2 = 0
     bull3 = str(str3) in str(str5)
     if bull3 == True:
         b3 = 1
     else:
         b3 = 0
     bull4 = str(str4) in str(str5)
     if bull4 == True:
         b4 = 1
     else:
         b4 = 0
     bull = (b1+b2+b3+b4)
     print("Your Cows are :", bull)
     print("Your Bulls are :", cow)
else:
     print("                                                CONGRATULATION", name)
     print("You won the game . We are very happy that you played our game .")
     print("                                                      THANK YOU")
