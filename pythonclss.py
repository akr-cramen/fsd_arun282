#2/9/25

#greatest of three
'''a=int(input("enter 1st number: "))
b=int(input("enter 2st number: "))
c=int(input("enter 3st number: "))
if a>b:
    if a>c:
        print("a is largest of three")
    else:
        print("c is largest of three")
else:
    if b>c:
        print("b is largest of three")
    else:
        print(" is largest of three")'''

#honors>95%, first division >=60, 2nd divisoin >=45, 3rd divion >=30, fail<30
'''a=float(input("enter the percentage scored: "))
if a>95 or a==95:
    print("honors scored!")
elif a>=60 and a<95:
    print("1st division scored!")
elif a>=45 and a<60:
    print("2nd division scored!")
elif a>=30 and a<45:
    print("3rd division scored!")
else:
    print("fail")
'''
#goi announce pension to the citizens of india where criteria is female, age above 60, annual income less than 2 lakh
'''a=input("enter the gender of candidate(M/F): ")
b=int(input("enter the age of candidate: "))
c=float(input("enter the income in lakh per annum: "))
if a=="F":
    if b>60 or b==60:
        if c<2 or c==2:
            print("pension can be granted")
        else:
            print("pension cant be granted due to exeeded salary")
    else:
        print("pension cant be granted due to age not reached")
else:
    print("pension can only be granted to females")'''

#3/9/25

#wap to take age as input and if less than 18 and less than 0 to check
'''age=int(input("enter the age: "))
if age >18:
    print("you are above 18")
elif age<0:
    print("age cannot be less than 0")
elif age<18:
    print("you are less than 18")
elif age==18:
    print("you are 18")

'''
#